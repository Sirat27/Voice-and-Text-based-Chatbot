from tkinter import *
import pyttsx3
import speech_recognition
import threading

engine = pyttsx3.init()
engine.setProperty('rate', 150)
# from chatterbot import ChatBot
# from chatterbot.trainers import ListTrainer


# bot = ChatBot('Bot')  # object of chatbot class
# trainer = ListTrainer(bot)  # define train object variable
#
#
#
# trainer.train(data_list)  # train function to train the data

# data_list = {
#     "hi": "hey there",
#     "hello": "hey there",
#     "how are you": "i am fine , thanks",
#     "hi,how is it going": "good",
#     "what is your name": "my name is chatbot ",
#     "can you play a song": "which song",
#     "can you help me in selecting my project": "sure,let me know your field of study",
#     "can you help me with my project": "sure,let me know your field of study",
#     "can you help me in my project": "sure,let me know your field of study",
#     "i need help": "how can i help",
#     "help me": "how can i help",
#     "help": "how can i help",
#     "my field of study is engineering": "ok , which branch of engineering?",
#     "i am pursuing computer science engineering": "ok , which field of computer engineering you are good in?",
#     "i am pursuing electrical engineering": "ok , which field of electrical engineering you are good in?",
#     "i am pursuing mechanical engineering": "try developing a solar powered water heater or a heat pump",
#     "i am interested in web development": "try making library/hospital management system or a web app",
#     "web development": "try making hospital management system or food delivery web app",
#     "i am interested in machine learning": "try making face recognition or match predictor system",
#     "i am interested in data science": "try making fraud detection or anomaly detection system",
#     "i am interested in app development": "try making food delivery or travel application system",
#     "i am interested in signal processing": "you can work on time series analysis or sound detection radar model",
#     "i am interested in micro electronics": "you can develop an IC that can perform signal amplification",
#     "thank you": "you are welcome"
# }

qna = {
    "hi": "hey there",
    "hello": "hey there",
    "how are you": "i am fine , thanks",
    "hi,how is it going": "good",
    "what is your name": "my name is chatbot ",
    "can you play a song": "which song",
    "can you help me in selecting my project": "sure,let me know your field of study",
    "can you help me with my project": "sure,let me know your field of study",
    "can you help me in my project": "sure,let me know your field of study",
    "i need help": "how can i help",
    "help me": "how can i help",
    "help": "how can i help",
    "my field of study is engineering": "ok , which branch of engineering?",
    "i am pursuing computer science engineering": "ok , which field of computer engineering you are good in?",
    "i am pursuing electrical engineering": "ok , which field of electrical engineering you are good in?",
    "i am pursuing mechanical engineering": "try developing a solar powered water heater or a heat pump",
    "i am interested in web development": "try making library/hospital management system or a web app",
    "web development": "try making hospital management system or food delivery web app",
    "i am interested in machine learning": "try making face recognition or match predictor system",
    "i am interested in data science": "try making fraud detection or anomaly detection system",
    "i am interested in app development": "try making food delivery or travel application system",
    "i am interested in signal processing": "you can work on time series analysis or sound detection radar model",
    "i am interested in micro electronics": "you can develop an IC that can perform signal amplification",
    "thank you": "you are welcome"
}


# function to display question text in text area
def botReply():
    question = questionField.get()
    # answer = bot.get_response(question)
    answer = qna[question]
    textarea.insert(END, 'You : ' + question + '\n')
    textarea.insert(END, 'Bot : ' + str(answer) + '\n\n')
    questionField.delete(0, END)
    engine.say(qna[question])
    engine.runAndWait()


# function to convert audio/speech to text
def audioToText():
    while True:
        sr = speech_recognition.Recognizer()
        try:
            with speech_recognition.Microphone()as m:
                sr.adjust_for_ambient_noise(m, duration=0.2)
                audio = sr.listen(m)
                query = sr.recognize_google(audio)
                questionField.delete(0, END)
                questionField.insert(0, query)
                botReply()
        except Exception as e:
            print(e)


root = Tk()

root.geometry('500x570+100+30')  # set dimensions of the chatbot window
root.title('ChatBot')  # adds title of the window
root.config(bg='red')  # used to add background colour to our window

logoPic = PhotoImage(file='pic.png')  # to create/import image into the code
logoPicLabel = Label(root, image=logoPic, bg='red')
logoPicLabel.pack(pady=5)  # top by default -> used for placing of image

centerFrame = Frame(root)
centerFrame.pack()  # container/text area

scrollbar = Scrollbar(centerFrame)
scrollbar.pack(side=RIGHT)  # to create scrollbar at right

textarea = Text(centerFrame, font=('times new roman', 20, 'bold'), height=10, yscrollcommand=scrollbar.set, wrap='word')
textarea.pack(side=LEFT)  # to create text area at left
scrollbar.config(command=textarea.yview)

questionField = Entry(root, font=('verdana', 20, 'bold'))
questionField.pack(pady=15, fill=X)  # adding the question text field

askPic = PhotoImage(file='ask.png')
askButton = Button(root, image=askPic, command=botReply)  # designing the enter button
askButton.pack()


def click(event):
    askButton.invoke()


root.bind('<Return>', click)  # enter key can be used to invoke ask button

thread = threading.Thread(target=audioToText)
thread.setDaemon(True)
thread.start()

root.mainloop()  # with the help of mainloop method we can see our window continuously
# ---------------------------------------------------------------
