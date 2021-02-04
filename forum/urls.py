from django.urls import path, include
from rest_framework import routers
from .api import PostViewset, SectionViewset, ThreadViewset, UserViewset
from rest_framework_simplejwt import views as jwt_views
from .views import index
from graphene_django.views import GraphQLView


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewset)
router.register(r'sections', SectionViewset)
router.register(r'posts', PostViewset)
router.register(r'threads', ThreadViewset)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', index),
    path('api/', include(router.urls)),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/token/refresh/',
         jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('silk/', include('silk.urls', namespace='silk')),
    path('graphql', GraphQLView.as_view(graphiql=True), name='graphql')
]
