from django.shortcuts import get_object_or_404, render
from .models import Cars
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from cars.choices import max_price, MAKE, YEAR


def list_view(request):
	cars = Cars.objects.order_by('-list_date').filter(is_published=True)
	paginator = Paginator(cars, 6)
	page = request.GET.get('page')
	paged_cars = paginator.get_page(page)

	context = {
		"cars": paged_cars
	}
	return render(request, "cars/cars.html", context)



def detail_view(request, car_id):
	listing = get_object_or_404(Cars, pk=car_id)

	context = {
		'listing': listing
	}
	return render(request, "cars/car_details.html", context)




def search(request):
	queryset_list = Cars.objects.order_by('-list_date').filter(is_published=True)
	# paginator = Paginator(queryset_list, 3)
	# page = request.GET.get('page')
	# paged_cars = paginator.get_page(page)

	# keyword search
	if "keywords" in request.GET:
		keywords = request.GET['keywords']
		if keywords:
			queryset_list = queryset_list.filter(description__icontains = keywords)

	# Make search
	if "make" in request.GET:
		make = request.GET['make']
		if make:
			queryset_list = queryset_list.filter(make__iexact = make)

	# Model search
	if "model" in request.GET:
		model = request.GET['model']
		if model:
			queryset_list = queryset_list.filter(model__iexact = model)

	# price search
	if "price" in request.GET:
		price = request.GET['price']
		if (max_price):
			queryset_list = queryset_list.filter(price__range = (15000, price))

	context = {
		'max_price': max_price,
		'MAKE': MAKE,
		'YEAR':YEAR,
		'cars': queryset_list,
		'values': request.GET
	}
	return render(request, "cars/search.html", context)

