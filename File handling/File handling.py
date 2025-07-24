# Step 1: Create or overwrite file
with open("journal.txt", "w") as file:
    file.write("This is the start of my journal.\n")
    file.write("Day 1: Feeling motivated!\n")

# Step 2: Read the file
print("Step 2: Reading current journal:")
with open("journal.txt", "r") as file:
    content = file.read()
    print(content)

# Step 3: Append a new entry
new_entry = input("Step 3: Enter your new journal entry: ")
with open("journal.txt", "a") as file:
    file.write(f"{new_entry}\n")

# Step 4: Overwrite the beginning with a title
with open("journal.txt", "r+") as file:
    file.seek(0)
    file.write("--- MY JOURNAL ---\n")

print("Done! Check 'journal.txt' for updates.")
