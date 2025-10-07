from rest_framework import routers
from .views import DepartmentViewSet, DoctorViewSet, PatientViewSet, AppointmentViewSet

router = routers.DefaultRouter()
router.register('departments', DepartmentViewSet)
router.register('doctors', DoctorViewSet)
router.register('patients', PatientViewSet)
router.register('appointments', AppointmentViewSet)

urlpatterns = router.urls
