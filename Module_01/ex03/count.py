import sys
import string

def upper_count(str):
    return len(list(filter(lambda x: x in string.ascii_uppercase, str)))

def lower_count(str):
    return len(list(filter(lambda x: x in string.ascii_lowercase, str)))

def space_count(str):
    return len(list(filter(lambda x: x in " ", str)))
def punctuation_count(str):
    return len(list(filter(lambda x: x in string.punctuation, str)))

def main_prog(sys):
    print(upper_count(sys.argv[1]), "upper letter(s)")
    print(lower_count(sys.argv[1]), "lower letter(s)")
    print(punctuation_count(sys.argv[1]), "punctuation mark(s)")
    print(space_count(sys.argv[1]), "spaces")
    return
    
main_prog(sys)