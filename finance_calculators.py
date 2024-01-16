import math
# Start
print("Investment - to calculate the amount of interest you'll earn \
on your investment")
print("Bond - to calculate the amount you'll have to pay on a home loan")
decision1 = input("Enter [I]nvestment or [B]ond from Menu: ")
# containers
B = "b"
I = "i"
SI = "s"
CI = "c"
# investment route
if decision1 == I:
    print("investment selected")
    decision_investment1 = float(input("Enter how much money will you be \
depositing: "))
    decision_investment2 = float(input("Enter the applicable interest \
rate: "))
    decision_investment3 = int(input("Enter how many years will you be \
investing for: "))
    decision_investment4 = input("Enter [S]imple interest or [C]ompound \
interest:")
    deposit = float(decision_investment1)
    rate = int(decision_investment2)
    time = int(decision_investment3)
    r = rate/100 # variables for interest
    P = deposit
    t = time
    simple_interest = P *(1 + r*t)
    compound_interest = P * math.pow((1 + r),t)
    if decision_investment4.lower() == SI:
        print(simple_interest)
    elif decision_investment4 == CI.lower():
        print(compound_interest)
# bond route
if decision1 == B: 
    print("bond selected")
    decision_bond1 = input("Enter the present value of the house: ")
    float(decision_bond1)
    decision_bond2 = input("Enter the applicable interest rate: ")
    float(decision_bond2)
    decision_bond3 = input("Enter the number of months you plan to repay: ")
    int(decision_bond3)
    house_value = float(decision_bond1)
    monthly_rate = float(decision_bond2)
    time = int(decision_bond3)
    P = house_value # variables for bond
    rate = monthly_rate/100
    i = rate/12
    n = time
    repayment = (i * P)/(1-(1 + i)**(-n))
    print(repayment)
# End