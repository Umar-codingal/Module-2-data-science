file=open("shoppinglist.txt","w")
file.write("1. Milk\n")
file.write("2. Bread\n")
file.write("3. Eggs\n")
file.write("4. Butter\n")
file.close()


print("Shopping list saved!")


file=open("shoppinglist.txt","r")
content=file.read()
print("\n==== My Shopping list ====\n")
print(content)
file.close()

file=open("shoppinglist.txt","r")
content=file.readlines()
print(f"You have {len(content)} items in your shopping list")
file.close()

file=open("shoppinglist.txt","a")
file.write("5. Cheese\n")
file.write("6. Fruits\n")
file.close()

file=open("shoppinglist.txt","r")
print("\n==== Updated Shopping list ====\n")
print(file.read())
file.close()

