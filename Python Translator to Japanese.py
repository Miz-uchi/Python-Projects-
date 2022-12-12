# Python Translator to Japanese 
# Python の日本語翻訳

from googletrans import Translator 

tl =  Translator()

text = input ('Insert your Text:')

res = tl.translate(text,dest='ja')

print(res.text)