# Imports
from datetime import datetime
import time
import os

# Class
class Clock():
    def __init__(self):
        self.Alarm_List = {}
        self.now = 0
        self.current_time = 0

    def Current_Time_Update(self):
        
        self.now = datetime.now()
        self.current_time = self.now.strftime("%H:%M")
        return self.current_time

    def add_alarm(self):
        
        self.Alarm_Name = input("please enter name for alarm: ")
        self.Alarm_Time = input("Please enter Time for Alarm as HH:MM")
        print("Alarm name is: "+ self.Alarm_Name)
        if self.Alarm_Name in self.Alarm_List:
            print ("Name Alrady Exits")
            self.add_alarm()
        else:
            self.Alarm_List[self.Alarm_Name] = {self.Alarm_Time}
            
    def Set_Alarm(self): 
        print(self.Alarm_List)
        Choice = input("Please input the name of the alarm to set or Q to quit: ")
        if Choice in self.Alarm_List:
            print("Alarm Set")
        elif Choice == "Q":
            self.Menu()
        else:
            print("No alarm with this name")
            self.Set_Alarm()

        
        while True:
            if self.Alarm_List[Choice] != str("{"+"'"+self.Current_Time_Update()+"'"+"}"):  
                time.sleep(1)
                print("Current Time" "{"+"'"+self.Current_Time_Update()+"'"+"}")
                print(str("Alarm Time" self.Alarm_List[Choice]))
            elif str(self.Alarm_List[Choice]) == str("{"+"'"+self.Current_Time_Update()+"'"+"}") :
                
                print("Alarm!!!!!! " + self.Alarm_Name + " " + self.Alarm_Time)
                break
            
                

    def Remove_Alarm(self):
        
        print(self.Alarm_List)
        Choice = input("Please Input Name of Alarm to remove: ")
        for x in self.Alarm_List:
            if str(x) == str(Choice):
                del self.Alarm_List[Choice]
                print("Alarm Removed")
                print("Alarm List " + str(self.Alarm_List))
                break
            else:
                print("No alarm by That name Exists")

    def Menu(self):
        os.system('cls')
        print("Please Choose Option:")
        print(" 1.Current Time""\n 2.Add Alarm""\n 3.Remove Alarm""\n 4.Alarm List""\n 5.Set Alarms""\n 6.Quit")
        Choice = input()
        if Choice == "1":
            print("Current Time is: "+ str(self.Current_Time_Update()))
        elif Choice == "2":
            self.add_alarm()
        elif Choice == "3":
            self.Remove_Alarm()
        elif Choice == "4":
            print(self.Alarm_List)
        elif Choice == "5":
            self.Set_Alarm()
        elif Choice == "6":
            quit()
        else:
            "Not a Valid Selection"
        input("Press Any key to Continue")
        self.Menu()

# Call Stack
Alarm_Clock = Clock()
Alarm_Clock.Menu()

