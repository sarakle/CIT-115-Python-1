def getFloatInput(prompt): # This keeps prompting the user until they have entered a proper input
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
        except ValueError:
            print("Enter a number greater than 0.")

def getMedian(values): # Calculates the median of a list for the numerical values
    values.sort()
    n = len(values)
    if n % 2 == 0:
        return (values[n // 2 - 1] + values[n // 2]) / 2
    else:
        return values[n // 2]

def main(): # Gathers property sales values an calculates the statistics
    sales_values = [] 
    while True:
        fSalesPrice = getFloatInput("Enter property sales value: ")
        sales_values.append(fSalesPrice)  # Add the inputted value to the list


        while True:
            another_value = input("Enter another value (Y or N): ")
            if another_value == 'N':
                break
            elif another_value == 'Y':
                break
            else:
                pass # Continues the loop until the user inputs the correct value
        
        if another_value == 'N':  # Exit the main loop if the user says "N"
            break

    if sales_values:
        # Sort the list for output and median calculation
        sales_values.sort()

        print("Sorted Sales Values:")
        # Displaying each value with "Property" labels
        for i, value in enumerate(sales_values, start=1):
            print(f"Property {i}: ${value:,.2f}")

        # Displays statistics of inputted values
        print(f"Minimum: ${min(sales_values):,.2f}")
        print(f"Maximum: ${max(sales_values):,.2f}")
        print(f"Total: ${sum(sales_values):,.2f}")
        print(f"Average: ${sum(sales_values) / len(sales_values):,.2f}")
        print(f"Median: ${getMedian(sales_values):,.2f}")
        print(f"Commission: ${sum(sales_values) * 0.03:,.2f}")

if __name__ == "__main__":
    main()
