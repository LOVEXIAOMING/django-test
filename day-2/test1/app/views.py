from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
	return HttpResponse('hello')
def page(request):
	a="aaaaaaaaa"
	b=[1,2,3,4,5,6]
	c={'name':'wukong','age':100}
	return render(request,'hello.html',{
		'a':a,
		'b':b,
		'c':c
	})