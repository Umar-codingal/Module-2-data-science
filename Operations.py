n= int(input("How many characters to preview: "))
file= open("shoppinglist.txt","r")
print(file.read(n))
file.close()
print()

file= open("shoppinglist.txt","r")
lines=file.readlines()
print(f"you have {len(lines)} items in your shopping list")
for i in range(len(lines)):
    print(i+1,"->",lines[i].strip())
print()

word=input("Skip lines starting with: ")
file= open("shoppinglist.txt","r")
for line in file:
    if not line.startswith(word):
        print("Skip ->",line.strip())
    else:
        print("keep ->",line.strip())

file.close()
print()


