from users.repo.task_repo import TaskRepository
from users.utils.logger import logger
class TaskService:

    @staticmethod
    def get_tasks():
        logger.info("Fetching all tasks")
        return TaskRepository.get_all_tasks()

    @staticmethod
    def create_task(data):
        logger.info("Creating task")
        return TaskRepository.create_task(data)
        