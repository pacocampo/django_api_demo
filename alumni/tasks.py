
from celery.task.schedules import crontab
from celery.decorators import periodic_task,task
from celery.utils.log import get_task_logger
from django.core.mail import send_mail as sending

logger = get_task_logger(__name__)

@task(name="send_email_per_user")
def send_email(email,user):

	sending('Hola '+user,
		"Este correo viene desde django",
		'ligorio.salgado13@gmail.com',[email])
	logger.info("Email enviado")


@periodic_task(
    run_every = (crontab()),
    name = 'send_email_per_second',
    ignore_result = True
)
def send_email_per_second():
	sending('Hola Ligorio',
		"Este correo viene desde django",
		'ligorio.salgado13@gmail.com',['lsalgadof93@gmail.com'])
	logger.info("Email enviado")
    

