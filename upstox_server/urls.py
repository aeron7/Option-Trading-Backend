from rest_framework import routers
from django.conf.urls import url
from app.fn_views import getRedirectUrl, getAccessToken, getMasterContract

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/
router = routers.DefaultRouter()
urlpatterns = [
    url("redirecturl/", getRedirectUrl),
    url("accesstoken/", getAccessToken),
    url("mastercontract/", getMasterContract)
]

urlpatterns += router.urls