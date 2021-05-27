# serializers.py
from rest_framework import serializers
from django.utils.crypto import get_random_string
from .models import MyUuid

class MyUuidSerializer(serializers.HyperlinkedModelSerializer):
    generate_id = get_random_string(length=32)
    create_uuid = MyUuid.objects.create(uuid=generate_id)
    print(generate_id)
    class Meta:
        model = MyUuid
        fields = ('uuid', 'created')