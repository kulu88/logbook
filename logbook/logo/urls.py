from django.urls import path


from . import views

app_name = 'logo'

urlpatterns = [
    path('', views.logbook, name='logbook'),
    path('summary/', views.summary, name='summary'),
    path('add_flight/', views.add_flight, name='add_flight'),
    path('update_flight/<int:pk>/', views.update_flight, name='update_flight'),
    path('delete_flight/<int:pk>/', views.delete_flight, name='delete_flight'),
    path('flight_detail/<int:pk>/', views.flight_detail, name='flight_detail'),
    path('aircraft_list/', views.aircraft, name = 'aircraft_list'),
    path('delete_aircraft/<int:pk>/', views.delete_aircraft, name = 'delete_aircraft'),
    path('update_aircraft/<int:pk>/',views.update_aircraft, name= 'update_aircraft'),
    path('people/', views.people, name ="people"),
    path('delete_person/<int:pk>/', views.delete_person, name = 'delete_person'),
    path('airport_list/', views.airport, name ="airport_list"),
    path('delete_airport/<int:pk>/', views.delete_airport, name = 'delete_airport'),
    path('update_airport/<int:pk>/', views.update_airport, name= 'update_airport'),
]