# Exercise 9.2
# Creates an investment calculator with GUI
# Sawan Srivastava
# 1/18/2020
from tkinter import *
class InvestmentCalculator:
    def __init__(self):
        window = Tk() # Create a window
        window.title('Investment Calculator') # Set title      
        Label(window, text = 'Investment Amount').grid(row = 1, column = 1, sticky = W)
        Label(window, text = 'Years').grid(row = 2, column = 1, sticky = W)
        Label(window, text = 'Annual Interest Rate').grid(row = 3, column = 1, sticky = W)
        Label(window, text = 'Future Value').grid(row = 4, column = 1, sticky = W)
        self.InvestmentAmountVar = StringVar()      
        Entry(window, textvariable = self.InvestmentAmountVar, justify = RIGHT).grid(row = 1, column = 2)
        self.numberOfYearsVar = StringVar()       
        Entry(window, textvariable = self.numberOfYearsVar, justify = RIGHT).grid(row = 2, column = 2)
        self.InterestRateVar = StringVar()       
        Entry(window, textvariable = self.InterestRateVar, justify = RIGHT).grid(row = 3, column = 2)
        self.FutureValueVar = StringVar()
        lblFutureValue = Label(window, textvariable = self.FutureValueVar).grid(row = 4, column = 2, sticky = E)        
        btComputeInvestment = Button(window, text = 'Calculate', command = self.computeInvestment).grid(row = 5, column = 2, sticky = E)          
        window.mainloop() 
    def computeInvestment(self):  
        FutureValueVar = float(self.InvestmentAmountVar.get()) * (1+(float(self.InterestRateVar.get())/1200))**(float(self.numberOfYearsVar.get())*12)
        self.FutureValueVar.set(format(FutureValueVar, ".2f"))     
        return FutureValueVar
InvestmentCalculator()
       
