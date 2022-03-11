from django.urls import path
from .views import CreateContact

urlpatterns = [
    path('create/', CreateContact.as_view()),
    path('edit/<int:contact_id>/', CreateContact.as_view()),
    path('delete/<int:contact_id>/', CreateContact.as_view()),
    path('list/', CreateContact.as_view()),
]
