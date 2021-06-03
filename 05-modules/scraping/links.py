import urllib.request
import re


def get_links(page):
    url = f'http://127.0.0.1:5000/{page}'
    html = urllib.request.urlopen(url).read()
    links = re.findall(r'href=[\'"]?([^\'" >]+)', str(html))
    return links
queue = ['index.html']
bezochtelinks = list()
while len(queue) > 0:
    currentLink = queue.pop(0)
    links = get_links(currentLink)
    for link in links:
        if link not in bezochtelinks:
            queue.append(link)
            bezochtelinks.append(link)
print("\n".join(sorted(bezochtelinks)))
