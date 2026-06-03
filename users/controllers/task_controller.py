from rest_framework.views import APIView
from rest_framework.response import Response

from users.services.task_service import TaskService
from users.serializers import TaskSerializer


class TaskView(APIView):

    def get(self, request):
        tasks = TaskService.get_tasks()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TaskSerializer(data=request.data)

        if serializer.is_valid():
            TaskService.create_task(serializer.validated_data)

            return Response({
                "message": "Task Created Successfully"
            })

        return Response(serializer.errors)