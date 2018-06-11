import re

text_to_search=''''
helloooooo
'''

print(r'\tTab') #The r at the beginning means it's a raw string
                #Meaning python doesen't intepret it or do anything to it

pattern = re.compile(r'hello')

matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)

print(text_to_search[0:3])
