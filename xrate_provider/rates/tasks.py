from xrate_provider.celery import app 
from rates.services import update_rates

@app.task(name="update_rates_task")
def update_rates_task(self):
    update_rates()

# app.tasks.register(update_rates_task)