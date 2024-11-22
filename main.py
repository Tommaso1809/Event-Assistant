#How to use:
# 1. Install pywhatkit using pip install pywhatkit
# 2. Insert your number and message in the Event class
# 3. Run the script and it will send the message to the number at the specified time
# 4. You can add more events by adding more objects to the list_events list


import pywhatkit as pwk
import datetime


class Event :

    def __init__(self,date,number):
        self.date=date
        self.number=number
    
    def set_date(self,date):
        self.date=date
    
    def get_date(self):
        return self.date
    
    def set_number(self,number):
        self.number=number
    
    def get_number(self):
        return self.number

list_events=[]

# Add your events here
list_events.append(Event("22-11","+391234567890")) # +391234567890 is the number to send the message to

def sendMessage(number):

    # Message to be sent
    message = "Insert your message here" 
    pwk.sendwhatmsg_instantly(number, message, 18, 30)
    print("Message Delivered")


x = datetime.datetime.now()
datenow=x.strftime("%d") +"-"+ x.strftime("%m")

today=False

for obj in list_events:

    if obj.get_date() == datenow :
        sendMessage(obj.get_number())
        today=True
        break


if not today:
    print("No Event Today")

