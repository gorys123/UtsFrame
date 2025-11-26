# hr_app/urls.py
from rest_framework.routers import DefaultRouter
from .views import JobOpeningViewSet, CandidateViewSet, ApplicationViewSet

router = DefaultRouter()
router.register(r'jobs', JobOpeningViewSet)
router.register(r'candidates', CandidateViewSet)
router.register(r'applications', ApplicationViewSet) # Endpoint untuk CRUD aplikasi spesifik

urlpatterns = router.urls
