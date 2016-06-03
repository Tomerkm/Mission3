# -*- coding: utf-8 -*-
"""
Created on Sun May 15 20:12:43 2016

@author: Student
"""
import Message as mes 
import math
import Point as P
import Arena as Aren

class Air:
    """ Point class represents and manipulates x,y coords. """

    def __init__(self,Roboter,count_robots,arena):
        self.count_robots=count_robots
        self.Roboter=Roboter
        self.arena=arena


    def distance(self,p1,p2):
        f=(p1.x-p2.x)*(p1.x-p2.x) + (p1.y-p2.y)*(p1.y-p2.y)  
        distance_=math.sqrt(f)
        return distance_
    

    def Send_Message(self,Robot_ID,Message_To_Send):
        
        position_Point = arena.Get_Robot_Place(Robot_ID)
        
        print("tomer")
                
def main():
    print("TOMER")
    p1 = P.Point(1,2)
    p2 = P.Point(3,0)
    s = Air(2)

    print s.distance(p1,p2)    
        
        
#main()
        


         
