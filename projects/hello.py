# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 11:32:49 2023

@author: nasta
"""

def main():
    name=input("what is your name?")
    print(hello(name))
    
    
def hello(to="world"):
    return f"hello, {to}"



if __name__ == "__main__":
    main()
