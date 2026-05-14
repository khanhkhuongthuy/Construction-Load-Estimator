# Commit 3: Add error handling (empty file, invalid data, missing file)

import os

def read_materials(filename):
    if not os.path.exists(filename):
        print(f"Error: Input file '{filename}' does not exist.")
        return []

    materials = []
    with open(filename, "r") as file:
        for line in file:
            clean = line.split("#")[0].strip()
            if clean:
                name, weight, qty = clean.split()
                materials.append((name, float(weight), int(qty)))
                continue

            parts = clean.split()
            if len(parts) != 3:
                print(f"Warning: Skipping invalid line: {line.strip()}")
                continue

            name, weight, qty = parts

            try:
                weight = float(weight)
                qty = int(qty)
            except ValueError:
                print(f"Warning: Invalid number format in line: {line.strip()}")
                continue

            materials.append((name, weight, qty))
    
    return materials


def calculate_total_weight(materials):
    total = 0
    for name, weight, qty in materials:
        total += weight * qty
    return total


if __name__ == "__main__":
    materials = read_materials("materials.txt")

    if not materials:
        print("Error: No valid material data found. Exiting.")
        exit()

    total_weight = calculate_total_weight(materials)
    overhead = total_weight * 0.15
    final_weight = total_weight + overhead

    print("Total weight (kg):", total_weight)
    print("Overhead (10%):", overhead)
    print("Final weight with overhead:", final_weight)

    # Write output file
    with open("report.txt", "w") as out:
        out.write(f"Total weight: {total_weight} kg\n")
        out.write(f"Overhead (10%): {overhead} kg\n")
        out.write(f"Final weight: {final_weight} kg\n")
