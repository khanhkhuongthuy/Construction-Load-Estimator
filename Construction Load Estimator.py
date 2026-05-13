# Commit 1: Read data from file

def read_tasks(filename):
    tasks = []
    with open(filename, "r") as file:
        for line in file:
            # Remove comments and whitespace
            clean = line.split("#")[0].strip()
            if clean:
                tasks.append(int(clean))
    return tasks

if __name__ == "__main__":
    tasks = read_tasks("tasks.txt")
    print("Loaded task durations (minutes):")
    print(tasks)
