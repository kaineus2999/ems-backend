import time
from django.conf import settings
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from django.db import transaction
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.status import HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST
from rest_framework.response import Response
from rest_framework.exceptions import (
    NotFound,
    ParseError,
    PermissionDenied,
)
from .models import Green_cards_supporter
from .serializers import Green_cards_supporterDetailSerializer, Green_cards_supporterListSerializer

class Green_cards_supporters(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get(self, request):
        all_green_cards_supporters = Green_cards_supporter.objects.all()
        serializer = Green_cards_supporterListSerializer(all_green_cards_supporters, many=True, context={"request": request},)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = Green_cards_supporterDetailSerializer(data=request.data)
        if serializer.is_valid():
                    green_cards_supporter = serializer.save(responsible_person = request.user)   
                    serializer = Green_cards_supporterDetailSerializer(green_cards_supporter, context={"request": request},)
                    return Response(serializer.data)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    
class Green_cards_supporterDetail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try: 
            return Green_cards_supporter.objects.get(pk=pk)
        except Green_cards_supporter.DoesNotExist:
            raise NotFound
    
    def get(self, request, pk):
        green_cards_supporter = self.get_object(pk)
        serializer = Green_cards_supporterDetailSerializer(green_cards_supporter, context={"request": request},)
        return Response(serializer.data)

    def put(self, request, pk):
        green_cards_supporter = self.get_object(pk)
        if green_cards_supporter.responsible_person != request.user:
            raise PermissionDenied

    def delete(self, request, pk):
        green_cards_supporter = self.get_object(pk)
        if green_cards_supporter.responsible_person != request.user:
            raise PermissionDenied
        green_cards_supporter.delete()
        return Response(status=HTTP_204_NO_CONTENT)