# Commit 1: Read material weights and quantities from file

def read_materials(filename):
    materials = []
    with open(filename, "r") as file:
        for line in file:
            clean = line.split("#")[0].strip()
            if clean:
                name, weight, qty = clean.split()
                materials.append((name, float(weight), int(qty)))
    return materials


def calculate_total_weight(materials):
    total = 0
    for name, weight, qty in materials:
        total += weight * qty
    return total


if __name__ == "__main__":
    materials = read_materials("materials.txt")

    total_weight = calculate_total_weight(materials)
    overhead = total_weight * 0.10
    final_weight = total_weight + overhead

    print("Total weight (kg):", total_weight)
    print("Overhead (10%):", overhead)
    print("Final weight with overhead:", final_weight)

    # Write output file
    with open("report.txt", "w") as out:
        out.write(f"Total weight: {total_weight} kg\n")
        out.write(f"Overhead (10%): {overhead} kg\n")
        out.write(f"Final weight: {final_weight} kg\n")
