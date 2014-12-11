import redis
from redis_search.indexer import Indexer

def index_repo(content):
	conn=redis.Redis()
	docid = content['id']
	items=[]
	items.extend([content['title']])
	Indexer.absolute_index(conn,docid,items)
	repo_full_content = content['title'] + " " +content['desc']
	Indexer.index_document(conn,docid,repo_full_content)

