'''
You have a text dataset. Write Python code to preprocess the text,
including tasks like tokenization, stemming, and removing stop words.
'''
import nltk
'''
--------------------TOKENIZATION----------------------------------
'''
sentence_data = "The First sentence is about Python. The Second: about Django. You can learn Python,Django and Data Ananlysis here "
nltk_tokens = nltk.sent_tokenize(sentence_data)
print (nltk_tokens)

word_data = "It originated from the idea that there are readers who prefer learning new skills from the comforts of their drawing rooms"
nltk_tokens = nltk.word_tokenize(word_data)
print (nltk_tokens)
'''
-------------------Stemming-------------------------------------
'''
from nltk.stem import PorterStemmer
nltk.download("punkt")
# Initialize Python porter stemmer
ps = PorterStemmer()
# Example inflections to reduce
example_words = ["program","programming","programer","programs","programmed"]
for word in example_words:
   print (word, ps.stem(word))

'''
---------------------STOP WORDS----------------------------------
What are Stop words?
Stop Words: A stop word is a commonly used word (such as “the”, “a”, “an”, “in”) that a search engine has been programmed to ignore, both when indexing entries for searching and when retrieving them as the result of a search query. 

We would not want these words to take up space in our database, or taking up valuable processing time. 
For this, we can remove them easily, by storing a list of words that you consider to stop words. 
NLTK(Natural Language Toolkit) in python has a list of stopwords stored in 16 different languages
'''
from nltk.corpus import stopwords

nltk.download('stopwords')
print(stopwords.words('english'))

example_sent = """This is a sample sentence,
                  showing off the stop words filtration."""

stop_words = set(stopwords.words('english'))
from nltk.tokenize import word_tokenize
word_tokens = word_tokenize(example_sent)
# converts the words in word_tokens to lower case and then checks whether
# they are present in stop_words or not
filtered_sentence = [w for w in word_tokens if not w.lower() in stop_words]
# with no lower case conversion
filtered_sentence = []

for w in word_tokens:
    if w not in stop_words:
        filtered_sentence.append(w)

print(word_tokens)
print(filtered_sentence)