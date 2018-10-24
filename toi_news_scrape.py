import urllib2
import bs4.element
from bs4 import BeautifulSoup
import dateutil.parser

#proxy_support = urllib2.ProxyHandler({"http":"www-proxy-idc.in.oracle.com:80","https":"www-proxy-idc.in.oracle.com:80" })
#opener = urllib2.build_opener(proxy_support)
#urllib2.install_opener(opener)

class TimesOfIndiaParser:
    heading = ''
    passage = ''
    time = ''
    def read_times_of_india_article(self, url):
        page = urllib2.urlopen(url).read()

        soup = BeautifulSoup(page, 'html.parser')
        soup.prettify()

        main_content = soup.find('div', class_='main-content')
        self.parse_time(main_content)
        self.heading = unicode(main_content.section.h1.arttitle.contents[0])

        contentss = main_content.find('arttextxml')

        self.contentparse(contentss)

    def parse_time(self, main_content):
        times = main_content.find_all('time')
        if len(times)!= 1:
            print 'time tag list length is not equal to 1'
        else:
            self.time = dateutil.parser.parse(times[0]['datetime']).strftime('%b %d, %y, %I:%M %p')
            

    def print_article(self):
        print self.heading
        print self.time
        print self.passage

    def contentparse(self, contents):        
            if type(contents) == bs4.element.Tag:
                if contents.name == 'br':
                    return
                if not contents.can_be_empty_element:
                    for content in contents:
                        try:
                            self.contentparse(content)
                        except Exception as e:
                            print e
                            print dir(contents)
            else:
                    if contents == u'\n':
                        self.passage += '\n'
                    else:
                        self.passage += unicode(contents.replace('\n', ' '))
                        


    

