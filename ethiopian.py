def hello():
    print('Good Luck!')
    
def halve(x):
    return x // 2

def double(x):
    return x * 2

def even(x):
    return not x % 2

def ethiopian(num1, num2):
    print("Ethiopian multiplication of %i and %i" %
            (num1, num2))
    
    result = 0
    
    while num1 >= 1:
        if even(num1):
            print("%4i %6i DELETE" %
                    (num1, num2))
        else:
            print("%4i %6i KEEP" %
                    (num1, num2))
            result += num2
            
        num1 = halve(num1)
        num2 = double(num2)
        
    return result


if __name__ == '__main__':
    num1 = int(input("Enter first number >> "))
    num2 = int(input("Enter second number >> "))
    result = ethiopian(num1, num2)
    print(f"{num1} x {num2} = {result}")
    hello()
