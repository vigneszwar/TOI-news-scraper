import urllib2
import bs4.element
from bs4 import BeautifulSoup
import dateutil.parser
import toi_dao

proxy_support = urllib2.ProxyHandler({"http":"www-proxy-idc.in.oracle.com:80","https":"www-proxy-idc.in.oracle.com:80" })
opener = urllib2.build_opener(proxy_support)
urllib2.install_opener(opener)

class TimesOfIndiaParser:
    heading = ''
    passage = ''
    time = ''
    author_name = ''
    url = ''
    def read_times_of_india_article(self, url):
        self.url = url
        page = urllib2.urlopen(url).read()

        soup = BeautifulSoup(page, 'html.parser')
        soup.prettify()

        main_content = soup.find('div', class_='main-content')

        try:
            author = main_content.find("a", {'class':'auth_detail'})
            self.author_name = author.text
        except Exception e:
            print 'unable to parse author', str(e)

        self.parse_time(main_content)
        self.heading = unicode(main_content.section.h1.arttitle.contents[0])

        contentss = main_content.find('arttextxml')
        
        

        self.contentparse(contentss)

    def store_it_in_db(self):
        db = toi_dao.TOIDAO()
        print 'storing news ', self.url, ' in mongo db'
        print db.insert_toi_record(self.url, self.heading, self.passage, self.time, self.author_name)

    def parse_time(self, main_content):
        times = main_content.find_all('time')
        if len(times)!= 1:
            print 'time tag list length is not equal to 1'
        else:
            self.time = dateutil.parser.parse(times[0]['datetime']).strftime('%b %d, %y, %I:%M %p')
            

    def print_article(self):
        print self.heading
        print self.author_name, self.time
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
                        


    

