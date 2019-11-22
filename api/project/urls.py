from rest_framework.routers import DefaultRouter
from app.viewsets import MetricViewSet

router = DefaultRouter()
router.register(r'metrics', MetricViewSet)

urlpatterns = router.urls
