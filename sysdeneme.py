import nltk
nltk.download('reuters')
from nltk.corpus import reuters

categories = ['wheat', 'tea', 'strategic-metal', 
              'housing', 'money-supply', 'fuel']
print(reuters.sents(categories = categories)[5])