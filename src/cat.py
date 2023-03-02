import sys


__version__ = "1.0.1"
__author__ = "Todo Lodo"


class Cat:
    def __init__(self, args):
        self.numbered = False
        self.ending = False

        self.n = 0


        if len(args) == 0:
            self.interactive()

        else:
            if args in ["-v", "--version"]:
                print(__version__)
                exit(0)

            if args in ["-h", "--help"]:
                print("cat [files] [options]\n"
                      "\n"
                      "options:\n"
                      "\t-v, --version  : prints current version\n"
                      "\t-n             : Index each line while printing out contents of a file\n"
                      "\n-E             : prints out a '$' for each new line tag\n"
                      "\n"
                      "Example:"
                      "\tsingle file:\n"
                      "\t\tcat file -n\n"
                      "\n"
                      "\tmultiple files:\n"
                      "\t\tcat file1 file2 file3 -n")
                exit(0)

            if "-n" in args:
                self.numbered = True
                args.remove("-n")
            if "-E" in args:
                self.ending = True
                args.remove("-E")

            for file in args:
                with open(file, "r") as f:
                    for line in f.readlines():
                        self.display(line.replace("\n", "$" if self.ending else ""))
                        self.n += 1


    def interactive(self):
        while True:
            user = input()
            self.display(user)
            self.n += 1

    def display(self, line):
        print(f"{f'{self.n} ' if self.numbered else ''}{line}")


if __name__ == '__main__':
    Cat(sys.argv[1:])
