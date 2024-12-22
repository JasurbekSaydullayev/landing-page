from django.db import models


class Announcements(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='announcements/')
    file = models.FileField(upload_to='files/announcements/', null=True, blank=True)

    def __str__(self):
        return self.title


class Customers(models.Model):

    status_choices = (
        ('Yangi', 'yangi'),
        ('Qabul qilingan', 'qabul qilingan'),
        ('Rad etilgan', 'rad etilgan')
    )

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    status = models.CharField(max_length=100, choices=status_choices, default='Yangi')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name