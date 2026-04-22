import threading
from django.db.models import Avg
from django.shortcuts import render,get_object_or_404,redirect
from .models import Hospital,Specialization,Appointment
from .forms import ReviewForm,AppointmentForm
from django.core.mail import send_mail

def hospital_list(request):
    hospitals = Hospital.objects.all().order_by('-rating')

    #Filter by specialization
    spec = request.GET.get('spec')
    if spec:
        hospitals = hospitals.filter(specializations__name=spec)
    
    #Filter by rating !
    rating = request.GET.get('rating')
    if rating:
        hospitals = hospitals.filter(rating__gte=rating)

    # Filter by cost
    cost = request.GET.get('cost')
    if cost:
        hospitals = hospitals.filter(cost_index__lte=cost)

    specializations = Specialization.objects.all()

    return render(request,'hospitals/list.html',{
        'hospitals':hospitals,
        'specializations':specializations})

def hospital_detail(request,id):
    hospital = get_object_or_404(Hospital,id=id)
    reviews = hospital.review_set.all()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.hospital = hospital
            review.save()

            avg_rating = hospital.review_set.aggregate(Avg('rating'))['rating__avg']
            hospital.rating = avg_rating
            hospital.save
            
            form = ReviewForm()
    else:
        form = ReviewForm()
        
    return render(request,'hospitals/detail.html',{
        'hospital':hospital,
        'reviews':reviews,
        'form':form})

def compare_hospitals(request):
    ids = request.GET.getlist('compare')
    if not ids:
        return render(request,'hospitals/compare.html',{
        'error': 'Please select atleast one hospital'})
    if len(ids)>3:
        return render(request,'hospitals/compare.html',{
        'error':'You can compare maximum 3 hospitals !'    
        })
    hospitals = Hospital.objects.filter(id__in=ids).prefetch_related('specializations')
    
    return render(request,'hospitals/compare.html',{
        'hospitals':hospitals,
    })

from .models import Hospital

from .forms import AppointmentForm

def book_appointment(request):
    if request.method == "POST":
        form = AppointmentForm(request.POST)

        if form.is_valid():
            appointment = form.save()
            subject="MediWise Appointment Confirmation",
            message = f"""
            Hi {appointment.patient_name},

            Your appointment has been successfully confirmed.

            Details:
            Hospital: {appointment.hospital.name}
            Date: {appointment.date}

            If you did not request this appointment, please ignore this email.

            Thank you for choosing MediWise.

            Regards,
            MediWise Team
            """

            threading.Thread(
                target=send_email_async,
                args=(subject, message, appointment.email)
            ).start()

            return redirect('appointment_success')
    else:
        form = AppointmentForm()

    hospitals = Hospital.objects.all()

    return render(request, 'hospitals/book_appointment.html', {
        'form': form,
        'hospitals': hospitals
    })
        
def appointment_success(request):
    return render(request,'hospitals/appointment_success.html')

def send_email_async(subject, message, recipient): # Helper function for the async email(synchronize)
    try:
        send_mail(
            subject,
            message,
            "MediWise <mediwise.appco@gmail.com>",  
            [recipient],
            fail_silently=True,
        )
    except Exception as e:
        print("Email failed:", e)