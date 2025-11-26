# hr_app/views.py
from rest_framework import viewsets
from .models import JobOpening, Candidate, Application
from .serializers import JobOpeningSerializer, CandidateSerializer, ApplicationSerializer

class JobOpeningViewSet(viewsets.ModelViewSet):
    queryset = JobOpening.objects.all().order_by('-posted_date')
    serializer_class = JobOpeningSerializer

class CandidateViewSet(viewsets.ModelViewSet):
    queryset = Candidate.objects.all().order_by('full_name')
    serializer_class = CandidateSerializer

class ApplicationViewSet(viewsets.ModelViewSet):
    # Prefetch related untuk mengoptimalkan pengambilan data terkait
    queryset = Application.objects.all().select_related('candidate', 'job_opening').order_by('-application_date')
    serializer_class = ApplicationSerializer

