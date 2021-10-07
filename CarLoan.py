import math


class CarLoan:

    def __init__(self, custName, loanAmount, intRate, numPayments):
        self.__name = custName
        self.__loanAmount = loanAmount
        self.__intRate = intRate
        self.__numPayments = numPayments
        self.__monthlyPayment = intRate / 12 * self.__loanAmount / (1 - math.pow(1 + intRate / 12, (-1) * self.__numPayments))

    def get_cust_name(self):
        return self.__name

    def get_loan_amount(self):
        return self.__loanAmount

    def get_int_rate(self):
        return self.__intRate

    def get_num_payments(self):
        return self.__numPayments

    def get_monthly_payment(self):
        return self.__monthlyPayment

    def make_a_payment(self):
        intPayment = self.__intRate / 12 * self.__loanAmount

        self.__loanAmount -= self.__monthlyPayment - intPayment
        self.__numPayments -= 1