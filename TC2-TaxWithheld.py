"""Student Name:krishna Priyanka Garikapati
Student No:W0502117
Techcheck#2"""
# Tax Withheld Calculator

# Write a console program that calculates the total amount of tax withheld from an employee’s weekly salary.
# The total withheld tax amount is calculated by combining the amount of provincial tax withheld and the amount of 
# federal tax withheld, minus a per-dependent deduction from the total tax withheld. The user will enter their pre-tax 
# weekly salary amount and the number of dependents they wish to claim. 
# 
# The program will calculate and output the amount of provincial tax withheld, amount of federal tax withheld, the 
# dependent tax deduction, and the user’s final take-home amount.
# Provincial withholding tax is calculated at 6.0%. Federal withholding tax is calculated at 25.0%. 
# The tax deduction for dependents is calculated at 2.0% of the employee’s salary per dependent.

def main():
  #TotalWithheldTax=ProvincialTaxWithheld + FederalTaxWithheld-per dependendent tax deduction
  #TotalTakehome=totalweeklysalary-TotalWithheldTax
  
  #Input variable
 WeeklySalary=float(input("Please enter full amount of your weekly salary:"))
 Dependents=int(input("How many dependents do you have?:"))
   

  #Withheld taxs calculations
 ProvincialTaxWithheld=0.06*WeeklySalary
 print("\nProvincial Tax Withheld: ${0:.2f}".format(ProvincialTaxWithheld))
 FederalTaxWithheld=0.25*WeeklySalary
 print("Federal Tax Withheld: ${0:.2f}".format(FederalTaxWithheld))
 DependentDeduction=0.02*Dependents*WeeklySalary
 print("Dependent deduction for",Dependents, "dependents: ${0:.2f}".format(DependentDeduction))
  

  #Total takehome calculation
 TotalWithheld=ProvincialTaxWithheld+FederalTaxWithheld-DependentDeduction
 print("Total Withheld: ${0:.2f}".format(TotalWithheld))
 TotalTakeome=WeeklySalary-TotalWithheld
 print("Total Take-Home Pay: ${0:.2f}".format(TotalTakeome))
main()
