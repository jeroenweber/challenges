#Vind het maximum product van twee getallen in een reeks positieve getallen, poging 1
# input: [1, 3, 24, 6, 25, 13, 14, 4, 5, 18, 40]
# output: 1000


def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,numbers[first] * numbers[second])
    return max_product

if __name__ == '__main__':
    #input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))


