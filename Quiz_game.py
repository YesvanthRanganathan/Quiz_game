print("--------- WELCOME TO PYTHON QUIZ GAME :)--------")
def quiz_game():
    guesses=[]
    correct_guesses=0
    question_number=1

    for key in questions:
        print("----------")
        print(key)
        for i in choices[question_number - 1]:
            print(i)
        user_input = input("Enter Your Choice(A,B,C OR D):").upper()
        guesses.append(user_input)
        correct_guesses = correct_guesses + check_answer(questions.get(key), user_input)
        question_number = question_number + 1


    display_score(correct_guesses, guesses)


def check_answer(answer, user_input):
    if answer == user_input:
        print("Correct!!")
        return 1
    else:
        print("Wrong!!")
        return 0


def display_score(correct_guesses, guesses):
    print("--------")
    print("------RESULTS!-----")
    # ---> Line 28 to 31 If you want to know the original answer you can use
    # print("ANSWER",end=" ")
    # for key in questions:
    #   print(questions.get(key),end="")#->this question.get(key) is used to print the key values in answer
    # print()
    print("USER_ANSWER", end=" ")
    for i in guesses:
        print(i, end="")
    print()
    score = int((correct_guesses / len(questions)) * 100)
    print("Your Score is " + str(score) + "/100")
    if score == 100:
        print("Congratulations!!")


def play_again():
    playagain = input("Do you want to Platagain(YES or NO):").upper()

    if playagain == "YES":
        return True
    else:
        return False


questions={"Which Programming languages is basic to learn":"C",
           "Which Programming Language is Very easy to  learn":"B",
           "Who created Python Programming:":"A",
           "Which Year Python Program was created :":"A",
           "Python is Interpreted or Compiler language :":"A"}

choices=[["A : Java","B : Python","C : C","D : C++"],
         ["A : Java","B : Python","C : JavaScript","D : C"],
         ["A : Gudio van Rossum","B : Elon mask","C : Bill Gates","D : Mark Antony"],
         ["A : 1991","B : 1947","C : 1987","D : 1995"],
         ["A : Interpreted","B : Compile","C : Both A & B","D : All the above"]]

quiz_game()

while play_again():
    quiz_game()
print("Thanks for Playing this game!!!!")