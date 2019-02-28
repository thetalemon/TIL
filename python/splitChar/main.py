import sys

args = sys.argv

print(args)

argsList = list(args[1])

for item in argsList :
    print(item + ", "),
