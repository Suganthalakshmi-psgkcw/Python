file = "sample.txt"

# Write data to file (overwrite mode)
with open(file, "w") as f:
    f.write("Python is easy to learn.\n")
    f.write("File handling is important.\n")

# Append data to file
with open(file, "a") as f:
    f.write("Practice makes perfect.\n")

# Read file content
with open(file, "r") as f:
    text = f.read()

# Display content
print("File Content:\n", text)

# Count lines, words, characters
print("Lines:", text.count("\n"))
print("Words:", len(text.split()))
print("Characters:", len(text))
print("Python count:", text.count("Python"))
