# Tensorflow-Discord-Chatbot

This is a chatbot that you can message interactively with using the Discord platform. The bot is trained on specific words and phrases, and can make educated decisions of how to respond depending on what you say to it. The machine-learning/neural-network aspect of how the bot works means that you don't have to give it very specific inputs to get a response that makes sense. 

## Technologies

* Tensorflow : an open-source machine-learning library for neural networks
* Discord API : used to connect the bot with the discord platform and be interactive on it
* NLTK : Natural Language Toolkit for Python, a language processing library for English

## How to Run

1. Fill out intents.json with possible inputs and responses
2. Run the training.py file to train the bot based on the text
3. Build a bot based on chatbot.py or use AlienBot.py the example
4. Run AlienBot.py (will need your personal Discord API keys)

## Future Improvements - Coming Soon

* more responses for when the bot thinks it might have an error
* ability to save & "learn" someone's name 
