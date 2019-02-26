from bs4 import BeautifulSoup

#Making HTML and XML content
markup = '''test values
and it's coordinates'''

results = BeautifulSoup(markup, 'lxml')

print(type(results))