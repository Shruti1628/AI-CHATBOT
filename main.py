import datetime
import time
name = input("Welcome To AI ChatBot!!.Please Tell Me Your Good Name:")
presenthour=datetime.datetime.now().hour #function to get current time
if 5<=presenthour <=11:
    print("GoodMorning !",name)
elif 11<=presenthour <17:
    print("GoodAfternoon !!",name)
elif 17<= presenthour <20:
    print("goodEvening!",name)  
else:
    print("GoodNight!",name)
# creating a memory in chatbot
responses={
         "hello": "Hi!.How can I help You?",
         "how are you": "I am Fine.Thankyou!!",
         "who Are You":"I am Smart Ai ChatBox.",
         "motivate me":"The Best Time To Plant a Tree Was 20 Years Ago.The Second Best Time Is Now!! ",
          "happy":"Great To Hear that!! Happiness Of your Life Depends On The Quality Of Your Thoughts!!"
    }    
# DeFINE A function
def getResponse(userQuestion):
    userQuestion = userQuestion.lower()
    for eachkey in responses:
        if eachkey in userQuestion:
            return responses[eachkey]
        else:
            ("I am not able to tell you that. I Am in Learning Process")
        
#Taking The Input From User
while True:      
    UserInput =input("Enter The Question You Want To Ask:")
    result = getResponse(UserInput)     
    print("AI Bot Response:",result)
    if "bye" in UserInput.lower():
     break
print("Thankyou For Using AI Chatbox")

 

