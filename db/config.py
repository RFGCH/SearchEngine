from pymongo import MongoClient

bucket_name = 'search-engine-bd-2'
client = MongoClient('localhost', 27017)  
db = client['search_engine_db']