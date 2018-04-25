from django.shortcuts import render, HttpResponse


# Create your views here.
def index(request):
	return render(request, 'index.html')


def news(request):
	return render(request, 'news.html')


def news_data(request, year, month, day):
	return HttpResponse(year + '年' + month + '月' + day + '日')


def data(request):
	if request.method == 'GET':
		return render(request, 'data.html')
	else:
		year = request.POST.get('years',None)
		month = request.POST.get('months', None)
		day = request.POST.get('days', None)
		return HttpResponse(year + '年' + month + '月' + day + '日')


def get_post(request):
	if request.method == 'GET':
		return render(request, 'get_post.html')
	else:
		username = request.POST.get('username', None)
		password = request.POST.get('password', None)
		return HttpResponse('username: ' + username + ' password: ' + password)
