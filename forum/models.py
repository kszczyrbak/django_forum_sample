from django.db import models
# Create your models here.


class Section(models.Model):
    name = models.CharField(max_length=50)
    section_logo = models.TextField()

    def __str__(self):
        return f"Section: {self.name}"


class User(models.Model):
    username = models.CharField(max_length=255)
    avatar = models.TextField()
    about = models.TextField()
    signature = models.TextField()
    followed_threads = models.ManyToManyField(
        "Thread", related_name="following_users", blank=True)

    def __str__(self):
        return f"User: {self.username}"


class Thread(models.Model):
    title = models.CharField(max_length=50)
    section = models.ForeignKey(
        Section, related_name="threads", on_delete=models.CASCADE)
    createdBy = models.ForeignKey(
        User, related_name="threads", on_delete=models.CASCADE)

    def __str__(self):
        return f"Thread: {self.title}"


class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    thread = models.ForeignKey(
        Thread, related_name="posts", on_delete=models.CASCADE)
    createdBy = models.ForeignKey(
        User, related_name="posts", on_delete=models.CASCADE)

    def __str__(self):
        return f"Post: {self.title}"
