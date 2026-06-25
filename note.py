f = open("history-notes.txt","w")
f.write("1923 - Ruhr Crisis\n")
f.write("1939 - Invasion of Poland\n")
f.write("1945 - Atomic Bombing of Hiroshima\n")
f.write("1953 - soviet nuclear test\n")
f.write("1962 - Cuban Missile Crisis\n")
f.write("1989 - Fall of the Berlin Wall\n")
f.close()


f = open("economics-notes.txt","w")
f.write("Economics is the study of how societies allocate resources.\n")
f.write("Supply and demand determine market prices.\n")
f.write("Inflation is a sustained increase in the general price level.\n")
f.close()

print("Notes saved!")

import os

print("--- History Notes ---")
with open("history-notes.txt", "r") as f:
    for line in f:
        print(line.strip())
print()

print("=== Word count ====")
with open("history-notes.txt", "r") as f:
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
with open("history-notes.txt", "r") as f:
    content += "=== history-notes.txt ===\n"
    content += f.read() + "\n"
with open("economics-notes.txt", "r") as f:
    content += "=== economics-notes.txt ===\n"
    content += f.read() + "\n"
with open("merged-notes.txt", "w") as out:
    out.write(content)  

print("saved to merged-notes.txt")
print()