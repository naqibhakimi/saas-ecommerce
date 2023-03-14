import threading


class BackgroundTask:
    def __init__(
        self, func, *args, **kwargs
    ) -> None:
        self.func = func
        self.args = args
        self.kwargs = kwargs

    def __call__(self) -> None:
        thread = threading.Thread(target=self.func, args=self.args, kwargs=self.kwargs)
        thread.start()


class BackgroundTasks(BackgroundTask):
    def __init__(self, tasks = None):
        self.tasks = list(tasks) if tasks else []

    def add_task(
        self, func, *args, **kwargs
    ) -> None:
        task = BackgroundTask(func, *args, **kwargs)
        self.tasks.append(task)

    def __call__(self) -> None:
        for task in self.tasks:
            task()
