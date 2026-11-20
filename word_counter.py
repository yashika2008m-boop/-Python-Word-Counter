
print("===== WORD COUNTER =====")

try:
    filename = input("Enter file name: ")

    with open(filename, "r") as file:
        content = file.read()

    words = content.split()
    count = len(words)

    print("Total number of words:", count)

except FileNotFoundError:
    print("Error: File not found!")

