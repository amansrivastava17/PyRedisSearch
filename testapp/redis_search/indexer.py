from tokenizer import *
import redis

class Indexer():
	@classmethod	
	def absolute_index(self,conn,docid,items):
		pipeline=conn.pipeline(True)
		for item in items:
			pipeline.sadd('idx:'+item,docid)
		return len(pipeline.execute())
	@classmethod
	def index_document(self,conn,docid,content):
		words = tokenize(content)
		pipeline = conn.pipeline(True)
		for word in words:
			pipeline.sadd('idx:'+word,docid)
		return len(pipeline.execute())


