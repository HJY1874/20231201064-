from django.http import Http404, HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "singlepage/index.html")

# The texts are much longer in reality, but have
# been shortened here to save space
texts = [
    "这是第一部分的内容。在实际应用中，这部分内容可能会更长，包含更多的文本信息。",
    "这是第二部分的内容。这部分展示了如何使用AJAX技术从服务器动态加载内容。",
    "这是第三部分的内容。这里演示了JavaScript History API的使用，可以更新URL而不刷新页面。"
]

def section(request, num):
    if 1 <= num <= 3:
        return HttpResponse(texts[num - 1])
    else:
        raise Http404("没有找到该部分")