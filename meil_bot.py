import tkinter as tk
from tkinter import filedialog
import smtplib
import imghdr
from email.message import EmailMessage
import time
import datetime

root = tk.Tk()
root.title("Email-bot 1000")
sending = False
file = []


def addFile():
    filename = filedialog.askopenfilename(
        initialdir="/", title="Choose file", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if(len(file) != 0):
        file.clear()
    file.append(filename)
    label["text"] = f"Loaded file: {file[0]}"


def startSendingEmails():

    EMAIL_ADDRESS = "xxxx@xxxx.xx"
    EMAIL_PASSWORD = "xxxxxxx"

    msg = EmailMessage()
    msg['Subject'] = 'Subject'
    msg['From'] = "From"

    msg.set_content('This is a plain text email')

    msg.add_alternative("""\
    <!DOCTYPE html>
    <html>

    <body>

    
    </body>
    </html>
    """, subtype='html')

    """Every 50 mails, there is 5 minuts brake, due to STMP limitation and 24h break, due to  Gmail"""

    count = 0
    count_global = 0
    with open(file[0], "r") as file_meil:
        for mail in file_meil:
            count += 1
            if(count == 50):
                count = 0
                time.sleep(360)
            elif(count_global == 460):
                count_global = 0
                time.sleep(87000)
            try:
                with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                    smtp.send_message(msg, None, mail)
                    time.sleep(5)
            except:
                label_error = tk.Label(text=f"Problem with: {i}")
                label_error.pack()


canvas = tk.Canvas(root, height=400, width=400)
canvas.pack()

startSending = tk.Button(root, text="Start", padx=10,
                         pady=5, bg="green", command=startSendingEmails)
openFile = tk.Button(root, text="Open file", padx=10,
                     pady=5, bg="green", command=addFile)

label = tk.Label(text="Choose file")

label.pack()
startSending.pack()
openFile.pack()
root.mainloop()
