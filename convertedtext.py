from bs4 import BeautifulSoup
import requests

result = requests.get('http://pythonforbeginners.com')
# add Davids root after the file is uploaded to repository

data = result.text

soup = BeautifulSoup(data, 'html.parser')

# soup = BeautifulSoup(data)

mydivs = soup.findAll("div", {"class" : "post-bodycopy cf"})

print mydivs



#for paragraph in mydivs:
 # print(paragraph)


#heading = soup.select('h2.post-body-copy').text.strip()
#print(heading)

# this is assuming that the PDF file has been parsed and converted to an HTML format and we're going to be looking for
# different heading styles to separate the sections





#