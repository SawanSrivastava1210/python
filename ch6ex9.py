# Exercise 6.9
# Contains two functions footToMeter and meterToFoot 
# Sawan Srivastava
# 1/13/2020
def footToMeter(foot):
    meter = 0.305*foot
    return str(foot)+'          '+str(meter)
def meterToFoot(meter):
    foot = meter/0.305
    return str(meter)+'            '+str(format(foot,".2f"))
def main():
    print('Feet       Meters    |    Meters       Feet')
    print(footToMeter(1),'        ',meterToFoot(20))
    print(footToMeter(2),'         ',meterToFoot(26))
    print(footToMeter(3),'        ',meterToFoot(30))
    print(footToMeter(4),'         ',meterToFoot(36))
    print(footToMeter(5),'        ',meterToFoot(40))
    print(footToMeter(6),'         ',meterToFoot(46))
    print(footToMeter(7),'        ',meterToFoot(50))
    print(footToMeter(8),'         ',meterToFoot(56))
    print(footToMeter(9),'        ',meterToFoot(60))
    print(footToMeter(10),'        ',meterToFoot(66))
main()


