import pandas as pd
from string import punctuation
from string import digits


#class containing the word frequency dictionary and its correspinding score
class review:
    def __init__(self, wordFreq, score,ID):
        self.dict = dictionary
        self.score = score
        self.id = ID


#will return a dictionary of word fequencies for each review
#TODO ignore empty entries
#to parse entire data sheet set range to 19555
for i in range(3):
    dictionary = {}

    #read excel doc and parce desired section
    df = pd.read_excel (r'songReviewDataP1.xlsx', usecols = [6], nrows = 1, skiprows = i+1)
    scoreVal = pd.read_excel (r'songReviewData.xlsx', usecols = [7], nrows = 1, skiprows = i+1)

    text = df.to_string().lower()

    temp = scoreVal.to_string()
    reviewScore = temp.partition('\n')[0]

    #exclude all punctuation and numbers from review
    text = "".join([ch for ch in text if ch not in punctuation and ch not in digits])
    text = text.split()
    for j in text:
            dictionary[j] = dictionary.get(j, 0)+1

    #creates a new instance of class for each song reviewed
    reviewExample = review(dictionary, reviewScore, i)

    print("Word frequency:\n", reviewExample.dict,"\n","Score for given review:", reviewExample.score, "\n", "ID:", reviewExample.id)
