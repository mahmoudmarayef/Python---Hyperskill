# write your code here

class Formatter:
    def __init__(self):
        self.dn = 0
        self.f = ["plain", "bold", "italic", "link", "inline-code", "header", "new-line", "ordered-list", "unordered-list"]
        self.se = ""

    def choose_format(self):
        while self.dn == 0:
            ch = input('Choose a formatter: ')
            if ch in self.f:
                if ch == "header":
                    self.header()
                elif ch == "bold":
                    self.bold()
                elif ch == "plain":
                    self.plain()
                elif ch == "italic":
                    self.italic()
                elif ch == "inline-code":
                    self.inline_code()
                elif ch == "link":
                    self.link()
                elif ch == "new-line":
                    self.new_line()
                elif ch == "ordered-list":
                    self.ordered_list()
                elif ch == "unordered-list":
                    self.unordered_list()
            elif ch == '!done':
                f = open("output.md", "w")
                f.write(self.se)
                f.close()
                self.dn = 1
            else:
                print('Unknown formatting type or command')

    def header(self):
        while True:
            level = input("Level: ")
            if 1 < int(level) > 6:
                print("The level should be within the range of 1 to 6")
                continue
            else:
                text = input("Text: ")
                sign = "#" * int(level)
                self.se += f"{sign} {text}\n"
                print(self.se)
                break

    def bold(self):
        text = input("Text: ")
        self.se += f"**{text}**"
        print(self.se)

    def plain(self):
        text = input("Text: ")
        self.se += text
        print(self.se)

    def italic(self):
        text = input("Text: ")
        self.se += f"*{text}*"
        print(self.se)

    def inline_code(self):
        text = input("Text: ")
        self.se += f"`{text}`"
        print(self.se)

    def link(self):
        label = input("Label: ")
        url = input("URL: ")
        self.se += f"[{label}]({url})"
        print(self.se)

    def new_line(self):
        self.se += "\n"
        print(self.se)

    def ordered_list(self):
        while True:
            rows = input("Number of rows: ")
            if int(rows) <= 0:
                print("The number of rows should be greater than zero")
                continue
            else:
                for i in range(1, int(rows) + 1):
                    row = input(f"Row #{i}: ")
                    self.se += f"{i}. {row}\n"
                print(self.se)
                break

    def unordered_list(self):
        while True:
            rows = input("Number of rows: ")
            if int(rows) <= 0:
                print("The number of rows should be greater than zero")
                continue
            else:
                for i in range(1, int(rows) + 1):
                    row = input(f"Row #{i}: ")
                    self.se += f"* {row}\n"
                print(self.se)
                break


f1 = Formatter()
f1.choose_format()
