
def print_factors(number):
    print("The factors of", number,"are: ")
    for i in range (1, number +1):
        if number%i == 0:
            print(i)
            
    

number = int(input("Enter your number to find it's factors: "))

def prime_check(number):
    if number<2:
        return False

    for j in range(2,int(number**0.5)+1):
        if number % j == 0:
           return False
        else:
            print("prime")


    
# print_factors(number)
prime_check(number)