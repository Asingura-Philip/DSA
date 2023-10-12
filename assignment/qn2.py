while True:
    client_name = input("Enter Client name: ")
    if client_name.lower() == "done":
        break

    try:
        loan_amount = float(input("Enter amount of loan: "))
        days = int(input("Enter days taken with the loan: "))

        interest_rate = 0.10  # 10% interest
        fine_rate = 0.01  # 1% fine per day for overdue payment

        total_amount = loan_amount + (loan_amount * interest_rate)
        if days > 30:
            extra_days = days - 30
            fine = loan_amount * fine_rate * extra_days
            total_amount += fine

        print(f"Total amount from {client_name} is: {total_amount:.2f}.")

    except ValueError:
        print("Invalid input. Please enter numeric values for loan amount and days.")
