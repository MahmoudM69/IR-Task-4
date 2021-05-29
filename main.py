try:
    from win_unicode_console import enable
    enable()
except ImportError:
    pass
import re
import nltk
from arabic_reshaper import ArabicReshaper
from langdetect import detect
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


configuration = {
    'delete_harakat': True,
    'support_ligatures': True,
    'RIAL SIGN': True,
}
reshaper = ArabicReshaper(configuration=configuration)

# Read Doc
with open("Doc1.txt", encoding="utf-8") as D1:
    D1 = D1.read()

D1 = reshaper.reshape(D1)

print('')
print('Your text:\r\n')
print(D1)

# Language detector
lang = detect(D1)
if lang == "en":
    lang = 'english'
elif lang == "ar":
    lang = 'arabic'
elif lang == "fr":
    lang = 'french'
elif lang == "de":
    lang = 'german'

# Remove punctuation
D1 = re.sub(r'[^\w\s]', '', D1)

# Reduce all letters to lower case
D1 = D1.lower()

# with using tokens. ps: Arabic can not be tokenized by nltk
nltk.download('punkt')
D1 = word_tokenize(D1, ('english' if lang == 'arabic' else lang))

# Importing stopwords
nltk.download('stopwords')
stop_words = set(stopwords.words(lang))

# Remove stop words
result = [i for i in D1 if not i in stop_words]

# Sorting
# result.sort()

# Printing
print('')
print('Your text after compiling:\r\n')
print(result)
