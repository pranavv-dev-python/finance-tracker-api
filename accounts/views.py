from rest_framework import generics
from .serializers import  RegisterSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated 

class Registeruser(generics.CreateAPIView):
    
    serializer_class = RegisterSerializer
    permission_classes  = []


class profile(APIView):
    permission_classes = [IsAuthenticated]
    def get(self , request ):
        return Response({
            "username": request.user.username ,
            "email": request.user.email ,
        })
    

