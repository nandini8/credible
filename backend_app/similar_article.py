# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 21:00:56 2018

@author: Abhishek
"""
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 21:00:56 2018

@author: Abhishek
"""
import gensim
import numpy as np
import pandas as pd
from nltk.tokenize import word_tokenize
import nltk, string
from sklearn.feature_extraction.text import TfidfVectorizer

SIMILARITY_THRESHOLD_SCORE = 0.6

def addRow(df, row):
    df.loc[-1] = row
    df.index = df.index + 1  # shifting index
    df = df.sort_index()  # sorting by index
    

stemmer = nltk.stem.porter.PorterStemmer()
remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)
    
def stem_tokens(tokens):
    return [stemmer.stem(item) for item in tokens]

'''remove punctuation, lowercase, stem'''
def normalize(text):
    return stem_tokens(nltk.word_tokenize(text.lower().translate(remove_punctuation_map)))

vectorizer = TfidfVectorizer(tokenizer=normalize, stop_words='english') 

def cosine_sim(text1, text2):
    tfidf = vectorizer.fit_transform([text1, text2])
    return ((tfidf * tfidf.T).A)[0,1]

def cosineSimBatch(content, contentList):
    scoreList = []
    for txt in contentList:
        scoreList.append(cosine_sim(content, txt))
    return scoreList

def getArticleTopicIds(articleDf):
    idList = []
    topicsDf = pd.DataFrame(columns=['topic_id', 'content'])
        
    for index, row in articleDf.iterrows():

        if topicsDf.empty:
            addRow(topicsDf, [row['article_id'], row['content']])
            idList.append(row['article_id'])
            continue
        
        simScoreList =  cosineSimBatch(row['content'], topicsDf['content'])
     
        #print('comparing document: ', row['content'][:80], '\n\tscore: ', simScoreList)
        
        if np.max(simScoreList) < SIMILARITY_THRESHOLD_SCORE:
            addRow(topicsDf, [row['article_id'], row['content']])
            idList.append(row['article_id'])
        else:
            idList.append(idList[np.where(simScoreList == np.max(simScoreList))[0][0]])

    articleDf['topics_id'] = idList    
    return articleDf
    

if __name__ == '__main__':
    contentClm = ["The 28yearold Quebec City man charged with murder and attempted murder in the shooting at the Quebec Islamic Cultural Centre last year has pleaded not guiltyAlexandre Bissonnette was charged with a total of 12 offences in the shooting that left six dead and five critically injuredHe was charged with six counts of firstdegree murder and six of attempted murder with five charges related to people who were critically wounded One of the attempted murder charges collectively includes 35 people  31 men and four children  who witnessed the shootingBissonnette was present in a Quebec City courtroom this morning as Justice François Huot read out each of the charges After each he replied not guiltyHeightened securitySecurity to enter the courtroom was tight  anyone wanting to watch the proceedings must pass through a metal detector Those watching the proceedings were also asked to present government identificationThe widow of one of the victims surrounded by a group of friends was among those who showed up at the courthouse for the first day of the proceedings Several of the women wept as Bissonnette entered his pleaThe founders of the mosque were also presentThis pretrial portion of the proceedings will determine what evidence the jury will hear Any evidence presented during this portion is covered by a publication ban a routine step taken to ensure no prejudicial information is heard by potential jurorsThe trial is expected to last two months and jury selection is scheduled to start next week The judge in the case asked for 600 potential jury members to be summoned three times as many as routinely requested for a trial in Quebec City",
           "New Delhi Prime Minister Narendra Modis NaMo App has witnessed around two lakh new downloads after the Congress alleged data theft by the application the BJP sources claimed on WednesdayWhen the Congress Party started the DeleteNaMoApp campaign on social media hardly would they have imagined that the outcome would have been so different party sources here saidSince the Congress campaign against NaMo App started it has notched up more than 2 lakh new downloads The rate of downloads has increased manifold since the Congress  Rahul Gandhi started attacking it a senior party source saidBJP sources said that Modi in a recent meeting with MPs had stressed upon the need to connect with people using the app The party had initiated a massive outreach campaign using this app to involve booth level workers across the countryAfter allegations that data from the prime ministers official app was shared with foreign firms without the consent of users Congress president Rahul Gandhi had said the NaMo App secretly recorded audio video and contacts Gandhi used the hashtag DeleteNaMoAppHitting back Union minister Smriti Irani had said even Chhota Bheem a cartoon character knew that commonly asked permission on apps do not tantamount to snooping",
             "New Delhi Prime Minister Narendra Modis NaMo App has witnessed around two lakh new downloads after the Congress alleged data theft by the application the BJP sources claimed on WednesdayWhen the Congress Party started the DeleteNaMoApp campaign on social media hardly would they have imagined that the outcome would have been so different party sources here saidSince the Congress campaign against NaMo App started it has notched up more than 2 lakh new downloads The rate of downloads has increased manifold since the Congress  Rahul Gandhi started attacking it a senior party source saidBJP sources said that Modi in a recent meeting with MPs had stressed upon the need to connect with people using the app The party had initiated a massive outreach campaign using this app to involve booth level workers across the countryAfter allegations that data from the prime ministers official app was shared with foreign firms without the consent of users Congress president Rahul Gandhi had said the NaMo App secretly recorded audio video and contacts Gandhi used the hashtag DeleteNaMoAppHitting back Union minister Smriti Irani had said even Chhota Bheem a cartoon character knew that commonly asked permission on apps do not tantamount to snooping",
             "Aamir Khans global appeal and geographical reach into unexplored markets has him enjoying the status of the worlds biggest Superstar explains Trade Analyst Amul MohanDecoding Aamir Khans stature as an actor and entertainer Amul Mohan explainsVery few stars have the ability to bring the audience into the cinemas by the truckloads like Aamir and his track record is a testament to that It all started a decade ago in 2008 when his movie Ghajini opened and went on to be the first 100 crore movie After starting the 100 crore club Aamir Khan also happens to be the one to start the 200 crore club 300 crore club The actor holds the record for the highest scoring Hindi film with Dangal at 370 crores which is yet untouched by anyone elseAmul Mohan addsHis different and out there choices make him stand head and shoulders above the rest of his competitors And one of the major reasons for his constant rise is the way the audiences adore him and back him in all that he doesThe number of people who know Aamir Khan by his name and face is gigantic The actor has a phenomenal fan following in India and China respectively With the combined population of 14 billion and 135 billion in China and India respectively Aamir Khan is the biggest Superstar globally and geographicallyHe further informsAamir Khan also happens to be the only actor with 3 films in the Top 5 films with highest worldwide collections With every next movie Aamir Khan has only has bettered the number barring a few offs It is 2018 now and the audience not only in the metros but pan India have a lot of options Options for different kinds of movies and television shows and other things which theyre no longer consuming in a movie theatre or their television screens In a world like that Aamir is still the constant in bringing the audience to a cinema hallTrendingAamir Khans PK when it was released in China it was a decent success but when his Dangal released in China it had broken all records thereAamir was hailed for his powerpacked performance in the film and Dangal instantly made Aamir Khan as a megastar in ChinaAs a matter of fact Chinese IMDB ranked Dangal their No1 film and ranked Aamir Khan as No 1 foreign actorThe massive success of Secret Superstar in China added one more feather to Aamirs cap and cemented the fact that Aamir is the biggest foreign movie star in ChinaAamirs films have a universal appeal as its not targeted towards a particular age group or region in terms of content His films resonate with people around the globeThe actor is currently working on two highly anticipated projects which include Thugs Of Hindostan and the magnum opus Mahabharat which will be a threepart seriesWith a massive fan following which amounts approximately to 3 billion people and audience from other countries across the globe watching Aamir Khans film We can easily deduce that Aamir is the biggest Superstar in the world",
           "BY Follow JoeSchoffstallA Texas county has been hit with a lawsuit for concealing records in relation to noncitizens on voter rollsThe Public Interest Legal Foundation PILF an election integrity group filed a complaint on Thursday against the Office of the Harris County Voter Registrar in the United States District Court for the Southern District of Texas for its refusal to disclose documents or allow the inspection of its voter rolls in relation to registrants who were removed after it was discovered that they were noncitizensThe Foundation seeks a declaration that all of Defendants records related to list maintenance including but not limited to those explicitly requested by the Foundation are subject to public inspection without encumbrance by any state public disclosure laws and must be preserved for such inspection purposes the complaint reads The Foundation seeks an injunction to compel Defendant Bennett to comply with Subsection 20507i through an order commanding her to permit inspection and duplication of all records concerning the maintenance of registration listsVoter registration officials in Harris County previously testified that thousands of noncitizens were discovered on their rolls every year and then handed over to the District Attorney for prosecution Houston one of the largest cities in the United States is located in Harris CountyPILF initially requested to review the records of Harris County on Dec 1 2017 but was ultimately denied access to the documents on Jan 11 The group then sent a final notice to the county in late January warning that they could face a federal lawsuit if they continued to deny the group inspection of the recordsPILF is seeking access to the records under Section 8 of the National Voters Registration Act of 1993 which allows individuals to inspect records concerning the implementation of programs and activities conducted for the purpose of ensuring accuracy and currency of official lists of eligible votersHarris County has previously admitted a problem with noncitizen registration and voting J Christian Adams president and general counsel of PILF said of the suit Election officials should be transparent and in fact are required by federal law to be transparent Our requests to inspect records will help educate lawmakers and the public alike on how noncitizens are gaining entry into the voting system how long they remain how they vote and what we can do to fix the issue The question is not ifbut how many noncitizens are participating Harris County cannot expect to get away with avoiding its federal transparency responsibilitiesThe Harris County voter registrar did not return a request for comment by press timeAnother Texas County was also recently threatened with a lawsuit for withholding identical records in relation to noncitizens registered to voteBexar County which includes the city of San Antonio also one of the most populous counties in the country declined PILFs request to inspect their rolls following discovery or admittance of noncitizens that were removed from the rolls in DecemberPILF threatened the suit against Bexar County in late January"]
    articleIdClm = ['id1', 'id2', 'id3', 'id4', 'id5']
    
    articleDf = pd.DataFrame({'article_id': articleIdClm,
                 'content': contentClm})
    
    print(getArticleTopicIds(articleDf))
