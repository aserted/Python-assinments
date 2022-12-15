a = float(input("Gross income in usd:"))
b = float(input("No of dependents:"))
Tax = (a - 10000 - 3000*b)*20/100
print ("income tax: %f" %Tax)
