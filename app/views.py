from django.shortcuts import render

# Create your views here.
def condition(request):
    d={'a':100,'b':500,'c':250}
    return render(request,'condition.html',context=d)
