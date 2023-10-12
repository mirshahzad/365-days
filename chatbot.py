# This is a chat bot program

"""
Follow the below steps:
(i) pip install ChatterBot chatterbot-corpus spacy
(ii) python 3 -m spacy download en_core_web_sm
Or
choose the language you prefer
(iii) Navigate to the python3 directory
(iv) Modify lib/site-packages/chatterbot/tagging.py file to propoerly
load 'en_core_web_sm' 
"""

# 
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer


def create_chat_bot():
   chatbot = ChatBot('Chattering Bot')
   trainer = ChatterBotCorpusTrainer(chatbot)
   trainer.train('chatterbot.corpus.english')

   while True:
       try:
           bot_input = chatbot.get_response(input())
           print(bot_input)

       except (KeyboardInterrupt, EOFError, SystemExit):
           break


if __name__ == '__main__':
   create_chat_bot()