from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PacienteSerializer
from .models import Paciente

class PacienteViewSet(viewsets.ModelViewSet):

    queryset = Paciente.objects.all().order_by('id')
    serializer_class = PacienteSerializer

    
