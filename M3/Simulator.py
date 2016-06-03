import numpy as np
import matplotlib.pyplot as plt
import Point as P
import csv
import Robot as rob
import Arena as are
import Air as ai
import os.path
import random




lister_scatter = {}


Robot_Place = {}



def reslut(ID,Typer,Battery,X,Y):
    

    if ID=="" or Typer=="" or Battery=="" or X=="" or Y=="":
        raise ValueError("Error - At Least One Of The Data Is Empty")
        return 0
    try:
        ID = int(ID)
    except Exception:
        raise ValueError("Error - Cannot Convert ID String letters to int number")
        return 0
    try:
       Battery = float(Battery)
    except Exception:
        raise ValueError("Error - Cannot Convert Battery String letters to float number")
        return 0
    try:
       X = int(X)
    except Exception:
         raise ValueError("Error - Cannot Convert X String letters to int number")
         return 0
    try:
       Y = int(Y)
    except Exception:
         raise ValueError("Error - Cannot Convert Y String letters to int number") 
         return 0
    
    
    if ID<0:
        raise ValueError("Error - ID Cannot Be Negative")
        return 0
    if Battery<0 or Battery>100:
        raise ValueError("Error - Battery Range must be between 0-100")
        return 0
    if Typer!="s" and Typer!="d" and Typer!="D" and Typer!="S":
        raise ValueError("Error - Robot Must be Static (S) Or Dynamic (D) ")
        return 0
    if X<=0 or X>=999:
        raise ValueError("Error - X Value must be between 1 and 999")
        return 0
    if Y<=0 or Y>=999:
        raise ValueError("Error - Y Value must be between 1 and 999")
        return 0
    return 1
        

def Check_Id(Arr,Size):
    i=0
    while i<Size:
        j=i+1
        while j<Size:
            if Arr[i]==Arr[j]:
                raise ValueError("Error - There Are A Duplicate Keys")
                return 0
            j+=1
        i+=1
    return 1
    



def csv_shurot(csv_file):
    
    if os.path.isfile(csv_file)==False:
        return -55555
    file = open(csv_file)
    numline = len(file.readlines())
    return numline-1




def Create_ID_PLACE_In_Matrix(csv_file):
        
    ID_Robot_In_Place = np.empty( (1000,1000), dtype=object)
   
    with open(csv_file, 'rb') as csvfile:
       
        reader = csv.DictReader(csvfile)
            
        for row in reader:
            x= int(row["X"])
            y= int(row["Y"])
            ID_Robot_In_Place[y][x]=row["ID"]
            Robot_Place[row["ID"]] = P.Point(x,y)
            if row["Type"].lower() == "s":
                lister_scatter[row["ID"]] = plt.scatter(x, y,s=200,facecolor="red",linewidth='0',marker="D")
            else:
                lister_scatter[row["ID"]] = plt.scatter(x, y,s=200,facecolor="green",linewidth='0',marker="D")

         
    
    return ID_Robot_In_Place



def Create_Robot_Color_In_Matrix(image,csv_file):
        
                
    with open(csv_file, 'rb') as csvfile:
       
        reader = csv.DictReader(csvfile)
            
        for row in reader:
            x= int(row["X"])
            y= int(row["Y"])
            image[y][x]=2
    
    
    i=0
    while i<1000:
        image[i][0]=0
        image[0][i]=0
        image[999][i]=0
        image[i][999]=0        
        
        i+=1

   


class Simulator:
    
          
    def righter(self, event):
        print('Right')

    def lefter(self, event):
        print('Left')

    def uper(self, event):
        print('Up')

    def downer(self, event):
        print('Down')
    
    def __init__(self,csv_file):
        
        
        #------
        count_robots=csv_shurot(csv_file)
        if count_robots==-55555:
            raise ValueError("Error - Source File is Not found!")
            return
        if count_robots<=0:
            raise ValueError("Error - Empty File! (No Rows)")
            return
        
        robotim=self.csv(csv_file) 
        if not robotim:
            return

            
        fig, ax = plt.subplots()
        

        image = np.random.random_integers(0, 2, (1000, 1000))
       

        img_artist=ax.imshow(image, cmap=plt.cm.gray, interpolation='nearest')

      
    
        ID_Robot_In_Place=Create_ID_PLACE_In_Matrix(csv_file)
        Create_Robot_Color_In_Matrix(image,csv_file)
        

        self.arena=are.Arena(robotim,image,ID_Robot_In_Place,lister_scatter,Robot_Place,count_robots)        
        self.air=ai.Air(robotim,count_robots,self.arena)
        self.robots=robotim
        
        
      
        for Robot in robotim.values():
            if Robot.typer=="D" or Robot.typer=="d":
                Robot.pointer._set_(-500,-500) 

        self.plt=plt
        
        
    #def start_game():
        

        
        
  
  




#-=================================================================================

    def csv(self,csv_file):
        
        Empty=[]
        file = open(csv_file)
        numline = len(file.readlines())
        
     
        
        if numline-1<=0:
            raise ValueError("Error - Row size Is Empty ")
            return
            
        
        robots={}
        Check_Col_Line= []
        CheckKey=[i for i in range(numline)]
        
        index=0
        with open(csv_file, 'rb') as csvfile:
            reader = csv.DictReader(csvfile)
            
            for row in reader:
                flag = reslut(row["ID"],row["Type"],row["Battery"],row["X"],row["Y"])
                if flag==0:
                    return Empty
                
                CheckKey[index]=row["ID"]
                Check_Col_Line.append(P.Point(int(row["X"]),int(row["Y"])))
                index+=1
                vector_message = []
                vector_move = []
                robots[row["ID"]] = rob.Robot(row["Type"],vector_message,row["Battery"] ,row["ID"],vector_move,P.Point(int(row["X"]),int(row["Y"])))
            
                #print row
               
        
        
        
        if Check_Id(CheckKey,numline)==0:
            return Empty
            
        i=0
        for Point_Left in Check_Col_Line:
            j=0
    
            for Point_Right in Check_Col_Line:
    
                if i!=j:
                    if Point_Left.Equalser(Point_Right.get_x(),Point_Right.get_y())==True: 
                        raise ValueError("Error - There Are A Duplicate Points")
                        return Empty
                j+=1
            i+=1
            

        return robots

#======================================================================================



#callback = Simulator("Robot.csv")
