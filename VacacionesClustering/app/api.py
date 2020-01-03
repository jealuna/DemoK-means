from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import serializers
import pandas as pd
from .serializers import LugarSerializer
from .models import Lugar
from app.services.clasificacion import agrupa
from app.services.visualizacion import grafica_cluster

class LugarViewSet(ModelViewSet):
    queryset = Lugar.objects.all()
    serializer_class = LugarSerializer
    
    def get_serializer(self, *args, **kwargs):
        if "data" in kwargs:
            data = kwargs["data"]
            if isinstance(data, list):
                kwargs["many"] = True
        return super(ModelViewSet, self).get_serializer(*args, **kwargs)
    
#    def get_serializer_context(self):
#       context = super().get_serializer_context()
#        context['clusters'] = 1
#        return context
    #def perform_create(self, serializer):
    #    #game = self.request.data
    #    print(serializer)
    def create(self, request, *args, **kwargs):
    #    print(1+1)
        #, context={'request': request}
        serializer = self.get_serializer(data=request.data)
        if (serializer.is_valid(raise_exception=True)):
            columnas = ['Longitud', 'Latitud', 'Nombre']
            coordenadas_df = pd.DataFrame(columns=columnas)
            idx = 0
            clusters = 0
            for modelo in serializer.validated_data:
                #print(modelo)
                longitud = modelo['longitud']
                latitud = modelo['latitud']
                nombre = modelo['nombre']
                coordenadas_df.loc[idx] = [longitud, latitud, nombre]
                idx = idx + 1
                clusters = modelo['clusters']
            if clusters > len(coordenadas_df.index):
                raise serializers.ValidationError('El número de clústers debe ser menor o igual al número de puntos')
            cluster, centros = agrupa(coordenadas_df, clusters)
            #grafica_cluster(cluster, centros)
            print(cluster)
            json = cluster.to_json(orient='records', force_ascii=False)
        ##write_serializer.is_valid(raise_exception=True)
        ##instance = self.perform_create(write_serializer)

        ##read_serializer = OrderListSerializer(instance)
        return Response(json)
        ##return Response(read_serializer.data)
