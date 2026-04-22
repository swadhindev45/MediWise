from django import forms
from .models import Review,Appointment
from datetime import date, timedelta

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['name','rating','comment']

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['hospital', 'patient_name', 'email', 'date']


    def clean_date(self):
        selected_date = self.cleaned_data['date']
        tomorrow = date.today() + timedelta(days=1)

        if selected_date < tomorrow:
            raise forms.ValidationError("Appointment must be from tomorrow onwards.")

        return selected_date
