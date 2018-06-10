from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    email = models.CharField(max_length=100,unique=True)
    password = models.CharField(max_length=100)
    intro = models.CharField(max_length=300, blank=True, default='')
    avatar = models.CharField(max_length=200, blank=True, default='http://www.sucaijishi.com/uploadfile/2016/0203/20160203022635285.png')
    occupation = models.CharField(max_length=100, blank=True, default='保密')
    is_show_location = models.BooleanField(default=False)
    company_or_school = models.CharField(max_length=100, blank=True, default='保密')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    highlighted = models.TextField()

    groups = models.ManyToManyField(to="codeman.Group", related_name="join_groups", through='codeman.UserGroup')

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)

    class Meta:
        db_table = 'codeman_users'
        ordering = ('created_at',)