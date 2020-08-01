from django.shortcuts import render

def index_view(request):
    return render(request, 'index.html')

def vtoroi_view(request):
    return render(request, 'vtoroi.html')

def tretii_view(request):
    return render(request, 'tretii.html')