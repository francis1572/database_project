from django.urls import path
from . import views
from django.conf.urls import url


urlpatterns = [
	path('', views.index, name='index'),
	path('food/', views.FoodListView.as_view(), name='food'),
	path('foodType/', views.FoodTypeListView.as_view(), name='foodType'),
	path('material/', views.MaterialListView.as_view(), name='material'),
	path('AAA/', views.AAA.as_view(), name='AAA'),
	path('evaluation/', views.evaluation),
	path('order/', views.order),
	path('register/', views.register),
	path('addFood/', views.addFood),
	url(r'^food/(?P<pk>\d+)$', views.FoodDetail, name='food-detail'),
]