iDeposit = 0
fInterest = 0
iMonths = 0
iGoal = 0

# Input Validation for iDeposit
while iDeposit <= 0:
    try:
        iDeposit = int(input("What is the Original Deposit (positive value): "))
        if iDeposit <= 0:
            print("Input must be a positive numeric value.")
    except ValueError:
        print("Input must be a positive numeric value.")

# Input Validation for fInterest
while fInterest <= 0:
    try:
        fInterest = float(input("What is the Interest Rate (positive value): "))
        if fInterest <= 0:
            print("Input must be a positive numeric value.")
    except ValueError:
        print("Input must be a positive numeric value.")

# Input Validation for iMonths
while iMonths <= 0:
    try:
        iMonths = int(input("What is the Number of Months (positive value): "))
        if iMonths <= 0:
            print("Input must be a positive numeric value.")
    except ValueError:
        print("Input must be a positive numeric value.")

# Input Validation for iGoal
while iGoal <= 0:
    try:
        iGoal = int(input("What is the Goal Amount (can enter 0 but not negative): "))
        if iGoal < 0:
            print("Input must be 0 or greater.")
    except ValueError:
        print("Input must be a positive numeric value.")
    
# Convert interest rate percentage to decimal and calculate monthly interest rate
fInterest = fInterest / 100
fMonthlyInterest = fInterest / 12

accountBalance = iDeposit
month = 1
estimated_months = 0

# Calculate balance until goal is reached or months are exceeded
while month <= iMonths and (iGoal == 0 or accountBalance < iGoal):
    fInterestEarned = accountBalance * fMonthlyInterest
    accountBalance += fInterestEarned
    print(f"Month {month}: Account Balance is $ {accountBalance:.2f}")
    month += 1
    estimated_months += 1

# Goal Prediction Loop
nMonthsToReachGoal = 0
nSavingsAccountBalance = iDeposit

# Goal Prediction Loop (No outputs at this point)
while nSavingsAccountBalance < iGoal:
    nMonthlyInterest = nSavingsAccountBalance * fMonthlyInterest
    nSavingsAccountBalance += nMonthlyInterest
    nMonthsToReachGoal += 1

# Output Results
if iGoal > 0:
    print(f"It will take {nMonthsToReachGoal:,} months to reach your ${iGoal:,.2f} goal.")
