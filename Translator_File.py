import googletrans
from googletrans import Translator
import json

translator = Translator()	//we can translater to any language using the translator function 

f = open('sample1.txt', 'r')//give the path of the text file
if f.mode == 'r':
    contents = f.read()
 
    
result = translator.translate(contents, dest='bengali') //in contents the mail text file is being loaded.
print(result.text)      				//dest containts the language to which we want to convert the text file to.
                        
