with open("file.txt") as f:
    while True:
        line = f.readline()
        if not line:
            break
        if "ERROR" in line:
            print("Found error:", line.strip())
