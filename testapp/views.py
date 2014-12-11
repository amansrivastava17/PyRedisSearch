from django.shortcuts import render_to_response
from redis_search.search import RedisSearch
from bson.objectid import ObjectId 
import redis
from django.http import HttpResponse
from testapp.models import repos
from indexer import index_repo
from django.forms.models import model_to_dict
import datetime

def indexall(request):
	if request.method=='GET':
		content={} 
		content['title'] = request.GET.get("title","")
		content['desc'] = request.GET.get("desc","")
		content['created'] =datetime.datetime.utcnow()
		if(content['title'] !="")&(content['desc'] !=""):
			a=repos.objects.create(
				title = content['title'],
				desc = content['desc'],
				created = content['created']				
				)
			content['id']=a.id
			index_repo(content)
			return render_to_response('successful.html')
		else:
			return render_to_response('title.html')


def search(request):
	text = request.GET.get('q')
	results=RedisSearch.search_result(text)
	response=[]
	for resultid in results:
		result_obj = {}
		repo = repos.objects.get(id=ObjectId(resultid))
		result_obj['title'] = repo.title
		result_obj['created'] = repo.created
		result_obj['desc'] = repo.desc

		response.append(result_obj)
	return render_to_response('result.html',{'response':response})

def show(request):
	return render_to_response('search_form.html')
def title(request):
	return render_to_response('title.html')
def listpage(request):

	repo = repos.objects.all()
	return render_to_response('list.html',{'response':repo})
	
	
	
	



