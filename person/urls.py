from django.urls import path
from person.views import index, search, filter_by_country, filter_by_city, chart, detail_filter_view, detail_view


urlpatterns = [
	path('', index, name='index'),
	path('person/<str:person_name>/', detail_view, name='detail_view'),
	path('search/', search, name="search"),
	path('search_filter/', detail_filter_view, name="search_filter"),
	path('country/<str:country_name>/', filter_by_country, name="filter_by_country"),
	path("city/<str:city_name>/", filter_by_city, name="filter_by_city"),
	path('chart/', chart, name='chart'),
]