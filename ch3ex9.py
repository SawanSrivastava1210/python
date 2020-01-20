# Exercise 3.9
# reads employee name, hours worked, hourly pay rate, Federal tax rate, and State tax rate and prints out the payroll
# Sawan Srivastava
# 1/6/2020
Name = input('Enter Employee\'s NSaame: ')
Hours = eval(input('Enter number of hours worked in a week: '))
PayRate = eval(input('Enter hourly pay rate: '))
FedTax = eval(input('Enter federal tax withholding rate: '))
StateTax = eval(input('Enter state tax withholding rate: '))
GrossPay = Hours*PayRate
FedTaxTotal = GrossPay*FedTax
StateTaxTotal = GrossPay*StateTax
TaxTotal = FedTaxTotal+StateTaxTotal
NetPay = GrossPay-TaxTotal
print('')
print('Employee Name: ',Name)
print('Hours Worked: ', Hours)
print('Pay Rate: $', PayRate)
print('Gross Pay: $', GrossPay)
print('Deductions:')
print('  Federal Withholding(',FedTax*100,'%): $', FedTaxTotal)
print('  State Withholding(',StateTax*100,'%): $', StateTaxTotal)
print('  Total Deduction: $', TaxTotal)
print('Net Pay: $',NetPay)



