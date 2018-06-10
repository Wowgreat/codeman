from django.db import models
'''
user-group map
'''


class UserGroup(models.Model):
    user = models.ForeignKey('codeman.User', related_name="join_groups", on_delete=models.CASCADE)
    group = models.ForeignKey('codeman.Group', related_name="users_of_group", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "多对多的关系"

    def save(self, *args, **kwargs):
        super(UserGroup, self).save(*args, **kwargs)

    class Meta:
        db_table = 'codeman_user_groups'
        unique_together = ("user", "group")
        ordering = ('created_at',)