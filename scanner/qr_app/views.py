from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view
# from .models import QRCodeData
from .serializers import QRCodeDataSerializer
from django.conf import settings

@api_view(["POST"])
def generate_qr(request):
    serializer = QRCodeDataSerializer(data=request.data)
    if serializer.is_valid():
        qr_instance = serializer.save()
        qr_url = request.build_absolute_uri(qr_instance.qr_code.url)
        print(qr_url)

        return Response({"message": "QR Code generated successfully!", "qr_code_url": qr_url})
    
    return Response(serializer.errors, status=400)
