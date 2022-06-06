from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import lotto
from .crawl import crawling

# Create your views here.
def index(request):
    return HttpResponse("로또사이트에오신걸환영합니다")

def lottoview(request):
    # 데이터를 서버에 저장하는 하는 POST
    lottonumber=crawling()
    context={'lottonumber':lottonumber}
    return render(request,'pybo/lotto_list.html',context)
    

