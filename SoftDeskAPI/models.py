from accounts.models import CustomUser
from django.db import models



class Project(models.Model):
    PROJECT_TYPES = [
        ('back-end', 'Back-end'),
        ('front-end', 'Front-end'),
        ('iOS', 'iOS'),
        ('Android', 'Android'),
    ]
    name = models.CharField(max_length=255)
    project_type = models.CharField(max_length=20, choices=PROJECT_TYPES)
    description = models.TextField(blank=True)
    contributors = models.ManyToManyField(CustomUser, through='Contributor', related_name='contributions')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    #is_owner = models.BooleanField(default=False)
    def __str__(self):
        return self.name

class Contributor(models.Model):
    contributor = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='contributor_relationship')
    #is_owner = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.contributor.username} - {self.project.name}"

class Issue(models.Model):
    STATUS_CHOICES = [
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
        ('cancelled', 'Cancelled'),
    ]
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]
    TAG_CHOICES = [
        ('bug', 'Bug'),
        ('task', 'Task'),
        ('improvement', 'Improvement'),
    ]
    #is_owner = models.BooleanField(default=False)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='issues')
    created_at = models.DateTimeField(auto_now_add=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='issues')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='in_progress')
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='medium')
    assigned_user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True, related_name="assigned_to")
    tag = models.CharField(max_length=20, choices=TAG_CHOICES, default='bug')

    def __str__(self):
        return f"{self.project.name} - {self.tag} - {self.priority}"

class Comment(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    #is_owner = models.BooleanField(default=False)
    issue = models.ForeignKey('Issue', on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return f"{self.issue.project.name} - {self.content}"
