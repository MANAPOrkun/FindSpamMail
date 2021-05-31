import re
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
import nltk
import os

nltk.download('punkt')

ps = PorterStemmer()
word_list_index = {}
word_list_counter = {}

for filename in os.listdir('Spamas'):
    print(filename)
    try:
        input_program = open("Spamas\\"+filename, "r").read()

        # Replace email address with 'emailaddress'
        input_program = re.sub(r'[\w\.-]+@[\w\.-]+\.\w+', ' emailadress ', input_program)

        # Replace urls with 'webaddress'
        input_program = re.sub(r'[\w\.-]+@[\w\.-]+\.\w+', ' webadress ', input_program)

        # Replace money symbol with 'money-symbol'
        input_program = re.sub(r'£|\$', 'money-symbol', input_program)

        # Replace 10 digit phone number with 'phone-number'
        input_program = re.sub(".*?(\(?\d{3}\D{0,3}\d{3}\D{0,3}\d{4}).*?", ' phone-number ', input_program)

        # Replace normal number with 'number'
        input_program = re.sub('\d', ' number ', input_program)

        # remove punctuation
        input_program = re.sub(r'[^\w\d\s]', ' ', input_program)

        # remove whitespace between terms with single space
        input_program = re.sub(r'\s+', ' ', input_program)

        # remove leading and trailing whitespace
        input_program = re.sub(r'^\s+|\s*?$', ' ', input_program)

        # change words to lower case
        input_program = input_program.lower()

        words = word_tokenize(input_program)

        i = 0
        for w in words:
            lex = ps.stem(w)
            if lex not in word_list_index.keys():
                word_list_index[lex] = i
                word_list_counter[lex] = 1
                i = i + 1
            else:
                word_list_counter[lex] =  word_list_counter[lex] +  1
    except UnicodeDecodeError:
        continue

print("COUNTER")
print(word_list_counter)
print("INDEX")
print(word_list_index)