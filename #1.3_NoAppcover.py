#1.3 Translation and Context understanding

from translate import Translator

# Create a translator object
translator = Translator(to_lang="ur")

# Translate a phrase
mywordbefore = """
Today is a very disruptive world, 
but Machine Learning and AI, 
specifically Natural Language Processing, 
is a fascinating field at the intersection of computer science, 
artificial intelligence, and linguistics.
"""


mywordafter = translator.translate(mywordbefore)
print(mywordafter)  # Urdu


from textblob import TextBlob



# Create a TextBlob object
blobbefore = TextBlob(mywordbefore)
blobafter = TextBlob(mywordafter)


# Perform sentiment analysis
sentimentbefore = blobbefore.sentiment
print("before" ,sentimentbefore)  # Output: Sentiment(polarity=0.65, subjectivity=0.6)

# Perform sentiment analysis
sentimentafter = blobafter.sentiment
print("after" ,sentimentafter)  # Output: Sentiment(polarity=0.65, subjectivity=0.6)