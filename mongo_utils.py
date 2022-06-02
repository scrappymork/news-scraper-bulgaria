def get_database():
    from pymongo import MongoClient
    import pymongo
    import os

    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING=os.environ[ 'MONGO_URL' ]
    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    from pymongo import MongoClient
    client = MongoClient(CONNECTION_STRING)

    # Create the database for our example (we will use the same database throughout the tutorial
    return client['news_scrape_data']
    
# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":    
    
    # Get the database
    dbname = get_database()