# Engineering Design

**Team members:**

Jonathon Thompson
Damon Myers

Plan how your code will meet the product requirements. Keep answers brief.

## Inputs

*List each input and its Python data type.*
client_name: string
labor_hours: float
expenses: float

## Processing

*What calculations, text clean up, numeric converstions, ext will the program perform on the inputs?*
The equation `rate*hours+expenses` to get total cost
Stripping unnecessary trailing and tailing whitespaces using the `strip()` method and formatting it with the `title()` method

## Output

*What will the program display? How will you format it?*
PROJECT ESTIMATE
Client: client_name
Labor cost: labor_cost
Direct expenses: direct_expenses
Total estimate: final_cost

## Functions

*Describe `main()` and at least one calculation function. For each, give its name, purpose, parameters, and returned result (or none).*
