import csv

file_path = "sample.csv"
data_list = []

with open(file_path, mode="r") as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        data_list.append(row)

for item in data_list:
    print(item)
