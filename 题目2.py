# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 21:06:38 2020

@author: 1002
"""

class Item(object):
    def __init__(self,amount,name):
        self.name = name
        self.amount = amount
        self.historyList = [amount]
        
    def buy(self, number):
        self.amount += number
        self.historyList.append(self.amount)

    def sell(self, number):
        self.amount -= number
        self.historyList.append(self.amount)
        
    def getName(self):
        return self.name
        
    def getAmount(self):
        return self.amount
        
    def getHistory(self):
        return (self.historyList)        
        
    def __str__(self):
        return "There are {0} {1}s available.".format(self.amount, self.name)

class NewBook(Item):
    def __init__(self,amount):
        
        #Item.__init__(self,amount,name = "new book")
        super(NewBook, self).__init__(amount,name = "new book")
        
    def buy(self):
        Item.buy(self, number=10)
    
    def sell(self):
        Item.sell(self, number=1)
 
if __name__ == "__main__":
    """
    Test your code here
    
    """
    B = NewBook(20)
    
    B.sell()
    B.sell()
    
    B.buy()
    print(B)
    print("History is: " + str(B.getHistory()))
    
    