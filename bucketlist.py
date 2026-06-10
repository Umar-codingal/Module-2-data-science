file = open("bucketlist.txt","w")
file.write("1. Travel for 6 months a year\n")
file.write("2. Learn a new skill every month\n")
file.write("3. Finsh a book every fortnight\n")
file.close()

print("Bucket saved!")


file=open("bucketlist.txt","r")
content=file.read()
print("\n==== My Bucket list ====\n")
print(content)
file.close()

file=open("bucketlist.txt","r")
content=file.readlines()
print(f"you have {len(content)} items in your bucket list")
file.close()


file= open("bucketlist.txt","a" )
file.write("4. Have a good impact on the society")
file.write("\n5. Stay fit ")
file.close()

file=open("bucketlist.txt","r")
print("\n==== Updated Bucket list ====\n")
print(file.read())
file.close()
