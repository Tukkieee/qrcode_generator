import base64
import json
import qrcode
from io import BytesIO
from django.db import models

def qr_image_path(instance, filename):
    return f"qr_codes/{filename}"

class QRCodeData(models.Model):
    location = models.CharField(max_length=255)
    gps_coordinates = models.CharField(max_length=255, blank=True, null=True)
    item_name = models.CharField(max_length=255)
    description = models.TextField()
    qr_code = models.ImageField(upload_to=qr_image_path, blank=True, null=True)

    def save(self, *args, **kwargs):
        # Structure the data as a JSON object
        data_object = {
            "location": self.location,
            "gps_coordinates": self.gps_coordinates,
            "item_name": self.item_name,
            "description": self.description
        }

        # Convert object to JSON string and encode it in Base64
        json_data = json.dumps(data_object)
        encoded_data = base64.b64encode(json_data.encode()).decode()

        # Generate QR code
        qr = qrcode.make(encoded_data)
        buffer = BytesIO()
        qr.save(buffer, format="PNG")

        # Save QR code to media folder
        file_name = f"{self.item_name.replace(' ', '_')}_qr.png"
        self.qr_code.save(file_name, buffer, save=False)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.item_name
