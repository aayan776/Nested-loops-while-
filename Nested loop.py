i = 1
while i <= 5:
    j = 1
    while j <= 10:
        print(j, end = " ")
        j += 1
    i += 1
    print("")
string = input("Enter a string: ")
char = input("Enter letter that you want to find in string: ")
i = 0
count = 0
while i < len(string):
    if string[i] == char:
        count += 1
    i += 1
print(count)