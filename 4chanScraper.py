import bs4 as bs
import urllib.request
import os

url = "https://boards.4channel.org/w/thread/2113466"
url_lookslike ='https://i.4cdn.org/w/1546209390701.png'
page = urllib.request.urlopen(url).read()
soup = bs.BeautifulSoup(page,'lxml')


my_path = '/home/andy/Desktop/' + url[-7:]
try:
    os.makedirs(my_path)
except:
    os.makedirs(my_path + '(1)')

pre_image_box = []

for links in soup.find_all('img'):
    image_source = links.get("src")

    image_source = 'https:' + image_source[:-5]

    pre_image_box.append(image_source)


print(pre_image_box[1:])
x = 0
for items in pre_image_box:
    image_name = url[-7:] + '(' + str(x) + ')'
    try:
        try:
            urllib.request.urlretrieve(items + '.png', os.path.join(my_path, image_name))
        except:
            urllib.request.urlretrieve(items + '.jpg', os.path.join(my_path, image_name))
    except:
        pass

    x += 1

