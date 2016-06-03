# -*- coding: utf-8 -*-
"""
Created on Sun May 15 20:12:43 2016

@author: Student
"""

class Point:
    """ Point class represents and manipulates x,y coords. """


    def __init__(self,x,y):
        """ Create a new point at the origin """
        self.x = x
        self.y = y
    def _set_(self, value_x,value_y):
         self.x= value_x
         self.y= value_y
         
    def get_x(self):
        return self.x
        
    def get_y(self):
        return self.y 

    def Equalser(self,x,y):
        return self.x==x and self.y==y


    def __str__(self):
        return "X = " + str(self.x) + " And Y = " + str(self.y)   
    
                
def main():
   
   f = Point(1,2)
   print(f)
   f._set_(5,3)
   print(f.Equalser(5,3))

        
#main()   
        
#main()
        


         
