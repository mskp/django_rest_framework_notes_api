from .serializer import NoteSerializer
from .models import Note
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


# This view handles fetching and creating notes
@api_view(['GET', 'POST', 'DELETE'])
def note_view(req) -> Response:
    try:
        notes = Note.objects.all()  # To change
        match req.method:
            case 'GET':
                # fetch the data
                serializer = NoteSerializer(notes, many=True)
                return Response(serializer.data)

            case 'POST':
                # create new note
                title = req.data.get('title')
                content = req.data.get('content')

                serializer = NoteSerializer(
                    data={'title': title, 'content': content})

                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                
            case 'DELETE':
                # delete all notes
                notes.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            
            case '_':
                return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    except Exception as e:
        print(e)
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# This view handle fetching, updating and deleting the note
@api_view(['GET', 'PUT', 'DELETE'])
def note_detail_view(req, note_id: int) -> Response:
    try:
        note = Note.objects.get(pk=note_id)

        match req.method:
            case 'GET':
                serializer = NoteSerializer(note)
                return Response(serializer.data)

            case 'PUT':
                # update the note
                title = req.data.get('title')
                content = req.data.get('content')
                serializer = NoteSerializer(
                    note, data={'title': title, 'content': content})

                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            case 'DELETE':
                # delete the note
                note.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            
            case '_':
                return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    except Note.DoesNotExist:
        return Response({'message': f'Note with id {note_id} does not exist'}, status=status.HTTP_404_NOT_FOUND)

    except Exception as e:
        print(e)
        return Response(status.HTTP_500_INTERNAL_SERVER_ERROR)
