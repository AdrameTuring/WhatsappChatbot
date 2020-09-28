from flask import Flask 
from flask import request
from twilio.rest import Client
from marketstack import get_stock_price
import os

# Here we initialize our app
app=Flask(__name__)

# Here we initialize our client
client=Client('AC82a28642c8b68dabf3c8e938270b655e','8be9b68abd6857818ceb00a5a80dfa35')
TWILIO_NUMBER='whatsapp:+14155238886'
# Here is the function wich used to send messge from our twilio number 
# to the recipient.
def Send_msg(msg,recipient):
        client.messages.create(
            from_=TWILIO_NUMBER,
            body=msg,
            to=recipient
        )
# This function protoype our response
def Process_msg(msg):
    response=""
    if(msg=="hi"):
        response="Welcome to the stock market bot"
        response+="Type sym:<stock_symbol> to know the price of the stock"
    elif 'sym' in msg:
            data=msg.split(":")

            stock_symbol=data[1]
            stock_price=get_stock_price(stock_symbol)

            last_price=stock_price["last_price"]
            last_price=str(last_price)
            
            response="The stock price of "+stock_symbol+ "is: $"+ last_price
    else:
        response="Please try hi to get started"
    return response


@app.route('/webhook',methods=["POST"])
#This function is used to access to user's msg and send a response
def Webhooks():
    # Access to user's ()
    f=request.form
    # Access to message's body
    msg=f['Body']
    #Access to message's sender
    sender=f['From']
    #We use Process_msg function and stock the response into a variable 
    response=Process_msg(msg)
    #We use Send_msg function to send response from our twilio number 
    # to the sender's number 
    Send_msg(response,sender)
    return "Ok la réponse a étè envoyée avec succés",200