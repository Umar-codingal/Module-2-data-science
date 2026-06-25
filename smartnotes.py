file = open("To-Do List.txt","w")
file.write("Travel for 6 months a year\n")
file.write("Learn a new skill every month\n")
file.write("Finish a book every fortnight\n")
file.write("Have a good impact on the society\n")
file.write("Stay fit\n")
file.write("Spend more time with family\n")
file.write("Save money\n")
file.write("Volunteer for a cause\n")
file.write("Take care of mental health\n")
file.write("Explore new hobbies\n")
file.close()

print("To-Do List saved!")

n= int(input("How many characters to preview: "))
file= open("To-Do List.txt","r")
print(file.read(n))
file.close()
print()


file= open("To-Do List.txt","r")
lines=file.readlines()
print(f"you have {len(lines)} items in your To-Do List")
for i in range(len(lines)):
    print(i+1,"->",lines[i].strip())
print()

word=input("Skip lines starting with: ")
file= open("To-Do List.txt","r")
for line in file:
    if  line.startswith(word):
        print("Skip ->",line.strip())
    else:
        print("keep ->",line.strip())

file.close()
print()

file= open("To-Do List2.txt","w")
file.write("To-Do List.txt")
file.write("============\n")
file.close()
print("To-Do List2 saved!")
