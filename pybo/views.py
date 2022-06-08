from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import lotto
from .crawl import crawling
from .forms import lottoform
# Create your views here.
def index(request):
    return render(request,'pybo/home.html')

def lottoview(request):
    form=lottoform()
    # 데이터를 서버에 저장하는 하는 POST
    lottonumber=crawling()
    context={'lottonumber':lottonumber}
    return render(request,'pybo/lotto_list.html',context)

def result(request):
    amount=request.POST['amount']
    amount=int(amount)
    lottonumber=crawling(amount//1000)

    context={'lottonumber':lottonumber,'amount':amount}
    return render(request,'pybo/lotto_list.html',context)

