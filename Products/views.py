from django.shortcuts import render
from .models import Products
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def shop1(request):	
	product_list = Products.objects.all().order_by('uptime')
	page = request.GET.get('page', 1)
	paginator = Paginator(product_list, 9)
	try:
		products = paginator.page(page)
	except PageNotAnInteger:
		products = paginator.page(1)
	except EmptyPage:
		products = paginator.page(paginator.num_pages)
	return render(request,'shop1.html',{'detail':products})
