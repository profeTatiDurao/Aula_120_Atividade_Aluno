
#import nltk

#import json
#import pickle
#import numpy as np
#import random

#ignore_words = ['?', '!',',','.', "'s", "'m"]


#import tensorflow
#from data_preprocessing import get_stem_words

#model = tensorflow.keras.models.load_model('./chatbot_model.h5')


#intents = json.loads(open('./intents.json').read())
#words = pickle.load(open('./words.pkl','rb'))
#classes = pickle.load(open('./classes.pkl','rb'))

#crie as funções para estimizar e prever a resposta do robo



print("Oi, eu sou a Estela, como posso ajudar?")

while True:
    user_input = input("Digite sua mensagem aqui:")
    print("Entrada do Usuário: ", user_input)

    #crie a resposta do robo

