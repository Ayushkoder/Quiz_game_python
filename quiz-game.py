print("Welcome to my computer quiz!")

playing = input("Do you want to play? (yes/no): ")
if playing.lower() != "yes":
    quit()

score = 0
print("Okay, let's play!")

answer = input("What does TPU stand for? ")
print(f"Debug:the answer : {answer}")
if (answer.strip().lower()) == "tensor processing unit":
    print("You are absolutely right!")
    score += 1
else:
    print("It is an incorrect answer.")

answer2 = input("What does DPU stand for? ")
print(f"Debug:the answer : {answer2}")
if (answer2.strip().lower()) == "data processing unit":
    print("It is correct!")
    score += 1
else:
    print("It is incorrect, try again.")

print(f"Your final score is: {score}")
