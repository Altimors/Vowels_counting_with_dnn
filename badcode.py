import argparse
import numpy as np
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 

from tensorflow import keras
import math

parser = argparse.ArgumentParser(description="Return the number of vowels in a string using a machine learning dense model")

parser.add_argument('string', help="String to count vowels")
parser.add_argument('-l', '--load_weights', action='store_true', help="If set, will load the 'model.h5' file storing the model and the associated weights. If not set, will train the model on the train dataset 'imdb' and then saved it.")

args = parser.parse_args()

vowels = ['a', 'e', 'i', 'o', 'u', 'y']

def nb_vowels(s) :
    nb_v = 0
    for c in s.lower() :
        if c in vowels :
            nb_v += 1

    return nb_v

def get_char_array_count(s) :
    data = np.zeros(26)
    for c in s :
        i = ord(c) -  ord('a')
        
        if i < 0 or i > 25 :
            continue

        data[i] += 1

    return data

def generates_dataset(file) :
    X = []
    Y = []
    names = []
    for line in file.readlines() :
        l = line.split(" ")
        
        if len(l) < 2 :
            break

        s = ''.join(l[0:-1])
        s = s.lower()
        names.append(''.join(l[0:-1]))
        X.append(get_char_array_count(s))
        Y.append(int(l[-1]))

    X = np.array(X)
    Y = np.array(Y)

    return names, X, Y

    # X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=1)
    # X_train_names, X_test_names, Y_train_names, Y_test_names = train_test_split(names, Y, test_size=0.2, random_state=1)


if __name__ == "__main__" :

    model = keras.models.Sequential([
        keras.layers.Dense(26),
        keras.layers.Dense(1),
    ])

    model.compile(loss="mse", optimizer='adam', metrics=["accuracy"])

    if args.load_weights :
        model = keras.models.load_model("model.h5", compile=False)
    else :
        file = open("train.txt", "r")
        names, X, Y = generates_dataset(file)
        
        model.fit(X, Y,  epochs=10, validation_split=0.1, batch_size=10)
        model.save("model.h5") 
    
    y = model.predict(np.array([get_char_array_count(args.string)]))
    print("'{}' : {} voyelles.".format(args.string, round(y[0, 0])))