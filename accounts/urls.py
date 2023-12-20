from rest_framework import routers
#from accounts.views import CustomUserViewSet

from . import views

from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'user', views.CustomUserViewSet, basename='user')

urlpatterns = router.urls