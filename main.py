import CarLoan


def main():

    # Empty list to store CarLoan objects
    loanList = []

    while True:
        customerName = input("Enter name of the customer (or q to quit): ")

        # Exit loop if user input is q or Q
        if customerName == 'q' or customerName == 'Q':
            print("Done creating customer loans.\n\n")
            break

        # Ask for user input
        initLoan = input("Enter the initial car loan amount: ")
        intRate = input("Enter the annual interest rate in decimal: ")
        numPayments = input("Enter the total number of monthly payments: ")

        # Create CarLoan object and store it in variable loan
        loan = CarLoan.CarLoan(customerName, float(initLoan), float(intRate), int(numPayments))

        # Print out loan information
        print("A new instance of CarLoan is created")
        print(f"The total loan amount is: {loan.get_loan_amount()}")
        print(f"The annual interest rate is: {loan.get_int_rate()}")
        print(f"The monthly payment is: {loan.get_monthly_payment():.2f}\n")

        # Append loan variable to loan list
        loanList.append(loan)

    # Ask for customer name to check it
    custName = input("Enter name of the customer you want to check: ")

    while True:
        found = False

        # Loop through the loan list
        for loan in loanList:

            # If customer's name is found ask for number of payments
            if loan.get_cust_name() == custName:
                makePayment = int(input("Enter the number of payments made so far: "))

                # Continue asking for payment while input is invalid
                while makePayment > loan.get_num_payments():
                    makePayment = int(input("Invalid number of payments. Try again: "))

                # Call make_a_payment() the number of times makePayment's value is
                for i in range(makePayment):
                    loan.make_a_payment()

                # Print out remaining loan and remaining payments
                print(f"After {makePayment} payment(s):")
                print(f"The remaining loan balance is: {loan.get_loan_amount():.2f}")
                print(f"The number of remaining payments: {loan.get_num_payments()}")

                # Set found to True to exit loop
                found = True

        # If customer is found break out of the loop, else continue asking for customer's name
        if found:
            break
        else:
            custName = input("The customer is not found. Try again: ")


if __name__ == '__main__':
    main()
