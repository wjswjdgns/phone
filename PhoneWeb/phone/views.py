from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'phone/index.html')



def device(request):
    return render(request, 'phone/smartphone.html')


def hotdeal(request):
    return render(request, 'phone/hotdeal.html')



def advance(request):
    return render(request, 'phone/advance.html')




def information(request):
    return render(request, 'phone/information.html')