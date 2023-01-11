import sys


__version__ = "1.0.0"
__author__ = "Todo Lodo"


class Cat:
    def __init__(self, args):
        self.numbered = False
        self.ending = False

        self.n = 0

        if "-v" in args or "--version" in args:
            print(__version__)
            exit(0)

        if "-n" in args:
            self.numbered = True
            args.remove("-n")
        if "-E" in args:
            self.ending = True
            args.remove("-E")

        if len(args) == 0:
            self.interactive()

        for file in args:
            with open(file, "r") as f:
                for line in f.readlines():
                    self.display(line.strip("\n"))
                    self.n += 1


    def interactive(self):
        while True:
            user = input()
            self.display(user)
            self.n += 1

    def display(self, line):
        print(f"{f'{self.n} ' if self.numbered else ''}{line}{'$' if self.ending else ''}")


if __name__ == '__main__':
    Cat(sys.argv[1:])
