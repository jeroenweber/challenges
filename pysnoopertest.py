import pysnooper

@pysnooper.snoop("log.txt")
def total(number):
    sum = 0
    for element in numbers:
        sum = sum + element
    return sum

numbers = [9,10,6,2,3,20,5]
print(total(numbers))