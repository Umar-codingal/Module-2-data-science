
def print_factors(number):
    factors=[]
    print("The factors of", number,"are: ")
    for i in range (1, number +1):
        if number%i == 0:
            factors.append (i)
            print(factors)
            
    for j in factors:
        if len(j) == 2:
            print("Its a prime")
        else:
            print("not a prime")

        

number = int(input("Enter your number to find it's factors: "))

# def prime_check(factors):
#     for j in factors:
#         if len(j) == 2:
#             print("Its a prime")
#         else:
#             print("not a prime")

      
print_factors(number)
# prime_check(factors)