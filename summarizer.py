from gensim.summarization.summarizer import summarize
from gensim.summarization import keywords
 
import requests
 
# getting text document from Internet
#text = requests.get('http://rare-technologies.com/the_matrix_synopsis.txt').text
 
 
# getting text document from file
'''
fname="C:\\Users\\TextRank-master\\wikipedia_deep_learning.txt"
with open(fname, 'r') as myfile:
      text=myfile.read()
'''     
     
#getting text document from web, below function based from 3
from bs4 import BeautifulSoup
from urllib.request import urlopen
 
def get_only_text(url):
    
    """ 
    return the title and the text of the article
    at the specified url
    """
    page = urlopen(url)
    soup = BeautifulSoup(page, "lxml")
    text = ' '.join(map(lambda p: p.text, soup.find_all('p')))
    return soup.title.text, text    
''' 
fname="C:\Users\nEW u\Documents\the_matrix_synopsis.txt"
with open(the_matrix_synopsis.txt, 'r') as myfile:
      text = myfile.read()
'''
text = open("kafka.txt" , encoding="utf8").read()
      
print ('Summary:')
print (summarize(text, ratio=0.01))
 
print ('\nKeywords:')
print (keywords(text, ratio=0.01))
 
url="https://en.wikipedia.org/wiki/India"
text = get_only_text(url)
 
print ('Summary:')   
print (summarize(str(text), ratio=0.01))
 
print ('\nKeywords:')
 
# higher ratio => more keywords
print (keywords(str(text), ratio=0.01))