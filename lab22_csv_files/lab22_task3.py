import csv

file_path = "sample.csv"

print("Case 1: With header")
with open(file_path, mode="r") as file:
    csv_reader = csv.reader(file)
    header = next(csv_reader)  # Skip the header
    for row in csv_reader:
        print(row)

print("\nCase 2: Without header")
with open(file_path, mode="r") as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        print(row)
