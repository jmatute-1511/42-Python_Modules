import sys

def tellme_whois(num):
    if num == 0:
        return "I'm Zero"
    elif num % 2 == 0:
        return "I'm Even"
    else:
        return "I'm Odd"

def first_prog(sys):
    if len(sys.argv) != 2:
        return
    else:
        num = int(sys.argv[1])
        print(tellme_whois(num))
    return

first_prog(sys)