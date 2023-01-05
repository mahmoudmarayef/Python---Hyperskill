class Coffee:
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.cups = 9
        self.money = 550
        self.action = ""
        self.option = ""

    def main(self):
        while True:
            self.action = input("Write action (buy, fill, take, remaining, exit):\n")
            if self.action == "buy":
                self.buy()
            elif self.action == "take":
                self.take()
            elif self.action == "fill":
                self.fill()
            elif self.action == "remaining":
                self.remaining()
            elif self.action == "exit":
                exit()

    def remaining(self):
        print(f"""
The coffee machine has:
{self.water} ml of water
{self.milk} ml of milk
{self.beans} g of coffee beans
{self.cups} disposable cups
${self.money} of money
        """)

    def buy(self):
        self.option = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n")
        if self.option == "1":
            if self.water >= 250 and self.beans >= 16 and self.cups >= 1:
                self.water -= 250
                self.beans -= 16
                self.money += 4
                self.cups -= 1
                print("I have enough resources, making you a coffee!")
            else:
                print("Sorry, not enough water!")
        elif self.option == "2":
            if self.water >= 350 and self.milk >= 75 and self.beans >= 20 and self.cups >= 1:
                self.water -= 350
                self.milk -= 75
                self.beans -= 20
                self.money += 7
                self.cups -= 1
                print("I have enough resources, making you a coffee!")
            else:
                print("Sorry, not enough water!")
        elif self.option == "3":
            if self.water >= 200 and self.milk >= 100 and self.beans >= 12 and self.cups >= 1:
                self.water -= 200
                self.milk -= 100
                self.beans -= 12
                self.money += 6
                self.cups -= 1
                print("I have enough resources, making you a coffee!")
            else:
                print("Sorry, not enough water!")

    def take(self):
        print(f"I gave you ${self.money}")
        self.money = 0

    def fill(self):
        add_water = int(input("Write how many ml of water you want to add:\n"))
        add_milk = int(input("Write how many ml of milk you want to add:\n"))
        add_beans = int(input("Write how many grams of coffee beans you want to add:\n"))
        add_cups = int(input("Write how many disposable cups you want to add:\n"))
        self.water += add_water
        self.milk += add_milk
        self.beans += add_beans
        self.cups += add_cups


machine = Coffee()
machine.main()

