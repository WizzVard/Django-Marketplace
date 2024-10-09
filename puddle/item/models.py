from django.contrib.auth.models import User
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)

    # This is a configurations for the model
    class Meta:
        # Override ordering of items by name
        ordering = ('name',)
        # Override the name of a class in admin iterface
        verbose_name_plural = 'Categories'

    # Override the name representation of each item in admin interface
    def __str__(self):
        return self.name


class Item(models.Model):
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    # TextField is longer than a CharField
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='item_images', blank=True, null=True)
    is_sold = models.BooleanField(default=False)
    # ForeignKey is an index in the database between this item and a user
    # on_delete - if user was deleted, all of the items will also be deleted.
    # related_name='items' - This gives you a way to query for all the items that a particular user has created.
    # For example, if User has an instance user1, you can access all items that user1 has created by running:
    # user1.items.all()  This would return a queryset of all the items related to that user.
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name