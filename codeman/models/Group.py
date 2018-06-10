from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=200, unique=True)
    intro = models.CharField(max_length=300)
    create_man_id = models.ForeignKey('codeman.User', related_name="created_groups", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    user = models.ManyToManyField(to='codeman.User', related_name='users_of_group', through='codeman.UserGroup')
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super(Group, self).save(*args, **kwargs)

    class Meta:
        db_table = 'codeman_groups'
        ordering = ('created_at',)