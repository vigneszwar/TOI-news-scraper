import toi_news_scrape as ns
import urllib2
from bs4 import BeautifulSoup

url = 'https://timesofindia.indiatimes.com'
page = urllib2.urlopen(url).read()
soup = BeautifulSoup(page, 'html.parser')
soup.prettify()
link_list = soup.select('a[href$=.cms]')
import time
for link in link_list[20:30]:
    time.sleep(2)
    if link['href'].startswith('http') and not 'timesofindia' in link['href']:
        continue
    try:
        if not link['href'].startswith('http'):
            url = 'https://timesofindia.indiatimes.com' + link['href']
        else:
            url = link['href']
        print url
        obj = ns.TimesOfIndiaParser()
        obj.read_times_of_india_article(url)
        obj.print_article()
        print '-'*80
    except Exception as e:
        print e


