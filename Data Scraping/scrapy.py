from bs4 import BeautifulSoup
from urllib.request import urlopen, Request

# trial
header = {
    #'User-Agent': 'some user'
}
page_url = 'www.google.com'
request = Request(page_url, header = header)
url = urlopen(request)
soup = BeautifulSoup(url, 'html.parser')