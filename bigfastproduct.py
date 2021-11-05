#Vind het maximum product van twee getallen in een reeks positieve getallen, poging 2
def maximum_out(numbers):
    index = 0
    n = len(numbers)
    max = numbers[index]
    for i in range(1, n):
        if (numbers[i] > max):
            index = i
            max = numbers[i]
    numbers.pop(index)
    return max

def max_pairwise_product(numbers):
    return maximum_out(numbers) * maximum_out(numbers)

if __name__ == '__main__':
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))