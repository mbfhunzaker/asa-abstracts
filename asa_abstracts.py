import csv
from string import punctuation

abstracts = []

with open('data/clean_asa_2014_prelim.csv', 'rU') as f:
    abstracts = [ row for row in csv.reader(f, delimiter=',') ]


roundtable_abstracts = []
panel_abstracts = []

for abstract in abstracts:
    if len(abstract[-1]) > 100:
        if 'Roundtable' in abstract[3]:
            roundtable_abstracts.append(abstract[-1])
        elif 'Regular Session' in abstract[3] or 'Section on '  in abstract[3]:
            panel_abstracts.append(abstract[-1])


from string import punctuation
from nltk.corpus import stopwords

stopword_list = stopwords.words('english')

def word_clean(word):
    lower_word = word.lower()
    clean_word = lower_word.strip(punctuation)
    return clean_word

def text_clean(sentence):
    words = sentence.split()
    cleaned_words = []
    for word in words:
        clean_word = word_clean(word)
        cleaned_words.append(clean_word)
    clean_words = set(cleaned_words)
    clean_words = list(cleaned_words)
    return clean_words

def wordcount(text):
    word_freq = {}
    for abstract in text:
        clean_abstract = text_clean(abstract)
        for word in clean_abstract:
            if word not in stopword_list:
                try:
                    word_freq[word] = word_freq[word] + 1
                except:
                    word_freq[word] = 1
    return word_freq

def paircount(text):
    pair_freq = {}
    for abstract in text:
        clean_abstract = text_clean(abstract)
        cleaner_abstract = []
        for word in clean_abstract:
            if word not in stopword_list:
                cleaner_abstract.append(word)
        abstract_pairs = combinations(shorter,2)
        for word_pair in abstract_pairs:
                try:
                    pair_freq[word_pair] = pair_freq[word_pair] + 1
                except:
                    pair_freq[word_pair] = 1
    return pair_freq

#Some Tests!
print wordcount(roundtable_abstracts[-3:])
