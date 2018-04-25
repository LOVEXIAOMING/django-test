from django.shortcuts import render

# Create your views here.
def girls(request):
	return render(request,'girls.html')
def lmm(request):
	return render(request,'lmm.html')