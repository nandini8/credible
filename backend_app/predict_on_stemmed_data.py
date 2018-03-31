#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 14:59:05 2018

@author: rohan
"""
#import pickle as pk
from sklearn.externals import joblib
import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.stem import WordNetLemmatizer
from textblob import Word
import pandas as pd
from nltk.corpus import stopwords
import string

def predict_type(dataSet,):
    #print(dataSet)
    #loading training model
    clf = joblib.load("backend_app.mnb_merged_title.sav")
    count_vect = joblib.load("backend_app.vectoriser_merged_title.sav")
    out = []

    for i in dataSet:
        in_lst = []
        in_lst.append(i)
        out_lst = clf.predict(count_vect.transform(in_lst))
        out.append(out_lst[0])
    return out
    
def predict_score(dataSet):
    #print(dataSet)
    #loading training model
    clf = joblib.load("backend_app.mnb_merged_title.sav")
    count_vect = joblib.load("backend_app.vectoriser_merged_title.sav")
    score = []
    
    for i in dataSet:
        in_lst = []
        in_lst.append(i)
        sc = clf.predict_proba(count_vect.transform(in_lst))
        score.append(sc[0][1])
    return score


def credibility(dframe,str):
    df = dframe.copy()
    #create a new data frame with tag & score
    result = pd.DataFrame(columns = ["article_id", str, "label" , "credibility_score"])
    df = stemm(df, "content")
    tag = predict_type(df[str])
    prob = predict_score(df[str])
    #updating data frame
    result.article_id = dframe.article_id
    result[str] = dframe[str]
    result.label = tag
    result.credibility_score = prob
    return result

def stemm(dataSet, str):
    text = []
    text = dataSet[str]
    lemmatizer = WordNetLemmatizer()
    stop = stopwords.words('english')
    title=[]
    word_dict = []
    for t in text:
        exclude = set(string.punctuation)
        s= ''.join(i for i in t if not i.isdigit())
        s = ''.join(ch for ch in s if ch not in exclude)
        word_list=word_tokenize(s)
        words=''
        for word in word_list: 
            if(word not in stop): 
                word = lemmatizer.lemmatize(word)
                word = word.lower()
                #words.join(word)
                words+=' '
                word_dict.append(word)
                words += ''.join(word)
        #print(words)
        title.append(words)
    dataSet[str]=title 
    return dataSet

if __name__ == '__main__':
    #main
    df = pd.read_csv("text_tag.csv")
    df.columns = ["content" , "label"]
    out = credibility(df,"content")
    given = df.label
    pred = out.label

    count = 0
    for i in range(given.size):
        if given[i] == pred[i]:
            count = count + 1
    print(count/given.size)
    print(given.size)
