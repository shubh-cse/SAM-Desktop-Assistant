#importing libraries
from datetime import datetime
from os import system
import numpy as np
import matplotlib.pyplot as plt

#greeting message
print("Hi !!")

#looping to run the code again and again until it meets boundary condition
while(True):

    #taking user's command
    command = input("How may I help you ?? \n").lower()

    #if user want to know about the Desktop Assistant
    if(("who" in command) or ("you" in command) or ("yourself" in command)):
        print("My name is SAM :)")
        print("Version 2.0")
        continue

    #elif user don't want to run anything
    elif(("don't" in command) or ("not" in command) or ("did't" in command) or ("dont" in command) or ("didnt" in command)):
        #continue with the next iteration
        continue

    #if user want to know the current time
    elif(("time" in command) or ("timings" in command)):
        print(datetime.now().strftime("%H:%M:%S"))
        continue

    #if user want to stop the SAM
    elif(("stop" in command) or ("shutdown" in command) or ("shut" in command) or ("down" in command) or ("sleep" in command)):
        #boundary condition
        break

    #if user want to open the editor 
    elif(("editor" in command) or ("notepad" in command)):
         system("start notepad")
         continue

    #if user want to search something
    elif(("search" in command) or ("searching" in command) or ("chrome" in command) or ("engine" in command) or ("google" in command)):
        system("start chrome")
        continue

    #if user want to listen a song or watch a video
    elif(("youtube" in command) or ("tube" in command) or ("song" in command) or ("video" in command) or ("movie" in command) or ("film" in command)):
        system("start chrome youtube.com")
        continue

    #if user want too see its linkedin account
    elif(("linkedin" in command) or ("linked" in command)):
        system("start chrome linkedin.com/in/shubh-cse")
        continue

    #if user want to search for jobs
    elif(("jobs" in command) or ("jobs" in command) or ("intern" in command) or ("internship" in command)):
        system("start chrome linkedin.com/jobs")
        continue

    #if user want to do some calculation
    elif(("calculator" in command) or ("calculations" in command) or ("calculator" in command) or ("calculate" in command)):
        cal = input("Which operation you want to perform ?\n")
        n = int(input("Give the first number\n"))
        m = int(input("Give the second number\n"))
        if(("sum" in cal) or ("add" in cal) or ("addition" in cal)):
            print(n+m)
        elif(("subtarct" in cal) or ("sub" in cal) or ("minus" in cal) or ("subtraction" in cal)):
            print(n-m)
        elif(("div" in cal) or ("divide" in cal) or ("division" in cal)):
            print(n/m)
        elif(("prod" in cal) or ("mul" in cal) or ("multiplication" in cal) or ("product" in cal) or ("multiply" in cal)):
            print(n*m)
        else:
            print("Please enter correct mathematical operation !!")
        continue

    #if user want to purchase something online
    elif(("shop" in command) or ("shopping" in command) or ("purchase" in command) or ("purchasing" in command)):
        shop = input("Where you want to shop online - Amazon or Flipkart ?\n").lower()
        if("amazon" in shop):
            system("start chrome amazon.in")
        elif("flipkart" in shop):
            system("start chrome flipkart.com")
        else:
            print("Please select from Amazon or Flipkart !!")
        continue

    #if user want to plot sine graph
    elif(("sin" in command) or ("sine" in command)):
        a = float(input("Give the starting range : \n"))
        b = float(input("Give the ending range : \n"))
        num =float(input("Give the value for jump : \n"))
        x = np.arange(a,b,num)
        y = np.sin(x)
        plt.plot(x,y)
        plt.title("Sine Graph")
        plt.xlabel("x-axis")
        plt.ylabel("y-axis")
        plt.show()
        continue

    #if user want to plot cosine graph
    elif(("cos" in command) or ("cosine" in command)):
        a = float(input("Give the starting range : \n"))
        b = float(input("Give the ending range : \n"))
        num =float(input("Give the value for jump : \n"))
        x = np.arange(a,b,num)
        y = np.cos(x)
        plt.plot(x,y)
        plt.title("Cosine Graph")
        plt.xlabel("x-axis")
        plt.ylabel("y-axis")
        plt.show()
        continue

    #if user give the instruction that is not supported by the SAM
    else:
        print("SAM don't support this !!")
        continue

#SAM will give a thank you message to the user before sleeping
print("Thank you for using me.\nHave a nice day.")

    
        
        
    
        
    
    
    
