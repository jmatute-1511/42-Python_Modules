import sys

def check_args(sys):
	if len(sys.argv) == 1:
		return True
	return False

    
def change_str(sys):
    str = ''
    if check_args(sys) == True:
        return
    else:
        for it in sys.argv :
            if it == sys.argv[0]:
                continue
            str += it + ' '
    rev = "".join(reversed(str.strip()))
    return rev.swapcase()

def main(sys):
    print(change_str(sys))

main(sys)
            