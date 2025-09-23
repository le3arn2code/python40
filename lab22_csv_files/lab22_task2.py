import csv

file_path = "sample.csv"

with open(file_path, mode="r") as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        print(row)
