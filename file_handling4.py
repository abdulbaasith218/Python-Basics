
#instead of read you can use the readline
#read: before read it will keep the data , i mean small file data
#     that can not take and keep the large file (like a GB size file)

#so in the large file situation we should use the readline()
#this will take the line by line data


with open("data.txt", "r") as file:
    print(file.readline().strip())
    print(file.readline().strip())
    print(file.readline().strip())

#to read the line by line data , we have to use readline() no of times
#to avoid this we will use the loop function


with open("data.txt", "r") as file:
    for line in file:
        print(line.strip())
