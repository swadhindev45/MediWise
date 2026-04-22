# 🏥 MediWise — Hospital Comparison & Appointment Booking System

## 📌 Overview

MediWise is a full-stack web application built with Django that helps users:

* Compare hospitals based on key metrics
* View detailed hospital information
* Book appointments easily
* Receive email confirmations

The goal of this project is to simulate a **real-world healthcare decision system** with clean UI and practical backend features.

---

## 🚀 Features

### 🔍 Hospital Exploration

* View list of hospitals
* Filter by specialization, rating, and cost
* Detailed hospital pages

### ⚖️ Comparison System

* Select multiple hospitals
* Compare key attributes side-by-side

### ⭐ Reviews

* Users can add reviews for hospitals
* Displays user feedback

### 📅 Appointment Booking

* Book appointments with selected hospitals
* Date validation (only future dates allowed)
* Clean and modern UI

### 📧 Email Confirmation

* Automatic email sent after booking
* Includes appointment details

### ✅ Success Feedback

* Dedicated success page
* Animated confirmation (Lottie)

---

## 🛠️ Tech Stack

* **Backend:** Django
* **Frontend:** HTML, CSS, Bootstrap
* **Database:** SQLite (can be upgraded to PostgreSQL)
* **Email Service:** Gmail SMTP
* **UI Enhancements:** Bootstrap + Lottie animations

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/mediwise.git
cd mediwise
```

---

### 2️⃣ Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

---

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Apply migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 5️⃣ Create superuser

```bash
python manage.py createsuperuser
```

---

### 6️⃣ Run server

```bash
python manage.py runserver
```

---

### 7️⃣ Access the app

* User: http://127.0.0.1:8000
* Admin: http://127.0.0.1:8000/admin

---

## 📧 Email Configuration

Update in `settings.py`:

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

EMAIL_HOST_USER = 'your_email@gmail.com'
EMAIL_HOST_PASSWORD = 'your_app_password'
```

> ⚠️ Use Gmail App Password (not your actual password)

---

## 📂 Project Structure

```
mediwise/
│
├── hospitals/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── templates/
│   └── static/
│
├── manage.py
└── db.sqlite3
```

---

## 🎯 Key Learning Outcomes

* Django models, forms, and views
* Form validation and user input handling
* Email integration in web apps
* UI/UX improvement using Bootstrap
* Building a complete end-to-end system

---

## 🚀 Future Improvements

* User authentication system
* Booking history dashboard
* REST API using Django REST Framework
* React frontend integration
* Deployment on cloud (Render / AWS)

---

## 👨‍💻 Author

**Swadhin Rout**

---

## ⭐ If you like this project

Give it a star on GitHub 🌟
