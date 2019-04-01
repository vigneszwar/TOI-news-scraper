import pymongo

class TOIDAO(object):
    def __init__(self):
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient["NewsScrape"]
        self.toi_news_table = mydb["toi_news"]

    def insert_toi_record(self, url, heading, passage, time, author_name):
        if self.toi_news_table.find_one({"toi_url": url}):
            print 'news record already exists. Skipping insert for ', url
            return
        insert_document = {'toi_url': url, 'title':heading, 'content':passage, 'timestamp':time, 'author_name': author_name}
        self.toi_news_table.insert_one(insert_document)

    def display_all_records(self):
        for news_record in self.toi_news_table.find():
            print news_record

    def display_all_headings(self):
        for heading in self.toi_news_table.find({}, {'title':True, "_id":False}):
            print heading
