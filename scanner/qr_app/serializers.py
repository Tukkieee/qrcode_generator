from rest_framework import serializers
from .models import QRCodeData

class QRCodeDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = QRCodeData
        fields = "__all__"
