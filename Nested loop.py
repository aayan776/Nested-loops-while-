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
lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))
print("The prime numbers between", lower, "and", upper, "are: ")
for num in range(lower, upper + 1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)
num2 = int(input("Enter number: "))
t = num2
numLen = 0
while t > 0:
    numLen += 1
    t = int(t / 10)
if numLen > 4:
    numLen = int(numLen / 2)
    chk = 0
    while num2 > 0:
        rem = (num2 % 10)
        if chk == numLen:
            MidOne = rem
        elif chk == (numLen - 1):
            MidTwo = rem
        num2 = int(num2 / 10)
        chk = chk + 1
    product = MidOne * MidTwo
    print(product)
else:
    print("It is not more than a 4 digit number")
