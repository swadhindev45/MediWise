from django.urls import path
from . import views

urlpatterns = [
    path('',views.hospital_list,name='hospital_list'),
    path('hospital/<int:id>/',views.hospital_detail,name='hospital_detail'),
    path('compare/',views.compare_hospitals,name='compare_hospitals'),
    path('book/',views.book_appointment,name='book_appointment'),
    path('success/',views.appointment_success,name='appointment_success'),
]