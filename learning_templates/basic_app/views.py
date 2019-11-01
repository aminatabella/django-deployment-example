from django.shortcuts import render

def index(request):

    contextDic = {"text": "hello word", "number":3}

    return render(request, 'basic_app/index.html', contextDic)

def other(request):

    return render(request, 'basic_app/other.html')

def relative(request):

    return render(request, 'basic_app/relative_url_templates.html')
