from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

from . import util


def index(request):
    if request.method == 'POST':
        pass
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def get_page_details(request, title):
    entry = util.get_entry(title)

    if not entry:
        return render(request, "404-page/index.html")
    
    return render(request, "encyclopedia/wiki.html", {
        "title" : title,
        "entry" : entry,
        "entries": util.list_entries()
    })

def search(request):
    query = request.GET.get('q', '')

    entry = util.get_entry(query.lower())

    result = [entries for entries in util.list_entries() if query in entries]

    print(result)

    if entry:

        return render(request, "encyclopedia/wiki.html", {
            "title" : query,
            "entry" : entry,
            "entries": util.list_entries()
        })
    
    else:

        return render(request, "encyclopedia/search_result.html", {
            'query' : query,
            'result' : result
        })
    
def create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')

        util.save_entry(title, content)

        return HttpResponseRedirect(reverse('index'))

    return render(request, 'encyclopedia/create.html')

    
    

