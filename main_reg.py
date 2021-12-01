import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ

1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

python.org

321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T

EmailAddress@gmail.com
email.address@domain.net
email-123-address@my-domain.io
email-123-address@my-domain.XN--T60B56A

'''

urls = '''
https://google.com
http://www.python.org
https://youtube.com
http://new.domain.net
'''

sentence = 'Start a sentence and then bring it to an end'

# print(r'\tTab')  # r is used to get the raw string and not to interpret chars
# print('\tTab')


# pattern = re.compile('abc')  # "Compile a regular expression pattern, returning a Pattern object."
# print(type(pattern))
# matches = pattern.finditer(text_to_search)  # finds one match
# for match in matches:
#     print(match)
#     print(type(match))
# print(text_to_search[1:4])


# pattern = re.compile(r'end$')
# matches = pattern.finditer(sentence)
# for match in matches:
#     print(match)
# print(sentence[0:5], sentence[41:44])

# pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
# pattern = re.compile(r'\d{3}.\d{3}.\d{4}')
# pattern = re.compile(r'(\d{3}[-.]){2}(\d{4})')
# matches = pattern.finditer(text_to_search)
# for match in matches:
#     print(match)


# pattern = re.compile(r'(\d{3}[-.]){2}(\d{4})')
# with open('data.txt', 'r') as file:
#     contents = file.read()
#     matches = pattern.finditer(contents)
#     for match in matches:
#         print(match)
#     print(contents[102:114])



# Mr. Schafer
# Mr Smith
# Ms Davis
# Mrs. Robinson
# Mr. T
# pattern = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*')
# matches = pattern.finditer(text_to_search)
# for match in matches:
#     print(match)


# pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-]{2,63}')
# matches = pattern.finditer(text_to_search)
# for match in matches:
#     print(match)


# pattern = re.compile(r'https?://(\w+\.)?(\w+)(\.\w+)')
# matches = pattern.finditer(urls)
# for match in matches:
#     print(match)
#     print('match.group', match.group(2))

# subbed_urls = pattern.sub(r'\2\3', urls)
# print('### subbed_urls ###', subbed_urls)

# matches = pattern.findall(urls)
# print('matches', matches)


# pattern = re.compile(r'sentence')
# # matches = pattern.match(sentence)  # searches at the beginning of the string
# matches = pattern.search(sentence)
# print(matches)


# pattern = re.compile(r'start', re.IGNORECASE | re.S)
# matches = pattern.search(sentence)
# print(matches)
