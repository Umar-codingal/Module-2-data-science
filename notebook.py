f = open("science-notes.txt","w")
f.write("Humans dont have cell walls\n")
f.write("v=ir\n")
f.write("Uranium 235 is used as fuel in nuclear reactors\n")
f.close()


f = open("Math-notes.txt","w")
f.write("a^2 + b^2 = c^2\n")
f.write("sin^2(x) + cos^2(x) = 1\n")
f.write("sum of angles in a triangle = 180 degrees\n")
f.close()

print("Notes saved!")

import os

print("--- Science Notes ---")
with open("science-notes.txt", "r") as f:
    for line in f:
        print(line.strip())
print()

print("=== Word count ====")
with open("science-notes.txt", "r") as f:
    for line in f :
        print(line.strip())
        print("Word count:", len(line.split()))

print()

print("=== Merging notes ===")
if os.path.exists("merged-notes.txt"):
    print("Merged notes already exists. Deleting the old file.")
else:
    print("Creating merged notes file.")


content = ""
with open("science-notes.txt", "r") as f:
    content += "=== science-notes.txt ===\n"
    content += f.read() + "\n"
with open("Math-notes.txt", "r") as f:
    content += "=== Math-notes.txt ===\n"
    content += f.read() + "\n"
with open("merged-notes.txt", "w") as out:
    out.write(content)  

print("saved to merged-notes.txt")
print()

if os.path.exists("merged-notes.txt"):
    os.remove("merged-notes.txt")
    print("merged-notes.txt deleted.")
else:
    print("merged-notes.txt does not exist.")
