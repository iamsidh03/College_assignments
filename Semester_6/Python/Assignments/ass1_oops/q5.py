import re
class Time:
    def __init__(self,time_str):
        self.time_str=time_str
    def validString(self):
        pattern=r'^(?:[01]?[0-9]|2[0-3]):(?:[0-5]?[0-9]):(?:[0-5]?[0-9])$'
        if re.match(pattern,self.time_str):
            return True
        return False
    def convert_to_12hr(self):
        if not self.validString():
            print("String is invalid")
          
        hr,mins,sec=map(int,self.time_str.split(':'))
        if hr==0:
            periods="AM"
            hr=12
        elif hr<12:
            periods="PM"
        elif hr==12:
            periods='PM'
        else:
            periods='PM'
            hr-=12
        return f'{hr}:{mins}:{sec}:{periods}'
time_input=input("Enter time in HH:MM:SS (in 24-hrs format) ")
time_obj=Time(time_intput)
