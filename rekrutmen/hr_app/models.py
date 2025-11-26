# hr_app/models.py
from django.db import models

class JobOpening(models.Model):
    title = models.CharField(max_length=255)
    department = models.CharField(max_length=100)
    status = models.CharField(max_length=50, default='Open') # Open, Closed, Filled
    posted_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

class Candidate(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    skills = models.TextField(blank=True, null=True)
    # Relasi Many-to-Many melalui model Application
    applied_jobs = models.ManyToManyField(JobOpening, through='Application', related_name='applicants')

    def __str__(self):
        return self.full_name

# Tabel Perantara (Junction Table) untuk Many-to-Many relationship
class Application(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    job_opening = models.ForeignKey(JobOpening, on_delete=models.CASCADE)
    application_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=50, default='Applied') # Applied, Reviewed, Interviewing, Hired, Rejected
    notes = models.TextField(blank=True, null=True)

    class Meta:
        unique_together = ('candidate', 'job_opening') 

    def __str__(self):
        return f"{self.candidate.full_name} applies for {self.job_opening.title}"

