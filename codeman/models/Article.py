from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    is_show = models.BooleanField(default=False)
    id_del = models.BooleanField(default=False)
    helped_number = models.IntegerField(blank=True, default=0) #帮助了多少人
    post_man = models.ForeignKey('codeman.User', related_name="articles",on_delete=models.CASCADE)
    group = models.ForeignKey('codeman.Group', related_name="articles", on_delete=models.CASCADE, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'codeman_articles'
        ordering = ('created_at',)