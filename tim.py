#rekenmachine met een operator +, - , *, /
# string
import re

operators = ['x','-','+','/']
opmatch = '[0-9]*[+,-,*,/][0-9]*'

def readop():
    calc = input('your operation: ')
    print('your input: ' + calc)
    return calc

def checkandeval(calc):
    try:
        match = re.search(opmatch,calc)
        print('evaluates to: ' + str(eval((match.group(0)))))
    except Exception as e:
        print("An exception occurred: ", e)

while True:
    checkandeval(readop())

