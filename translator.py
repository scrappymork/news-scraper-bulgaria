import mongo_utils
import re
import time

dbname = mongo_utils.get_database()
cols=dbname.list_collection_names()
for collection in cols:
    try:
       print(collection)
       mongo_utils.translate_collection(collection)
    except:
        pass
