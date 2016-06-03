# -*- coding: utf-8 -*-
"""
Created on Sun May 15 20:01:57 2016

@author: Student
"""

import numpy as np
import Point as P
import random
import matplotlib.pyplot as plt


class Arena:
    

    
    

    def __init__(self,robotim,image,ID_Robot_In_Place,lister_scatter,Robot_Place,count_robots):
        self.robotim=robotim    
        self.image=image
        self.ID_Robot_In_Place=ID_Robot_In_Place
       
        self.Robot_Place=Robot_Place
        self.lister_scatter=lister_scatter
        self.count_robots=count_robots
        
        
    def Get_Robot_Place(self,ID):
        return self.Robot_Place[ID]
   
    
    def Move_Robot(self,ID,side):
        
        
        if self.robotim[ID].battery<3:
            print "Not Enough Battery To The Robot"
            return
        
        if self.robotim[ID].typer=="S" or self.robotim[ID].typer=="s":
            print "Static Robot Cannot Move "
            return
                    
         
        Pointer = self.Get_Robot_Place(ID)
        
        x=Pointer.get_x()
        y=Pointer.get_y()

        if side=="up":
            y+=1
        elif side=="down":
            y-=1
        elif side=="right":
            x+=1
        else:
            x-=1
           
        
        if self.image[y][x]==0:
            print("Robot Cannot Move To a wall (Black)")
        elif self.ID_Robot_In_Place[y][x]!=None:
            print("There Is a robot in a Specefic Place")
        else:
            self.robotim[ID].battery-=2 #lose battery for every active
            x_prev= self.Robot_Place[ID].get_x()
            y_prev= self.Robot_Place[ID].get_y()
            
            temp = self.ID_Robot_In_Place[y][x]
            
            self.ID_Robot_In_Place[y][x] = self.ID_Robot_In_Place[y_prev][x_prev] 
            self.ID_Robot_In_Place[y_prev][x_prev]  = temp
                        
            
            self.lister_scatter[ID].remove()
            self.Robot_Place[ID]._set_(x,y)
            
            
            
            self.lister_scatter[ID] = plt.scatter(x, y,s=200,facecolor="green",linewidth='0',marker="D")
            self.robotim[ID].vector_move.append(P.Point(x,y))

                
    
    
    def Get_All_Points(self,ID):
        
        str_res = ""
        for Robot in self.robotim[ID].vector_move:
           
            str_res = str_res + str(Robot)  + " , " 
        
        return str_res
     
        
            
            
        
    
    def Get_Neightbors(self,ID):
        
        
        Pointer =self.Get_Robot_Place(ID)
        
        
        x_min = Pointer.x-1
        x_max = Pointer.x+1
        y_min = Pointer.y-1
        y_max = Pointer.y+1
        
        
        if x_min<=0:
            x_min+=1
        if x_max>=999:
            x_max-=1
        if y_min<=0:
            y_min+=1
        if y_max>=999:
            y_max-=1
 
        Robot_Neighbors = []
        i=y_min
       
        while i<=y_max:
            j=x_min
            while j<=x_max:
               
                if Pointer.Equalser(i,j)==False:
                    if self.ID_Robot_In_Place[j][i]!=None:
                        Robot_Neighbors.append( self.robotim[self.ID_Robot_In_Place[j][i]])
                
                j+=1
            i+=1
       
        #for Robot in Robot_Neighbors:
         #   print Robot
        str_res = ""
        for Robot in Robot_Neighbors:
            str_res = str_res  +str(Robot)
            
        return str_res
      
def main():
    
    print("tomer")
        
        
#main()
       
        
        