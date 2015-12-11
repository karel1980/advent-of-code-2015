import re

data = open('day1.input','r').read()

print len(re.sub('\\)', '', data)) - len(re.sub('\\(', '', data))
