from rest_framework import serializers
from .models import Note

class NoteSerializer(serializers.Serializer):

    # class Meta:
    #     model = Note
    #     fields = ('created_time', 'title', 'context')
    
    #created_time = serializers.IntegerField(read_only=True)
    id = serializers.IntegerField(read_only=True)
    created_time = serializers.DateTimeField(read_only=True)
    title = serializers.CharField(max_length=200, allow_blank=True, required=False)
    context = serializers.CharField(style={'base_template': 'textarea.html'})

    def create(self, validated_data):

        return Note.objects.create(**validated_data)

    def update(self, instance, validated_data):

        instance.title = validated_data.get('title', instance.title)
        instance.context = validated_data.get('context', instance.context)
        instance.save()

        return instance