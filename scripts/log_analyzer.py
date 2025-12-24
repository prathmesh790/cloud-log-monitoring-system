from collections import Counter

log_file = "../logs/app.log"
ERROR_THRESHOLD = 100

levels = []

with open(log_file, "r") as f:
    for line in f:
        if " - " in line:
            level = line.split(" - ")[1]
            levels.append(level)

counts = Counter(levels)

print("\nLog Summary:")
for level, count in counts.items():
    print(f"{level}: {count}")

# Alert condition
if counts.get("ERROR", 0) > ERROR_THRESHOLD:
    print("\nALERT: High number of ERROR logs detected!")

