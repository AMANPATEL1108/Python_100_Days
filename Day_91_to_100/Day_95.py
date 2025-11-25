import re

pattern=r'[A-Z]+yclone'
text='''
Google LLC is an American multinational 
technology corporation focused on information technology, online 
advertising, search engine technology, email, cloud computing, 
software, quantum computing, e-commerce,Dyclone Cyclone consumer electronics, and 
artificial intelligence (AI).[9] It has been referred to as "the most 
powerful company in the world" by the BBC,[10] and is one of the world's
 most valuable brands.[11][12][13] Google's parent company Alphabet Inc.
   has been described as a Big Tech company.
'''

# match=re.search(pattern,text)
# print(match)

matches=re.finditer(pattern,text)

for match in matches:
    print(match.span())
    print(text[match.span()[0]:
    match.span()[1]])