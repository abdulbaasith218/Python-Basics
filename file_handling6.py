#here we are going to read the csv file then we should write that data in another file

with open("input_file.csv", "r") as infile, open("output_file.csv", "w") as outfile:
    for line in infile:
        print(line.strip())
        outfile.write(line)
