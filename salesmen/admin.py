from django.contrib import admin
from .models import Salesman

class SalesmanAdmin(admin.ModelAdmin):
	list_display = ['name', 'is_mvp', 'phone', 'email', 'hire_date']
	list_display_links = ['name', 'phone', 'email']
	list_filter = ['name']
	search_fields = ['name', 'description', 'email']
	list_per_page = 5
	class Meta:
		model = Salesman


admin.site.register(Salesman, SalesmanAdmin)

