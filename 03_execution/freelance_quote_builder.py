def totalCost(rate:float, hours:float, expenses:float) -> float:
    return rate*hours+expenses

def laborCost(rate:float, hours:float) -> float:
    return rate*hours

def main():
    client_name:str = input("Client Name: ").strip().title()
    hours:float = float(input("Hours Worked: "))
    rate:float = float(input("Hourly Rate: ").strip("$"))
    expenses:float = float(input("Direct Expenses: ").strip("$"))
    labor:float = laborCost(rate, hours)

    total:float = totalCost(rate, hours, expenses)

    print("PROJECT ESTIMATE")
    print(f"Client Name: {client_name}")
    print(f"Labor Cost: ${labor:.2f}")
    print(f"Direct Expenses: ${expenses:.2f}")
    print(f"Total Esitmate: ${total:.2f}")

main()