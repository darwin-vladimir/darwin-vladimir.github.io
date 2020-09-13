from django.shortcuts import render

def home_view(request):
    return render(request,'base_admin.html',{
    #context
    })


def index_view(request):
    return render(request,'index.html',{
    #context
    })
