
import numpy as np
import Point as P
import Message as Messager
import time
import datetime 
import matplotlib.pyplot as plt
import Arena as are
import time



class Robot:
    

    def __init__(self,typer,vector_message,battery,id,vector_move,pointer):
       
        
        self.typer=typer
        self.vector_message=vector_message
        self.battery=float(battery)
        self.id=id
        self.vector_move=vector_move
        self.count_message=0
        self.pointer=pointer
        

    def __str__(self):
        return "Typer = " + str(self.typer)   \
        + " , battery =  " + str(self.battery) + " , ide = " + str(self.id)  \
        +  ", count message = " + str(self.count_message) + ", And Point " + str(self.pointer) 
    
    
    
    

        

    
   # def __what_to_do(self):



    def _send_message_(self):
        #current time
         print datetime.datetime.time(datetime.datetime.now())
         Mili = str(datetime.datetime.time(datetime.datetime.now())).split('.')
         mili_res = int(Mili[1])/1000    
         Mili[0] = Mili[0]+":"+str(mili_res)
         current_time = Mili[0]
            
         
         message=Messager.Message(self.battery,self.id,current_time,self.count_message)    
         self.count_message=self.count_message+1;
         
              

    def Recharge(self):
    
    
        while self.battery<=100:
            time.sleep(0.1)
            self.battery+=0.5
            print self.battery
        
        self.battery=100



def main():
     
     
  print('tomer')


     
#main()