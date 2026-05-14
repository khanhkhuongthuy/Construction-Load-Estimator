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

if __name__ == "__main__":
    materials = read_materials("materials.txt")
    print("Loaded materials (name, weight per item, quantity):")
    print(materials)
