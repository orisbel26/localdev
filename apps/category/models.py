from django.db import models


# Create your models here.
class Category(models.Model):
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categorys"

    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)

    views = models.IntegerField(default=0, blank=True)
    parents = models.ForeignKey(
        "self", related_name="children", on_delete=models.CASCADE, blank=True, null=True
    )

    def __str__(self):
        return self.name

    def get_view_count(self):
        views = ViewCount.objects.filter(category=self).count()
        return views


class ViewCount(models.Model):
    category = models.ForeignKey(
        Category, related_name="category_viw_count", on_delete=models.CASCADE
    )
    ip_address = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.ip_address}"
