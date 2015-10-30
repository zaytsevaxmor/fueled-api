from django.conf.urls import include, patterns, url
from rest_framework import routers,authtoken
from django.views.generic import TemplateView
from api.views import UserViewSet, GroupViewSet
from rest_framework_jwt.views import obtain_jwt_token

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)

urlpatterns = patterns('',
    url(r'api/v1/auth/login_form/', TemplateView.as_view(template_name='login.html')),
    url(r'api/v1/auth/login/', obtain_jwt_token),
    url(r'api/v1/', include(router.urls)),
    url(r'^.*$', TemplateView.as_view(template_name='index.html')),
)