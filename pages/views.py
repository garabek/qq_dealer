from django.shortcuts import render
from django.http import HttpResponse

from cars.models import Cars
from salesmen.models import Salesman
from cars.choices import max_price, MAKE, YEAR

def index(request):
	cars = Cars.objects.order_by('-list_date').filter(is_published=True)[:3]
	context = {
		'max_price': max_price,
		'MAKE': MAKE,
		'YEAR':YEAR,
		'cars': cars
	}
	return render(request, "index.html", context)



def about(request):
	salesman = Salesman.objects.order_by('-hire_date')
	mvp_saleman = Salesman.objects.filter(is_mvp=True)
	context = {
		'salesman': salesman,
		'mvp_saleman': mvp_saleman
	}
	return render(request, "about.html", context)


# Create your views here.

