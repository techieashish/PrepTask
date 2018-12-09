from django.conf.urls import url, include
from . import views
from rest_framework.routers import DefaultRouter, url

router = DefaultRouter()
<<<<<<< HEAD
router.register(r"student", views.StudentViewSet)

urlpatterns = [
    url('^', include(router.urls)),
    url(r'^$', views.index, name="index_page"),
=======
router.register(r"university", viewset=views.UniversityView, base_name="university")
router.register(r"student", views.StudentView, base_name="student")

app_name = "learn"


urlpatterns = [
    url(r'^', include(router.urls)),
    #url(r'^$', views.index, name="index_page"),
>>>>>>> 840ea407ff60084bc65f994dd5450e0f4d75a1a6
    url(r'^query$', views.query_set_practice, name="practice")

]