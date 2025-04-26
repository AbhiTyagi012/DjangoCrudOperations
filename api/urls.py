from django.urls import path
from .views import CarList, CarDetail, CustomerList, CustomerDetail, BookingList, BookingDetail, AvailableCarsView

urlpatterns = [
    path('cars/', CarList.as_view()),
    path('cars/<int:pk>/', CarDetail.as_view()),
    path('customers/', CustomerList.as_view()),
    path('customers/<int:pk>/', CustomerDetail.as_view()),
    path('bookings/', BookingList.as_view()),
    path('bookings/<int:pk>/', BookingDetail.as_view()),
    path('available-cars/', AvailableCarsView.as_view()),
]