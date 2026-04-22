from django.core.management.base import BaseCommand
from hospitals.models import Hospital, Specialization


class Command(BaseCommand):
    help = 'Seed database with hospitals'

    def handle(self, *args, **kwargs):

        hospitals_data = [

            # 🟢 ODISHA
            {"name": "AIIMS Bhubaneswar", "location": "Bhubaneswar", "rating": 4.7, "cost_index": 1, "specializations": "General"},
            {"name": "KIMS Hospital", "location": "Bhubaneswar", "rating": 4.5, "cost_index": 2, "specializations": "Multi-specialty"},
            {"name": "SUM Ultimate Hospital", "location": "Bhubaneswar", "rating": 4.4, "cost_index": 2, "specializations": "Cardiology"},
            {"name": "Apollo Hospital Bhubaneswar", "location": "Bhubaneswar", "rating": 4.6, "cost_index": 3, "specializations": "Multi-specialty"},
            {"name": "Care Hospitals", "location": "Bhubaneswar", "rating": 4.3, "cost_index": 2, "specializations": "Neurology"},

            # 🔵 DELHI
            {"name": "AIIMS Delhi", "location": "New Delhi", "rating": 4.8, "cost_index": 1, "specializations": "General"},
            {"name": "Fortis Escorts", "location": "New Delhi", "rating": 4.6, "cost_index": 3, "specializations": "Cardiology"},
            {"name": "Max Super Specialty", "location": "New Delhi", "rating": 4.5, "cost_index": 3, "specializations": "Multi-specialty"},
            {"name": "BLK Hospital", "location": "New Delhi", "rating": 4.4, "cost_index": 3, "specializations": "Orthopedics"},
            {"name": "Safdarjung Hospital", "location": "New Delhi", "rating": 4.2, "cost_index": 1, "specializations": "General"},

            # 🟣 MUMBAI
            {"name": "Lilavati Hospital", "location": "Mumbai", "rating": 4.5, "cost_index": 3, "specializations": "Multi-specialty"},
            {"name": "Kokilaben Hospital", "location": "Mumbai", "rating": 4.6, "cost_index": 3, "specializations": "Oncology"},
            {"name": "Tata Memorial Hospital", "location": "Mumbai", "rating": 4.7, "cost_index": 1, "specializations": "Cancer"},
            {"name": "Nanavati Hospital", "location": "Mumbai", "rating": 4.4, "cost_index": 2, "specializations": "Cardiology"},
            {"name": "Fortis Hospital Mumbai", "location": "Mumbai", "rating": 4.3, "cost_index": 2, "specializations": "General"},

            # 🟠 CHENNAI
            {"name": "Apollo Hospital Chennai", "location": "Chennai", "rating": 4.7, "cost_index": 3, "specializations": "Multi-specialty"},
            {"name": "MIOT Hospital", "location": "Chennai", "rating": 4.5, "cost_index": 3, "specializations": "Orthopedics"},
            {"name": "Fortis Malar", "location": "Chennai", "rating": 4.4, "cost_index": 2, "specializations": "Cardiology"},
            {"name": "Global Hospital", "location": "Chennai", "rating": 4.3, "cost_index": 2, "specializations": "Transplant"},
            {"name": "Sankara Nethralaya", "location": "Chennai", "rating": 4.8, "cost_index": 1, "specializations": "Eye"},

            # 🔴 HYDERABAD
            {"name": "Yashoda Hospital", "location": "Hyderabad", "rating": 4.6, "cost_index": 3, "specializations": "Multi-specialty"},
            {"name": "KIMS Hyderabad", "location": "Hyderabad", "rating": 4.5, "cost_index": 2, "specializations": "Cardiology"},
            {"name": "Care Hospital Hyderabad", "location": "Hyderabad", "rating": 4.4, "cost_index": 2, "specializations": "Neurology"},
            {"name": "Apollo Hyderabad", "location": "Hyderabad", "rating": 4.6, "cost_index": 3, "specializations": "Multi-specialty"},
            {"name": "AIG Hospital", "location": "Hyderabad", "rating": 4.5, "cost_index": 3, "specializations": "Gastroenterology"},

            # 🟡 BANGALORE
            {"name": "Manipal Hospital", "location": "Bangalore", "rating": 4.6, "cost_index": 3, "specializations": "Multi-specialty"},
            {"name": "Narayana Health", "location": "Bangalore", "rating": 4.5, "cost_index": 2, "specializations": "Cardiology"},
            {"name": "Fortis Bangalore", "location": "Bangalore", "rating": 4.4, "cost_index": 2, "specializations": "General"},
            {"name": "Columbia Asia", "location": "Bangalore", "rating": 4.3, "cost_index": 2, "specializations": "General"},
            {"name": "Sakra World Hospital", "location": "Bangalore", "rating": 4.5, "cost_index": 3, "specializations": "Orthopedics"},

            # 🔵 KOLKATA
            {"name": "Apollo Gleneagles", "location": "Kolkata", "rating": 4.6, "cost_index": 3, "specializations": "Multi-specialty"},
            {"name": "AMRI Hospital", "location": "Kolkata", "rating": 4.4, "cost_index": 2, "specializations": "Cardiology"},
            {"name": "Fortis Kolkata", "location": "Kolkata", "rating": 4.3, "cost_index": 2, "specializations": "General"},
            {"name": "Peerless Hospital", "location": "Kolkata", "rating": 4.2, "cost_index": 1, "specializations": "General"},
            {"name": "Medica Superspecialty", "location": "Kolkata", "rating": 4.5, "cost_index": 2, "specializations": "Neurology"},
        ]

        for data in hospitals_data:
            spec_name = data.pop("specializations")

            spec_obj, _ = Specialization.objects.get_or_create(name=spec_name)

            hospital, created = Hospital.objects.get_or_create(**data)

            hospital.specializations.set([spec_obj])

        self.stdout.write(self.style.SUCCESS("✅ 35+ Hospitals added successfully!"))