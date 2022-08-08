from django.shortcuts import render


# Create your views here.
def index(request):
        context_dict = {'text':'hello world', 'number':100}
        return render (request,'brainapp/index.html', context_dict)


def other(request):
    return render(request,'brainapp/other.html')

def relative(request):
    return render(request,'brainapp/relative_url_template.html')
