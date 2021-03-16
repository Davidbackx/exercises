# Write your code here
import re
def parse_link(string):
    rmatch = re.fullmatch(r'<a href="(.*)">(.*)</a>', string)
    if match:
        url, caption = match.groups()
        return (caption, url)
    else:
        return None

