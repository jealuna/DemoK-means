from rest_framework.serializers import ModelSerializer
from .models import Lugar
  
class LugarSerializer(ModelSerializer):
    class Meta:
        model = Lugar
        fields = ('id', 'latitud', 'longitud', 'nombre', 'clusters')

#class LugarListSerializer(ModelSerializer):
#    model = Lugar
#    Lugar = serializers.SerializerMethodField()

#    def get_lugar(self, obj):
#        request = self.context.get('request')
#        customer_id = request.query_params.get('customer_id', None)
#        customer_pref = CustomerPreferences.objects.filter(preference_id=obj, customer=customer_id)
#        serializer = CustomerPreferencesSerializer(customer_pref, many=True)
#        return serializer.data
        
        #def to_representation(self, instance):
        #    ret = super().to_representation(instance)
        #    # Access self.context here to add contextual data into ret
        #    ret['clusters'] = self.context['clusters']
        #    return ret
