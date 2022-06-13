import re

#with open(r'zen.txt', 'r') as f:
    #f.readlines()
    #matches = re.findall('beautiful', f, re.IGNORECASE)

line = 'Beautiful is better than ugly.'
matches = re.findall('beautiful', line, re.IGNORECASE)
print(matches)

zen = """
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""

m = re.findall('^If', zen, re.MULTILINE)
print(m)

string = 'Two too.'
m2 = re.findall('t[ow]o', string, re.IGNORECASE)
print(m2)


#matching digits
line_dig = '123?34 hello?'
m3 = re.findall('\d', line_dig, re.IGNORECASE)
print(m3)


#matching all of the strings
t = '__one__ __two__ __three__'
results = re.findall('__.*?__', t)
for match in results:
    print(match)
