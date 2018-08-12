from tkinter import *
import tkinter as tk

chat_window = Tk()
chat_window.title("Hitam Bot")

#Determining the size of the chat window
#chat_window.geometry("450x600")
chat_window.geometry('{}x{}'.format(450, 600))

#Removing min/max button from the window to maintain the window
chat_window.resizable(0,0)

#Creating the top frame
top = Frame(chat_window)
top.pack(side=TOP,fill=X)

#Creating the bottom frame
bottom = Frame(chat_window)
bottom.pack(side=BOTTOM,fill=X)

#This displays the heading text on the top of the chat  window
head_text = Label(top,text="Hi,I am Leo the hitam bot.I am new and still learning.Start chatting.")
head_text.pack(side=TOP,fill=X)

#Textfield in the bottom frame to take the user input
input_user = StringVar()
input_field = Entry(bottom,text=input_user)
input_field.pack(fill=X,ipadx=10)

#Send button in the bottom frame
send_button = Button(bottom,text="Send")
send_button.pack(fill=X,ipadx=10)



#Main loop that runs the chat window over and over till the user terminates the process
chat_window.mainloop()



"""
#importing the listtrainer
from chatterbot.trainers import ListTrainer

from chatterbot.logic import LowConfidenceAdapter

from chatterbot.response_selection import get_random_response

#importing the chatbot
from chatterbot import ChatBot

#importing os to use operating system features
import os

#Creating the  instance of the leo
leo=ChatBot('Leo',read_only=True,
                logic_adapters=[
                {
                    'import_path': 'chatterbot.logic.BestMatch'
                },
                {
                    "import_path" : "chatterbot.logic.LowConfidenceAdapter",
                    "threshold" : 0.80,
                    "default_response" : "Sorry,We are working on it :-("
                }
            ],
            filters=[
                'chatterbot.filters.RepetitiveResponseFilter'
            ])


#Setting the trainer for leo
leo.set_trainer(ListTrainer)

#Loop to read all the data in the coversations folder
for _file in os.listdir('Conversations'):
    Convo=open('Conversations/'+_file, 'r').readlines()
    leo.train(Convo)

print('''************************HITAM BOT***********************************''')

print("Hi,I am Leo the hitam bot.I am new and still learning.Start chatting.")

#Chat loop
while True:
    try:
        request = input('You: ')

        response = leo.get_response(request)

        if (request == ""):
            print('Leo: Ask something so that I can help you')
        #elif (response.confidence ==  0):
            #print("Leo: We are working on it")
        elif (request == 'bye' or request=='bubye'):
            print('Leo: Bubye,Have a nice day')
            exit()
        else :
            print('Leo: ',response)

    except(KeyboardInterrupt,EOFError,TimeoutError,RuntimeError,SystemError,SystemExit):
        break
"""