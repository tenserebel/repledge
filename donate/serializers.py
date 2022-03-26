from rest_framework import serializers
from .models import donate

class donateSerializer(serializers.ModelSerializer):
    class Meta:
        model = donate 
        # fields = ['id','item_name','quantity','location','category']
        fields = "__all__"