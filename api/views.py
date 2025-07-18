from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from .models import (
    LandingPageContent, SliderItem,
    WhatIsTopfiytItem, TopfiytForWhoItem, Footer, 
)
from .serializers import (
    LandingPageContentSerializer, SliderItemSerializer,
    WhatIsTopfiytItemSerializer, TopfiytForWhoItemSerializer,
    FooterSerializer
)

class LandingPageContentDetail(generics.RetrieveAPIView):
    queryset = LandingPageContent.objects.all()
    serializer_class = LandingPageContentSerializer

    def get_object(self):
        return self.queryset.first()

class SliderItemList(generics.ListAPIView):
    queryset = SliderItem.objects.all().order_by('order')
    serializer_class = SliderItemSerializer

class WhatIsTopfiytItemList(generics.ListAPIView):
    queryset = WhatIsTopfiytItem.objects.all()
    serializer_class = WhatIsTopfiytItemSerializer

class TopfiytForWhoItemList(generics.ListAPIView):
    queryset = TopfiytForWhoItem.objects.all().order_by('order')
    serializer_class = TopfiytForWhoItemSerializer

class FooterView(APIView):
    def get(self, request):
        try:
            footer = Footer.objects.first()  
            if footer:
                serializer = FooterSerializer(footer)
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response({"message": "Footer bulunamadı."}, status=status.HTTP_404_NOT_FOUND)
        except Footer.DoesNotExist:
            return Response({"message": "Footer bulunamadı."}, status=status.HTTP_404_NOT_FOUND)