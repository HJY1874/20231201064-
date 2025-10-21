from django.http import Http404, HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "singlepage/index.html")

# The texts are much longer in reality, but have
# been shortened here to save space
texts = [
    "侯靖宇+20231201064",
    "侯靖宇+20231201064",
    "侯靖宇+20231201064"
]

def section(request, num):
    if 1 <= num <= 3:
        return HttpResponse(texts[num - 1])
    else:
        raise Http404("没有找到该部分")