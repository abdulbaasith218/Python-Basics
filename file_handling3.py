with open("notes.txt", "r") as file:
    for line in file:
        print(line.strip())


#by using the with here , it means that automatically close
#every time you do not have to put the close
#strip() : if we put this that will avoid excess space in the start and end



feedback = input("Enter your feedback: ")

with open("feedback_log.txt", "a") as log:
    log.write(feedback + "\n")

print("Thanks! Your feedback is saved.")
