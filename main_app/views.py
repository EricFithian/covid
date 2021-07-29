from django.shortcuts import render, get_object_or_404, redirect
from .models import Test
from django.views import View

#Here are my class based views

class TestListView(View):
    def get(self, request):
        queryset = Test.objects.all()
        context = {
            'objects': queryset
        }
        return render(request, 'tests/test_list.html', context)

# Create your function views here.

def home(request):
    return render(request, 'home.html')

def symptoms(request):
    return render(request, 'symptoms.html')

def testing_lookup(request, id):
    obj = get_object_or_404(Test, id=id)
    context = {
        'object': obj
    }
    return render(request, 'tests/test_detail.html', context)

def testing_delete(request, id):
    obj = get_object_or_404(Test, id=id)
    if request.method == "POST":
        #Building this in to make sure they don't delete just by going
        obj.delete()
        return redirect('../../')
    context = {
        "object": obj
    }
    return render(request, 'tests/test_delete.html', context)

def vaccines(request):
    return render(request, 'vaccines.html')