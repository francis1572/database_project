from django.contrib import admin

# Register your models here.
from .models import FoodType, Food, Order, Evaluation, FoodMaterial, make, FoodFeature

admin.site.register(FoodType)
admin.site.register(Food)
admin.site.register(Order)
admin.site.register(Evaluation)
admin.site.register(FoodMaterial)
admin.site.register(make)
admin.site.register(FoodFeature)