from django.urls import path


from . import views

app_name = 'cores'

urlpatterns = [
    path("", views.home, name="home")
]
