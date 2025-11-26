# hr_app/serializers.py
from rest_framework import serializers
from .models import JobOpening, Candidate, Application

class JobOpeningSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobOpening
        fields = '__all__'

class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = '__all__'

# Serializer untuk tabel perantara Application
class ApplicationSerializer(serializers.ModelSerializer):
    # Field read-only untuk menampilkan nama daripada hanya ID FK
    candidate_name = serializers.ReadOnlyField(source='candidate.full_name')
    job_title = serializers.ReadOnlyField(source='job_opening.title')

    class Meta:
        model = Application
        fields = ['id', 'candidate', 'candidate_name', 'job_opening', 'job_title', 
                  'application_date', 'status', 'notes']

