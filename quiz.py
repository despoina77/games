def new_game():
    guesses = []
    correct_guess = 0
    num_quest = 1

    for key in questions:
        print()
        print(key)
        for i in options[num_quest-1]:
            print(i)
        guess = input("Enter(A,B,C or D): ").upper()
        guesses.append(guess)

        correct_guess += check_answer(questions.get(key), guess)

        num_quest += 1
    display_score(correct_guess, guesses)
def check_answer(answer, guess):

   if answer == guess:
       print("Bravo!!")
       return  1
   else:
       print("Wrong!!")
       return  0
def display_score(correct_guesses, guesses):
    print()
    print("RESULTS")

    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end="")
    print()

    print("GUESSES: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("Your Score is: "+str(score)+"%")


def play_again():
    response = input("Do you want play again? (Y/N): ").upper()
    if response == "Y":
        return True
    else:
        return  False
questions = {
      "About how many computer languages are in use?: ": "A",
      "Which of these is not an early computer?: ": "B",
      "Who founded Apple Computer?: ": "A",
      "Which of these is not a peripheral, in computer terms?: ": "D"
}

options = [["A. 2000", "B. 50", "C. 20", "D. 5000"],
           ["A. SAGE", "B. NASA", "C. ENIAC", "D. UNIVAC"],
           ["A. Steve Jobs", "B. Sundar Pichai", "C. Bill Gates", "D. Sheryl Sandberg"],
           ["A. monitor", "B. mouse", "C. keyboard", "D. motherboard"]]

new_game()
while play_again():
    new_game()

print("Thanks for playing!")
