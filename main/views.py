# from django.shortcuts import render


# # Create your views here.
# def home(request):
from django.shortcuts import render
from django.htpp import HttpResponse
from.forms import rainfallforms


def contact(request):

form= contactform(request.post)
if form.is_valid():
  measurement=form.cleaned_data{'measurement'}
    
    print(measurement)

  return render(request,'form.html',{'form':form})

  def snippest_details(request):
    return render(request, 'main/index.html')