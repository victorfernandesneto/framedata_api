from django.urls import path, include, re_path
from apps.framedata.views import CharacterViewSet, MoveViewSet, ListCharacterMove
from rest_framework import routers
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Framedata SF6",
      default_version='v1',
      description="Framedata for STREET FIGHTER 6",
      terms_of_service="",
      contact=openapi.Contact(email="vvfernandesneto@gmail.com"),
      license=openapi.License(name=""),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

router = routers.DefaultRouter()
router.register('characters', CharacterViewSet, basename='characters')
router.register('moves', MoveViewSet, basename='moves')

urlpatterns = [
    path('', include(router.urls)),
    path('characters/<int:pk>/moves/', ListCharacterMove.as_view()),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]