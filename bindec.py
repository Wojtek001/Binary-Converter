
print ("Welcome to the binary converter program")
print("Type your number and number\'s type (2 or 10) after one space: ")

two_or_ten = ['2', '10']
number, decorbin = input().split()

while decorbin not in two_or_ten:
    print ('Invalid number\'s type!')
    decorbin = input("Enter correct number\'s type: ")

if decorbin == "10":
    number = int(number)
    result = ''
    for x in range(16):
        r = number % 2
        number = number//2
        result += str(r)
    result = result[::-1]
    print(result, 2)

elif decorbin == "2":
    result = 0
    for digit in number:
        result = result*2 + int(digit)
    print(result, 10)