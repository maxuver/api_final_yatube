from django.urls import include, path
from rest_framework.routers import DefaultRouter
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf.urls import url
from rest_framework import permissions

from .views import PostViewSet, GroupViewSet, CommentViewSet, FollowViewSet


app_name = 'api'

router_v1 = DefaultRouter()

router_v1.register('posts', PostViewSet)
router_v1.register('groups', GroupViewSet)
router_v1.register('follow', FollowViewSet, basename='follow')
router_v1.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)

urlpatterns = [
    path('v1/', include('djoser.urls.jwt')),
    path('v1/', include(router_v1.urls)),
]


schema_view = get_schema_view(
    openapi.Info(
        title="Yatube API",
        default_version='v1',
        description="Документация для приложения API проекта Yatube",
        contact=openapi.Contact(email="name@domain.ru"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns += [
    url(r'^v1/redoc/$', schema_view.with_ui('redoc', cache_timeout=0),
        name='schema-redoc'),
]
