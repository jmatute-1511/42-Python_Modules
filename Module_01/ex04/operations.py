import sys

def main(sys):
    if len(sys.argv) != 3:
        return
    num1 =  int(sys.argv[1])
    num2 = int(sys.argv[2])
    print("Sum		", num1 + num2)
    print("Diferences:	", num1 - num2)
    print("Product:	", num1 * num2)
    if num2 != 0:
        print("Quotient:	", num1 / num2)
        print("Reamainder:	", num1 % num2)
    else:
        print("Quotient:	", "ZeroDivisionError: division by zero")
        print("Reamainder:	", "ZeroDivisionError: modulo by zero")
   
    
main (sys)