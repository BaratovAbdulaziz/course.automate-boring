number = int(input("Enter a number: "))
steps = 0
def main(number):
    if number % 2 == 0:
        return number //  2
        
    else:
        return number * 3 + 1;
while number != 1:
    number= main(number)
    print(number)
    steps += 1
print(f"total steps required: {steps}") 