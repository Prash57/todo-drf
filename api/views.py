from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer
from base.models import Task

@api_view(['GET'])
def getRoutes(request):
    routes = [
        {'GET': 'api/base'},
        {'GET': 'api/base/update'},
        {'GET': 'api/base/delete'},
    ]
    return Response(routes)


@api_view(['GET'])
def getTasks(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)

    return Response(serializer.data)


@api_view(['POST'])
def createTask(request):
    serializer = TaskSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def updateTask(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=task, data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def deleteTask(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()

    return Response('Item succsesfully delete!')
