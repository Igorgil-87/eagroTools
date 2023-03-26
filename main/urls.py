from django.urls import path
from apps.car import views as car
from .views import *

urlpatterns = [
	path('', home, name='main-home'),
	path('<int:id>', home, name='main-home'),
	path('billing/', billing, name='main-billing'),
	path('allfarmersmaps/', allfarmersmaps, name='main-allfarmersmaps'),
	path('allusers/', allusers, name='main-allusers'),
	path('allnetworks/', allnetworks, name='main-allnetworks'),
	path('allfarms/', allfarms, name='main-allfarms'),
	path('farmermapdetails/', farmermapdetails, name='main-farmermapdetails'),
	path('adminmapdetails/', adminmapdetails, name='main-adminmapdetails'),
	path('editFarm/', editFarm, name='main-editFarm'),
	path('addSensor/', addSensor, name='main-addSensor'),
	path('deleteSensorNode/', deleteSensorNode, name='main-deleteSensorNode'),
	path('news/', news, name='news'),
	path('car/', car.car, name='car'),
	path('agriproject/', agriproject, name='agriproject'),
	path('deleteClusterNode/<str:clusternodeid>', deleteClusterNode, name='main-deleteClusterNode'),


]