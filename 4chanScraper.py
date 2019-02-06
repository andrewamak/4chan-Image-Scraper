import bs4 as bs
import urllib
from urllib.request import Request, urlopen
import os

# example url: url = "https://boards.4channel.org/w/thread/2113466"
#put in a 4chan thread url for bs to read
url = input('Please enter a 4chan URL: ')
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
page = urllib.request.urlopen(req).read()
soup = bs.BeautifulSoup(page,'lxml')

#creating a path onto the desktop named with the thread ID number
my_path = '/home/andy/Desktop/' + url[-7:]
os.makedirs(my_path)

#creating an empty list for the src to fill up
image_box = []

#acquiring the images with their sources and appending them into the 'image_box'
for links in soup.find_all('img'):
    image_source = links.get("src")
    image_source = 'https:' + image_source[:-5]
    image_box.append(image_source)

#the x is for nomenclature. the try/except clauses are for differentiating between jpg/png file types. 
x = 0
for items in image_box:
    image_name = url[-7:] + '(' + str(x) + ')'
    try:
        try:
            urllib.request.urlretrieve(items + '.png', os.path.join(my_path, image_name))
        except:
            urllib.request.urlretrieve(items + '.jpg', os.path.join(my_path, image_name))
    except:
        pass

    x += 1

print('Done')
