import toi_news_scrape as ns
import urllib2
from bs4 import BeautifulSoup
import toi_dao
import traceback

base_url = 'https://timesofindia.indiatimes.com'
page = urllib2.urlopen(base_url).read()
soup = BeautifulSoup(page, 'html.parser')
soup.prettify()
link_list = soup.select('a[href$=.cms]')
import time
"""
for link in link_list:
    print '--'*80
    print 'link', link
    
    if link['href'].startswith('http') and not 'timesofindia' in link['href']:
        print 'full url hence skipping', link
        continue
    if 'videos/' in link['href']:
        print 'skipping link', link
        continue
    try:
        time.sleep(2)
        if not link['href'].startswith('http'):
            url = base_url + link['href']
        else:
            url = link['href']
            print 'The code will not parse this full link url.', url
            print 'This will be enhanced in future'
            continue
        print url
        obj = ns.TimesOfIndiaParser()
        obj.read_times_of_india_article(url)
        obj.store_it_in_db()
        print '-'*80
    except Exception as e:
        print "unable to parse this url ", link
        print e
        traceback.print_exc()
        print '--'*80



"""
toi_dao.TOIDAO().display_all_headings()
