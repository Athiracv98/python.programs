'''def cube(number):
    cu=number**3
    return cu

def by_three(number):
    if number%3==0:
        return cube(number)

    else:
       return False

print("cube is",by_three(5))'''
def maximum(a):
    for i in a:
        ma=max(a)
        return ma
def minimum(a):
    for i in a:
        mi=min(a)
    return mi

list=[1,2,3,4]
print(minimum(list))
print(maximum(list))

'''def find_minimum(numbers):
    min_num = numbers[0]
    for num in numbers:
        if num < min_num:
            min_num = num
    return min_num

def find_maximum(numbers):
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
            
            
            
            
            
              
    return max_num

# Main program
number_list = [5, 9, 2, 7, 1, 8]
minimum = find_minimum(number_list)
maximum = find_maximum(number_list)

print("Minimum number:", minimum)
print("Maximum number:", maximum)'''


