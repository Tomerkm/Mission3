# -*- coding: utf-8 -*-
"""
Created on Sun May 15 20:12:43 2016

@author: Student
"""
import random
import Point as P

class Message:
    
    """ Point class represents and manipulates x,y coords. """
    def __init__(self,battery,sender_id,time_from_send,message_id):
        """ Create a new point at the origin """
        self.battery = battery
        self.sender_id=sender_id
        self.time_from_send=time_from_send
        self.message_id=message_id
        
    

#    def __get_message__(self):
        #return true   
        #return false
    
#    def __robot_message__(self):
        #return num_of sends

    def __if_can_get_the_message__(self):
        if self.distance>500:
            return False
        if self.distance<50:
            return True
        x=randint(1,100)
        chance=((500-self.distance)/450)*100
        if x<=chance:
               return True
        return False
        
def main():
   
   f = P.Point(1,2)
   print(f)
   f._set_(5,3)
   print(f)

        
        
        
#main()
        