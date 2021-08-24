import random
import json
import pickle
import numpy as np

import nltk
from nltk.stem import WordNetLemmatizer

from tensorflow.keras.models import load_model

lemmatizer = WordNetLemmatizer()
intents = json.loads(open('intents.json').read())

words = pickle.load(open('words.pkl', 'rb'))
tags = pickle.load(open('tags.pkl', 'rb'))

model = load_model('chatbotmodel.h5')

def clean_up_sentence(sentence):
	sentence_words = nltk.word_tokenize(sentence)
	sentence_words = [lemmatizer.lemmatize(word) for word in sentence_words]
	return sentence_words

def bag_of_words(sentence):
	sentence_words = clean_up_sentence(sentence)
	bag = [0] * len(words)
	for w in sentence_words:
		for i, word in enumerate(words):
			if word == w:
				bag[i] = 1
	return np.array(bag)

def predict_tag(sentence):
	bagOfWords = bag_of_words(sentence)
	res = model.predict(np.array([bagOfWords]))[0]
	ERROR_THRESHOLD = 0.25 # 25% for now
	results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]

	results.sort(key=lambda x: x[1], reverse=True)
	return_list = []
	for r in results:
		return_list.append({'intent': tags[r[0]], 'probability': r[1]})
	return return_list

def get_response(message):
	predictedTags = predict_tag(message)
	probability = predictedTags[0]['probability'];

	if (probability > 0.7):
		response = ""
		tag = predictedTags[0]['intent']
		allIntents = intents['intents']
		for i in allIntents:
			if i['tag'] == tag:
				response = random.choice(i['responses'])
				break
		return response
	else: # less sure the bot has the correct response
		return "Sorry, I thought about what you said, but I am not sure how to respond yet. Please send your exact message in #bot-suggestions so my creator can fix this!"