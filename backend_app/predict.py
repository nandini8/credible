#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 14:59:05 2018

@author: rohan
"""
#import pickle as pk
from sklearn.externals import joblib
import pandas as pd

def predict_type(dataSet,):
    #print(dataSet)
    #loading training model
    clf = joblib.load("backend_app/mnb_mix_title.sav")
    count_vect = joblib.load("backend_app/vectoriser_mix_title.sav")
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
    clf = joblib.load("mnb_mix_title.sav")
    count_vect = joblib.load("vectoriser_mix_title.sav")
    score = []
    
    for i in dataSet:
        in_lst = []
        in_lst.append(i)
        sc = clf.predict_proba(count_vect.transform(in_lst))
        score.append(sc[0][1]*0.3 + 0.65)
    return score


def credibility(df,content):
    #create a new data frame with tag & score
    result = pd.DataFrame(columns = ["article_id", content, "label" , "credibility_score"])
    tag = predict_type(df[content])
    prob = predict_score(df[content])
    #updating data frame
    result.article_id = df.article_id
    result[content] = df[content]
    result.label = tag
    result.credibility_score = prob
    print(result)
    return result
    
#main
if __name__ == '__main__':
    #df = pd.read_csv("mix_text_tag.csv")
    out = credibility(df,"content")
    given = df.label
    pred = out.label

    count = 0
    for i in range(given.size):
        if given[i] == pred[i]:
            count = count + 1
    print(count/given.size)
    print(given.size)
