# Exercise 6.11
# Contains one function computeCommission which computes commission  
# Sawan Srivastava
# 1/13/2020
def computeCommission(salesAmount):
    if 0.01 <= salesAmount <= 5000:
        commissionRate = 0.08
    elif 5000.01 <= salesAmount <= 10000:
        commissionRate = 0.1
    elif salesAmount >= 10000.01:
        commissionRate = 0.12
    Commission = salesAmount * commissionRate
    return str(salesAmount)+'                 '+str(Commission)
def main():
    print('Sales Amount          Commission')
    print(computeCommission(10000))
    print(computeCommission(15000))
    print(computeCommission(20000))
    print(computeCommission(25000))
    print(computeCommission(30000))
    print(computeCommission(35000))
    print(computeCommission(40000))
    print(computeCommission(45000))
    print(computeCommission(50000))
    print(computeCommission(55000))
    print(computeCommission(60000))
    print(computeCommission(65000))
    print(computeCommission(70000))
    print(computeCommission(75000))
    print(computeCommission(80000))
    print(computeCommission(85000))
    print(computeCommission(90000))
    print(computeCommission(95000))
    print(computeCommission(100000))
main()
