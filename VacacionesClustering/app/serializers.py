from rest_framework.serializers import ModelSerializer
from .models import Lugar
  
class LugarSerializer(ModelSerializer):
    class Meta:
        model = Lugar
        fields = ('id', 'latitud', 'longitud', 'nombre', 'clusters')

