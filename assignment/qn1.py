count = 0
total = 0

while True:
    try:
        input_value = input("Enter a number: ")
        if input_value.lower() == 'done':
            break
        else:
            number = float(input_value)
            total += number
            count += 1
    except ValueError:
        print("Invalid input")

    else:
        print("ollloooo")

    finally:
        print("bla bla")

if count > 0:
    average = total / count
else:
    average = 0

print(f"Total = {total}, Count = {count} and Average = {average}")
