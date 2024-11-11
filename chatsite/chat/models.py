from django.db import models

'''
Para atualizar novos models, comande:

```cmd
python manage.py makemigrations
python manage.py migrate
```
'''


class News(models.Model):
    nw_id = models.AutoField(primary_key=True)
    nw_date = models.DateTimeField(auto_now_add=True)
    nw_author = models.CharField(max_length=127, blank=True, null=True)
    nw_title = models.CharField(max_length=127)
    nw_resume = models.CharField(max_length=255, blank=True, null=True)
    nw_complete = models.TextField(blank=True, null=True)
    nw_views = models.IntegerField(default=0)
    nw_status = models.CharField(
        max_length=3,
        choices=[
            ('on', 'Online'),
            ('off', 'Offline')
        ],
        default='on'
    )


class Contact(models.Model):
    ct_id = models.AutoField(primary_key=True)
    ct_date = models.DateTimeField(auto_now_add=True)
    ct_name = models.CharField(max_length=127)
    ct_email = models.EmailField(max_length=127)
    ct_subject = models.CharField(max_length=127)
    ct_message = models.TextField()
    ct_status = models.CharField(
        max_length=10,
        choices=[
            ('received', 'Recebido'),
            ('readed', 'Lido'),
            ('responded', 'Respondido'),
            ('deleted', 'Apagado')
        ],
        default='received'
    )


class Register(models.Model):
    re_id = models.AutoField(primary_key=True)
    re_date = models.DateTimeField(auto_now_add=True)
    re_name = models.CharField(max_length=127)
    re_email = models.EmailField(max_length=127)
    re_birth = models.DateField()
    re_password = models.CharField(max_length=63)
    re_status = models.CharField(
        max_length=10,
        choices=[
            ('on', 'Online'),
            ('off', 'Offline'),
            ('del', 'Apagado')
        ],
        default='on'
    )
