from xrate_provider.celery import app 

@app.task(name="debug_task")
def debug_task(self):
    print(f'Request: {self.request!r}')

app.tasks.register(debug_task)