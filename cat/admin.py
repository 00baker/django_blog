from django.contrib import admin
from .models import Category
# Register your models here.
class CategoryModelAdmin(admin.ModelAdmin):
	list_display = ["name"]

	class Meta:
		model = Category
		
admin.site.register(Category, CategoryModelAdmin)
