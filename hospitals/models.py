from django.db import models

class Specialization(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class Hospital(models.Model):
    name = models.CharField(max_length=200)
    location=models.CharField(max_length=200)
    rating = models.FloatField(default=0)
    cost_index = models.IntegerField()
    specializations = models.ManyToManyField(Specialization)
    description = models.TextField()
    def __str__(self):
        return self.name

class Review(models.Model):
    hospital = models.ForeignKey(Hospital,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    rating = models.IntegerField()
    comment = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.name}-{self.hospital.name}"

class Appointment(models.Model):
    hospital = models.ForeignKey(
        Hospital,
        on_delete=models.CASCADE
    )
    patient_name = models.CharField(max_length=100)
    email = models.EmailField()
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.patient_name} - {self.hospital}"

