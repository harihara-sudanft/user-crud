from users.models import Task


class TaskRepository:

    @staticmethod
    def get_all_tasks():
        return Task.objects.all()

    @staticmethod
    def get_task_by_id(task_id):
        return Task.objects.get(id=task_id)

    @staticmethod
    def create_task(data):
        return Task.objects.create(**data)