# src/calculations.py

def estimate_split_time(cell_line: str,
                        doubling_time: float,
                        start_density: float,
                        days_passed: float):
    """
    Estimates current cell density (0–1) based on starting density and
    elapsed days, then prints whether you should split.
    """
    hours_passed = days_passed * 24
    doublings = hours_passed / doubling_time
    estimated_density = start_density * (2 ** doublings)

    print(f"\n{cell_line} estimate:")
    print(f"Estimated current density: {min(estimated_density, 1.0):.2f} (1.0 = confluency)")

    if estimated_density >= 0.9:
        print("✅ You should split your cells.")
    elif estimated_density >= 0.7:
        print("⚠️  Cells are approaching confluency.")
    else:
        print("🕒 Still growing, no need to split yet.")
