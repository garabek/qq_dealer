from django.contrib import admin
from .models import Cars

# Register your models here.

class CarsAdmin(admin.ModelAdmin):
	list_display = ['salesman', 'title', 'make', 'model', 'year', 
					'odometer', 'engine', 'price', 'is_published']
	list_display_links = ['salesman', 'title', 'make', 'model']
	list_filter = ['salesman']
	class Meta:
		model = Cars


admin.site.register(Cars, CarsAdmin)



# list_display = ['name', 'is_mvp', 'phone', 'email', 'hire_date']
# list_display_links = ['name', 'phone', 'email']
# list_filter = ['name']
# search_fields = ['name', 'description', 'email']
# list_per_page = 5