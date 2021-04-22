# mortgage.py
#
# Exercise 1.7
principal = 500000.0
interest_rate = 0.05
monthly_payment = 2684.11
total_amount_paid = 0.0
total_months_paid = 0

while principal > 0:
    if (0 <= total_months_paid < 12) or (60 <= total_months_paid < 108):
        extra_payment = 1000.0
    else:
        extra_payment = 0.0
    principal = principal * (1+interest_rate/12) - monthly_payment - extra_payment
    total_amount_paid = total_amount_paid + monthly_payment + extra_payment
    total_months_paid += 1
    print('monthly payment: {0} extra payment: {1} principal: {2} month: {3}'
          .format(monthly_payment,extra_payment,principal,total_months_paid))
    if principal < monthly_payment:
        monthly_payment = principal * (1+interest_rate/12)
        
print('Total amount paid for the mortgage is {0:0.2f} during a period of {1} months'.format(total_amount_paid,
                                                                                            total_months_paid))

