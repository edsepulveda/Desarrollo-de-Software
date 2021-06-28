from .models import Producto, Categoria, Orden, OrdenItem
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'



class ProductoSerializer(serializers.ModelSerializer):
    categoria = CategorySerializer()
    class Meta:
        model = Producto
        fields = '__all__'



class OrdenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orden
        fields = '__all__'

class OrdenItemSerializer(serializers.ModelSerializer):
    orden = OrdenSerializer()
    class Meta:
        model = OrdenItem
        fields = '__all__'