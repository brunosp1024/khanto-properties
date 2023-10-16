from celery import shared_task
from django.apps import apps
from datetime import datetime, timedelta
from django.core.mail import send_mail
from setup.settings import EMAIL_HOST_USER


@shared_task
def delete_items_task():
    models = apps.get_models()
    total = 0
    time_limit = datetime.now() - timedelta(hours=12)

    for model in models:
        if hasattr(model, 'deleted_at'):
            objects_to_exclude = model.dm_objects.filter(deleted_at__lte=time_limit)
            total += len(objects_to_exclude)
            objects_to_exclude.delete()

    if total > 0:
        mail_subject = 'Banco de dados atualizado.'
        message = f'Olá, Usuário<br><br>Seu banco de dados foi atualizado. \
            {total} item(ns) deletado(s) permanentemente da lixeira.<br> \
            Esse itens foram deletados há mais de 12 horas, \
            mas ficaram salvos no banco durante esse tempo para possível recuperação.<br><br> \
            att,<br>Equipe Khanto'
        to_email = 'bovodo4818@cindalle.com'
        send_mail(
            subject=mail_subject,
            message=message,
            from_email=EMAIL_HOST_USER,
            recipient_list=[to_email],
            fail_silently=True,
            html_message=message
        )
        return f'Database updated: {total} deleted item(s)'
    
    return 'No items to delete'