from rapidfuzz import process, fuzz
import os
import re

def parse_cellosaurus_synonyms(filepath="cellosaurus.txt"):
    cell_dict = {}
    current_entry = {}
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            if line.startswith('ID   '):
                current_entry = {"name": line.strip().split('ID')[1].strip(), "synonyms": []}
            elif line.startswith('SY   '):
                synonyms_line = line.strip().split('SY')[1].strip().rstrip(';')
                synonyms = [syn.strip() for syn in synonyms_line.split(';')]
                current_entry["synonyms"].extend(synonyms)
            elif line.startswith('//'):
                primary_name = current_entry["name"]
                synonyms = current_entry["synonyms"] + [primary_name]
                for synonym in synonyms:
                    cell_dict[synonym.lower()] = primary_name
    return cell_dict

def match_cell_line(user_input, cell_dict, threshold=80):
    matches = process.extract(user_input.lower(), cell_dict.keys(), scorer=fuzz.token_sort_ratio, limit=5)
    best_match, score, _ = matches[0]
    if score >= threshold:
        return cell_dict[best_match]  # returns standardized cell line name
    else:
        return None

# Usage example:
cell_dict = parse_cellosaurus_synonyms()

user_input = input("Enter cell line name: ")
standardized_name = match_cell_line(user_input, cell_dict)

if standardized_name:
    print(f"Matched standardized name: {standardized_name}")
else:
    print("No confident match found.")
