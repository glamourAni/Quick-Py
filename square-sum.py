def square(n: int) -> int:
    return n * n

def sum_of_squares(num: int) -> int:
    # natNo = 1
    _sum = square(num)

    while (num > 0):
        _sum = _sum + square(num - 1)
        num -= 1
    
    return _sum

def square_of_sum(num: int) -> int:
    _sum = num

    while (num > 0):
        _sum += num-1
        num -= 1
    return square(_sum)

def difference(num: int) -> int:
    return (square_of_sum(num) - sum_of_squares(num))

# testcases = [1, 5, 10,100]
# for testcase in testcases:
#    res = difference(testcase)
#    print(f"Difference between the sum of the squares of the first {testcase} natural numbers and the square of the sum is {res}\n")


    

