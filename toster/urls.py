from django.urls import path
from toster.views import index, test, result

urlpatterns = [
    path('', index),
    path('test', test),
    path('result', result),
]
