# write your code here
import random


def quiz():
    print("""
Which level do you want? Enter a number:
1 - simple operations with numbers 2-9
2 - integral squares of 11-29
    """)
    while True:
        quiz_level = int(input())
        if quiz_level == 1:
            ans = easy_level()
            print(f"Your mark is {ans}/5. Would you like to save the result? Enter yes or no.")
            save_result = input()
            if save_result == "yes" or save_result == "Yes" or save_result == "y":
                user_name = input("What is your name?\n")
                f = open("results.txt", "a")
                f.write("%s: %s/5 in level 1 (simple operations with numbers 2-9)\n" % (user_name, ans))
                f.close()
                print('The results are saved in "results.txt".')
            break
        elif quiz_level == 2:
            ans = hard_level()
            print(f"Your mark is {ans}/5. Would you like to save the result? Enter yes or no.")
            save_result = input()
            if save_result == "yes" or save_result == "Yes" or save_result == "y":
                user_name = input("What is your name?\n")
                f = open("results.txt", "a")
                f.write("%s: %s/5 in level 2 (integral squares of 11-29)\n" % (user_name, ans))
                f.close()
                print('The results are saved in "results.txt".')
            break
        else:
            print("Incorrect format.")
            continue


def check_input():
    while True:
        try:
            user_answer = int(input())
            return user_answer
        except ValueError:
            print("Incorrect format.")


def easy_level():
    i = 0
    result = 0
    right_ans = 0
    while i < 5:
        i += 1
        x = random.randint(2, 9)
        y = random.randint(2, 9)
        opr = ["+", "-", "*"]
        opera = random.choice(opr)

        print(f"{x} {opera} {y}")

        if opera == "+":
            result = int(x) + int(y)
        elif opera == "-":
            result = int(x) - int(y)
        elif opera == "*":
            result = int(x) * int(y)

        answer = check_input()
        if answer == result:
            right_ans += 1
            print("Right!")
        else:
            print("Wrong!")
    return right_ans


def hard_level():
    i = 0
    result = 0
    right_ans = 0
    while i < 5:
        i += 1
        x = random.randint(11, 29)
        print(x)
        result = pow(x, 2)
        answer = check_input()
        if answer == result:
            right_ans += 1
            print("Right!")
        else:
            print("Wrong")
    return right_ans


quiz()
