from urllib.request import urlopen
from bs4 import BeautifulSoup

def isUnwantedTag(tag):
    for c in ['¤', '®']:
        if c in tag:
            return True
    return False

def extractTrendingTags():
    htmlPage = urlopen("http://www.trendinalia.com/twitter-trending-topics/india/india-180324.html")
    soup = BeautifulSoup(htmlPage.read().decode("ISO-8859-1"), 'html.parser')
    listofTags = list(set(extractTagsFromMainPage(soup)))
    listofTag = list(set(extractTagsFromOtherLocation(soup)))
    #listTags = (listofTags + listofTag)
    #print(listofTags)
    return listofTags
    #return listTags

#extract tags from main page
def extractTagsFromMainPage(soup):
    hashTags = []
    div = soup.find_all("div", {"class": "span6"})
    for row in div[0].findAll('table')[0].tbody.findAll('tr'):
        column = row.findAll('td')
        for x in column[1].findAll('a'):
            if not isUnwantedTag(x['title']):
                hashTags.append(x['title'])
    return hashTags


#extract tags based on location
def extractTagsFromOtherLocation(soup):
    hashTags = []
    div = soup.find_all("div", {"class": "well"})
    for header in div[0].find_all("h5"):
        if(header.text == "Other Locations (in)"):
            ul = header.find_next_sibling("ul")
            for x in ul.find_all("a"):
                if not isUnwantedTag(x['title']):
                    hashTags.append(x['title'])
                #print("http://www.trendinalia.com/twitter-trending-topics"+x[2:])
                htmlPage = urlopen("http://www.trendinalia.com/twitter-trending-topics"+x.get('href')[2:])
                soup = BeautifulSoup(htmlPage.read().decode("ISO-8859-1"), 'html.parser')
                hashTags.extend(set(extractTagsFromMainPage(soup)))
                #print(len(hashTags))
    return hashTags


#if __name__ == '__main__':
	#listofTags = extractTrendingTags()
	#print(len(listofTags))