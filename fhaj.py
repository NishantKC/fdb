import os 
import shutil
#print(os.system("date"))
#os.mkdir("Hello")
#print(os.getcwd())
#print(os.listdir())
#print(os.path.exists("/users/nishantchinta/desktop/untitled folder 9"))
#print(os.path.splitext("/users/nishantchinta/desktop/untitled folder 8/fjjx.txt")[1])
source=input("enter the source path: ")
destination=input("enter the destination path: ")
source=source+"/"
destination=destination+"/"
files=os.listdir(source)
for i in files:
    shutil.copy((source+i),destination)