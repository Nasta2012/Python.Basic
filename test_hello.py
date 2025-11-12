# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 11:43:55 2023

@author: nasta
"""

from hello import hello 

def main():
    test_hello()
    

def test_hello():
    try:
        assert hello()=="hello, world"
    except AssertionError:
        print("wronge")
    try:
        assert hello(David)=="hello, David"
    except AssertionError:
        print("wronge2")
        
    
if __name__ == "__main__":
    main()



    




