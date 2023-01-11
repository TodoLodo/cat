import os

binPath = os.getcwd() + r"\bin"

print("\nAdding bin folder to path...\n")

print(rf'setx /M path "%path%;{binPath}"')

os.system(rf'setx /M path "%path%;{binPath}"')

input()