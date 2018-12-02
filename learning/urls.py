from django.conf.urls import url, include
from . import views
from rest_framework.routers import DefaultRouter
app_name = "learn"

router = DefaultRouter()
router.register(r"student/", views.StudentViewSet)

urlpatterns = [
    url('', include(router.urls)),
    url(r'^$', views.index, name="index_page"),
    url(r'^query$', views.query_set_practice, name="practice")

]