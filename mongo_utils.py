from googletrans import Translator
translator = Translator()
from pymongo import MongoClient
import pymongo
import os


def get_database():
    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING=os.environ[ 'MONGO_URL' ]
    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    client = MongoClient(CONNECTION_STRING)

    # Create the database for our example (we will use the same database throughout the tutorial
    return client['news_scrape_data']

def trasl_art(text):
   translator = Translator()
   global translated_text
   translated_text = translator.translate(text, src='bg')

def translate_collection(mong_col):
    dbname = get_database()
    col = dbname[mong_col]
    for art in col.find({ "news_text_trans": { "$exists": False }}, no_cursor_timeout=True).batch_size(1000):
        try:
          text=art['news_text']
          news_ttl=art['news_title']
          nwsln=art['news_link']
          spl_text=text.split(".")
          arr_text=[]
          for sentence in spl_text:
            try:
                tr_sentence=translator.translate(sentence, src='bg').text
                arr_text.append(tr_sentence)
            except:
                pass
          tr_text=' '.join(arr_text)
          arr_text=[]
          col.update_one({"news_link" : nwsln }, {"$set": {"news_text_trans": tr_text}})
          tr_title=translator.translate(news_ttl, src='bg').text
          col.update_one({"news_link" : nwsln }, {"$set": {"news_title_trans": tr_title}})
          for newart in col.find({"news_link" : nwsln }):
            print(newart)
        except:
            pass
# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":

    # Get the database
    dbname = get_database()
