current_value = int(input("Enter a number: "))
step_count = 0

def calculate_next_value(value):
    if value % 2 == 0:
        return value // 2
    else:
        return value * 3 + 1

while current_value != 1:
    current_value = calculate_next_value(current_value)
    print(current_value)
    step_count += 1

print(f"Total steps required: {step_count}")