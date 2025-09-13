from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    category = models.CharField(max_length=20)
    
    def __str__(self):
        return self.category
    

class ToDoList(models.Model):
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, related_name="item", default="")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="users")
    content = models.CharField(max_length=255)
    date = models.DateField()
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return (f"{self.author.username} added {self.content}")
       
