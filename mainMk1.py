import time
import webbrowser
import tkinter as tk
import smtplib, ssl
import sys

#Init
#basic varibles
future = 1
x=0
now=0


#finds Chrome and gets it ready#
webbrowser.register('chrome',
    None,
    webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))


#timeout plan
def Timeout():
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "JasonTheHelper@gmail.com"  # Enter your address
    receiver_email = "5413404251@vtext.com"  # Enter receiver address
    password = "Revier917"

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
    print("No response, sending timeout message")


#Go to site
def Meet0():
    webbrowser.get('chrome').open('https://meet.google.com/lookup/hwivvebpw7')
    print("Sent")
    x = 1

#make the GUI function for Sending to class#
def GUI():
    class Application(tk.Frame):
        def __init__(self, master=None):
            super().__init__(master)
            self.master = master
            self.pack()
            self.create_widgets()

        def create_widgets(self):
            self.hi_there = tk.Button(self)
            self.hi_there["text"] = "ELC is soon, would you like to go?"
            self.hi_there["command"] = self.say_hi
            self.hi_there.pack(side="top")

            self.quit = tk.Button(self, text="No", fg="red",
                                  command=self.master.destroy)
            self.quit.pack(side="bottom")

        def say_hi(self):
            print("Sending to class...")
            Meet0()


    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()

#check program with GUI
def CheckGUI():
    class Application(tk.Frame):
        def __init__(self, master=None):
            super().__init__(master)
            self.master = master
            self.pack()
            self.create_widgets()

        def create_widgets(self):
            self.hi_there = tk.Button(self)
            self.hi_there["text"] = "Confirm"
            self.hi_there["command"] = self.say_hi
            self.hi_there.pack(side="top")

            self.quit = tk.Button(self, text="Fine", fg="red",
                                  command=self.master.destroy)

            self.quit.pack(side="bottom")

        def say_hi(self):
            print("Thank you")

#Confirm program is running
message = """\
Confirming program is running"""
Timeout()




#End Result
while True:
    # finds current time
    result = time.localtime()
    print("result:", result)
    print("\nyear:", result.tm_year)
    print("tm_hour:", result.tm_hour)
    print("tm_min", result.tm_min)
    if (result.tm_hour >= 10.5) and (result.tm_min >= 25.5) and (result.tm_min <= 27) and (result.tm_hour <= 11):
        GUI()
        time.sleep(60)
        break
# No resonse
    if (now >= future) and (x<=0):
        message = """\
        Get To Class
        """
        Timeout()
        x=1

    time.sleep(30)

