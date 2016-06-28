def collatz(number):
    if number % 2 == 0:
        val = number // 2
        print("Even " + str(val))
        return val
    else:
        val = 3 * number + 1
        print("Odd: " + str(val))
        return val

num = int(input("Please enter your number: "))
while num != 1:
    num = collatz(num)