# This program is about to create a Telegram Bot

# Importing Modules
import requests
import json

# Defining functions
def summary(update, context):
    response = requests.get('https://api.covid19api.com/summary')
    if(response.status_code==200): #Everything went okay, we have the data
        data = response.json()
        print(data['Global'])
        context.bot.send_message(chat_id=update.effective_chat.id, text=data['Global'])
    else: #something went wrong
        context.bot.send_message(chat_id=update.effective_chat.id, text="Error, something went wrong.")
​
corona_summary_handler = CommandHandler('summary', summary)
dispatcher.add_handler(corona_summary_handler)