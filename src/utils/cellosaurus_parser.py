import os
import re
from rapidfuzz import process, fuzz


def parse_cellosaurus_synonyms(filepath=None):
    """
    Parses the Cellosaurus flat file to build a mapping
    from each synonym (lowercased) to its standardized cell line name.

    If `filepath` is not provided, defaults to `data/cellosaurus.txt` located two
    directories up from this script.
    """
    if filepath is None:
        here = os.path.dirname(__file__)
        filepath = os.path.abspath(
            os.path.join(here, '..', '..', 'data', 'cellosaurus.txt')
        )

    cell_dict = {}
    current_entry = {"name": None, "synonyms": []}

    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            # Start of a new entry
            if line.startswith('ID   '):
                current_entry = {"name": line.split('ID   ')[1].strip(), "synonyms": []}
            elif line.startswith('SY   '):
                synonyms_line = line.split('SY   ')[1].strip().rstrip(';')
                synonyms = [syn.strip() for syn in synonyms_line.split(';') if syn.strip()]
                current_entry["synonyms"].extend(synonyms)
            elif line.startswith('//'):
                # End of entry: register primary name and its synonyms
                primary = current_entry.get("name")
                if primary:
                    all_names = current_entry.get("synonyms", []) + [primary]
                    for name in all_names:
                        cell_dict[name.lower()] = primary
    return cell_dict


def match_cell_line(user_input, cell_dict, threshold=80):
    """
    Fuzzy-matches a user input string against the keys in `cell_dict`.
    Returns the standardized cell line name if the top match score >= threshold;
    otherwise returns None.
    """
    user_input_l = user_input.lower()
    matches = process.extract(
        user_input_l,
        cell_dict.keys(),
        scorer=fuzz.token_sort_ratio,
        limit=5
    )
    if not matches:
        return None

    best_match, score, _ = matches[0]
    if score >= threshold:
        return cell_dict[best_match]
    return None
