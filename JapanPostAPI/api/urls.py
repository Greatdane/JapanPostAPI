from rest_framework import routers
from .api import International_Parcel_Post_ViewSet, Country_Viewset

router = routers.DefaultRouter()
router.register('api/country', Country_Viewset, 'country')
router.register('api/parcelpost', International_Parcel_Post_ViewSet, 'parcelpost')

urlpatterns = router.urls