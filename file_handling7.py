import csv

with open("input_file.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["age"])
