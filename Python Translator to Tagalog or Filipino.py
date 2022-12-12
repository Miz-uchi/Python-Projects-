# Python Translator to Tagalog/Filipino

from googletrans import Translator 

tl =  Translator()

text = input ('Insert your Text:')

res = tl.translate(text,dest='tl')

print(res.text)