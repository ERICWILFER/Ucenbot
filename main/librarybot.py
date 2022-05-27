from django import template
from django.conf.urls.static import static
import nltk
from nltk.stem.lancaster import LancasterStemmer
import numpy
import tflearn
import tensorflow as tf
import json
import pickle
import datetime
import random
# import pyttsx3

stemmer = LancasterStemmer()
with open("static/librarybot/intents.json") as file:
    data = json.load(file)
try:
    # we_are_training
    with open("static/librarybot/data.pickle", "rb") as f:
        words, labels, training, output = pickle.load(f)
except:
    words = []
    labels = []
    docs_x = []
    docs_y = []
    for intent in data["intents"]:
        for pattern in intent["patterns"]:
            wrds = nltk.word_tokenize(pattern)
            words.extend(wrds)
            docs_x.append(wrds)
            docs_y.append(intent["tag"])
        if intent["tag"] not in labels:
            labels.append(intent["tag"])
    words = [stemmer.stem(w.lower()) for w in words if w != "?"]
    words = sorted(list(set(words)))
    # labels = sorted(labels)
    training = []
    output = []
    out_empty = [0 for _ in range(len(labels))]
    for x, doc in enumerate(docs_x):
        bag = []
        wrds = [stemmer.stem(w.lower()) for w in doc]
        for w in words:
            if w in wrds:
                bag.append(1)
            else:
                bag.append(0)
        output_row = out_empty[:]
        output_row[labels.index(docs_y[x])] = 1
        training.append(bag)
        output.append(output_row)
    training = numpy.array(training)
    output = numpy.array(output)
    with open("static/librarybot/data.pickle", "wb") as f:
        pickle.dump((words, labels, training, output), f)
tf.compat.v1.reset_default_graph()
net = tflearn.input_data(shape=[None, len(training[0])])
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, len(output[0]), activation="softmax")
net = tflearn.regression(net)
model = tflearn.DNN(net)
try:
    # we_are_training
    model.load("static/librarybot/model.tflearn")
except:
    model.fit(training, output, n_epoch=1000, batch_size=8, show_metric=True)
    model.save("static/librarybot/model.tflearn")


def bag_of_words(s, words):
    bag = [0 for _ in range(len(words))]
    s_words = nltk.word_tokenize(s)
    s_words = [stemmer.stem(word.lower()) for word in s_words]
    for se in s_words:
        for i, w in enumerate(words):
            if w == se:
                bag[i] = 1
    return numpy.array(bag)


# def talk(text):
#     engine = pyttsx3.init()  # object creation for text to speech
#     engine.setProperty('rate', 125)  # rate of speaking
#     voices = engine.getProperty('voices')
#     # 1 for female voice and 0 for male voice
#     engine.setProperty('voice', voices[1].id)
#     engine.say(text)
#     engine.runAndWait()
#     engine.startLoop(False)
#     engine.endLoop()


def response(inp):
    results = model.predict([bag_of_words(inp, words)])[0]
    results_index = numpy.argmax(results)
    tag = labels[results_index]
    if results[results_index] > 0.6:
        for tg in data["intents"]:
            if tg['tag'] == tag:
                responses = tg['responses']
                contexts = tg['context_set']
        global contextimg
        contextimg = random.choice(contexts)
        rresponse = random.choice(responses)
        print(rresponse)
        # print(contextimg)
        # talk(rresponse)
    else:
        rresponse = "I didn't really get that"
        contextimg = "./static/context/images/error.gif"
        # talk("I didn't really get that")
    return rresponse , contextimg;

 
