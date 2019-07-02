from .serializers import imageSerializer
from rest_framework.generics import (CreateAPIView)
from image_app.models import MyImage
from image_app import models


class ImageCreateAPIView(CreateAPIView):
	serializer_class = imageSerializer
	queryset = MyImage.objects.all()
	print(MyImage)