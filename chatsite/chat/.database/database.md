Para criar os modelos no Django e fazer a migração para SQLite, você pode definir os modelos no arquivo `models.py` da sua aplicação. Aqui está como você pode fazer isso:

```python
from django.db import models

class News(models.Model):
    nw_id = models.AutoField(primary_key=True)
    nw_date = models.DateTimeField(auto_now_add=True)
    nw_author = models.CharField(max_length=127, blank=True, null=True)
    nw_title = models.CharField(max_length=127)
    nw_resume = models.CharField(max_length=255, blank=True, null=True)
    nw_complete = models.TextField(blank=True, null=True)
    nw_views = models.IntegerField(default=0)
    nw_status = models.CharField(max_length=3, choices=[('on', 'On'), ('off', 'Off')], default='on')

class Contact(models.Model):
    ct_id = models.AutoField(primary_key=True)
    ct_date = models.DateTimeField(auto_now_add=True)
    ct_name = models.CharField(max_length=127)
    ct_email = models.EmailField(max_length=127)
    ct_subject = models.CharField(max_length=127)
    ct_message = models.TextField()
    ct_status = models.CharField(max_length=10, choices=[('received', 'Received'), ('readed', 'Readed'), ('responded', 'Responded'), ('deleted', 'Deleted')], default='received')
```

Depois de definir os modelos, você precisa criar e aplicar as migrações:

1. **Criar as migrações**:
   ```bash
   python manage.py makemigrations
   ```

2. **Aplicar as migrações**:
   ```bash
   python manage.py migrate
   ```

Isso criará as tabelas no banco de dados SQLite de acordo com os modelos definidos.

Você está desenvolvendo um projeto específico com essas tabelas?