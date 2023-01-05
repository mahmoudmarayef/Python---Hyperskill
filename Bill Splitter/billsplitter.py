# write your code here
import random
people = int(input("Enter the number of friends joining (including you):\n"))
names = []
share = {}

if people <= 0:
    print("No one is joining for the party")
else:
    print("Enter the name of every friend (including you), each on a new line:")
    for _ in range(people):
        name = input()
        names.append(name)

    bill = int(input("Enter the total bill value:\n"))
    bill_per_person = round(bill / len(names), 2)

    for name in names:
        share[name] = bill_per_person

    who_is_lucky = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:\n')

    if who_is_lucky == "Yes":
        random_key = random.choice(list(share))
        print(f"{random_key} is the lucky one!")

        new_bill = round(bill / (len(names) - 1), 2)
        for name in names:
            share[name] = new_bill
            
        share[random_key] = 0
    else:
        print("No one is going to be lucky")

    print(share)
