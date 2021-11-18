from django.urls import path

from . import views

app_name = 'bdaweb'
urlpatterns = [
    path("", views.home, name = "home"),
    # path("<int:id>", views.index, name="index"),
    # path("home", views.home, name = "home"),
    path('reg/',views.reg, name='reg'),
    path("<str:userid>/landingpage/", views.landingpage, name = "landingpage"),
]
