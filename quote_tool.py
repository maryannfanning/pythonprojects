# -*- coding: utf-8 -*-
"""
Created on Sun Apr 05 16:09:07 2015

@author: MaryAnn
"""

PRICELIST = { "widget": 1, "whatzit": 2, "fizz": 3, "wotsit": 4, "buzz": 5 }
SUPPORTLIST = {"bronze": 1, "silver": 2, "gold": 3}



class Quote:
    def _init_(self, products, prices, support, support_prices, duration, special_terms):
        '''initiates class with blank product, pricing, and support information but 
        but establishes defaults'''
        self.products = products
        self.prices = prices
        self.support = support
        self.support_prices = support_prices
        self.duration = duration
        self.special_terms = special_terms

        
    def add_product(self, input):
        '''adds items from the global PRICELIST to the products list, and adds their 
        prices to the prices list'''
        global PRICELIST
        self.products.append(input)
        self.prices.append(PRICELIST[input])
        return self.products, self.prices
        
    def add_support(self, input):
        '''selects item from the global SUPPORTLIST for support and identifies 
        their price'''
        global SUPPORTLIST
        self.support = input
        self.support_prices = SUPPORTLIST[input] 
        return self.support, self.support_prices 
        
    def change_duration(self, years):
        '''change the duration from the default at 1 to another number of years'''
        if years <= 3:
            self.duration = years 
            return self.duration
        elif years > 3:
            print "Error: Max duration is 3"
        elif years < 1:
            print "Error: Minimum duration is 1"

    def print_products(self):
        print self.products, self.prices
        
    def print_support(self):
        print self.support, self.support_prices 
        
    def print_duration(self):
        print self.duration 

new_quote = Quote()
new_quote.change_duration(1)
new_quote.print_duration()