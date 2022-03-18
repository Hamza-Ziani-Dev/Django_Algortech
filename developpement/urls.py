from django.urls import path
from developpement import views
app_name='developpement'
urlpatterns = [
    path('developpement/', views.developpement, name='developpement')
]