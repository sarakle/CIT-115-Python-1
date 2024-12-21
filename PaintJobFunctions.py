import math

# Gets a valid non-zero float from the user.
def getFloatInput(prompt):

  while True:
    try:
      user_input = float(input(prompt))
      if user_input > 0:
        return user_input
      else:
        print("Please enter a positive non-zero number.")
    except ValueError:
      print("Invalid input. Please enter a number.")

# Calculates the number of gallons of paint needed.
def getGallonsOfPaint(square_feet, feet_per_gallon):

  gallons_needed = math.ceil(square_feet / feet_per_gallon)
  return gallons_needed

# Calculates the labor hours to paint the wall.
def getLaborHours(gallons_needed, labor_hours_per_gallon):

  labor_hours = gallons_needed * labor_hours_per_gallon
  return labor_hours

# Calculates the labor cost to paint the wall.
def getLaborCost(labor_hours, labor_charge_per_hour):

  labor_cost = labor_hours * labor_charge_per_hour
  return labor_cost

# Calculates the paint cost.
def getPaintCost(gallons_needed, paint_price):

  paint_cost = gallons_needed * paint_price
  return paint_cost

# Returns the sales tax rate for the given state.
def getSalesTax(state):

    if state == "CT":
        return 0.06
    elif state == "MA":
        return 0.0625
    elif state == "ME":
        return 0.085
    elif state == "NH":
        return 0.0
    elif state == "RI":
        return 0.07
    elif state == "VT":
        return 0.06
    else:
        return 0.0

def showCostEstimate(square_feet, paint_price, feet_per_gallon, labor_hours_per_gallon, labor_charge_per_hour, state, last_name):
# Calculates and displays the cost estimate.

  gallons_needed = getGallonsOfPaint(square_feet, feet_per_gallon)
  labor_hours = getLaborHours(gallons_needed, labor_hours_per_gallon)
  labor_cost = getLaborCost(labor_hours, labor_charge_per_hour)
  paint_cost = getPaintCost(gallons_needed, paint_price)
  sales_tax = getSalesTax(state)
  total_cost = paint_cost + labor_cost + (paint_cost + labor_cost) * sales_tax

  print(f"Gallons of Paint: {gallons_needed}")
  print(f"Hours of Labor: {labor_hours:.2f}")
  print(f"Labor Charges: ${labor_cost:,.2f}")
  print(f"Paint Charges: ${paint_cost:,.2f}")
  print(f"Tax: ${((paint_cost + labor_cost) * sales_tax):,.2f}")
  print(f"Total Cost: ${total_cost:,.2f}")

def main():
  # Get user inputs
  square_feet = getFloatInput("Enter wall space in square feet: ")
  paint_price = getFloatInput("Enter paint price per gallon: ")
  feet_per_gallon = getFloatInput("Enter feet per gallon: ")
  labor_hours_per_gallon = getFloatInput("Enter labor hours per gallon: ")
  labor_charge_per_hour = getFloatInput("Enter labor charge per hour: ")

  # Get state input
  state = input("Enter the state for the job: ")

  # Get last name
  last_name = input("Customer's Last Name: ")

  # Calculate and display cost estimate
  showCostEstimate(square_feet, paint_price, feet_per_gallon, labor_hours_per_gallon, labor_charge_per_hour, state, last_name)

  print(f"File: {last_name}_PaintJobOutput.txt was created.")

main()

