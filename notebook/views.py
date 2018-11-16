from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import viewsets

from .serializers import NoteSerializer
from .models import Note


# class NoteViewSet(viewsets.ModelViewSet):

#     queryset = Note.objects.all().order_by('-created_time')
#     serializer_class = NoteSerializer


def note_list(request):

    if request.method == 'GET':
        notes = Note.objects.all()
        # import pdb; pdb.set_trace()
        serializer = NoteSerializer(notes, many=True)
        return JsonResponse(serializer.data, safe=False)

def note_detail(request, id):

    note = get_object_or_404(Note, id=id)
    # import pdb; pdb.set_trace()

    if request.method == 'GET':
        serializer = NoteSerializer(note)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = NoteSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        note.delete()
        return HttpResponse(status=204)
    
