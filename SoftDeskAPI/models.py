from accounts.models import CustomUser
from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()


class Contributor(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    #projects = models.ManyToManyField('Project', related_name='contributors')
    # foreign key to project
    projects = models.ForeignKey(Project, on_delete=models.CASCADE)


class Issue(models.Model):
    STATUS_CHOICES = [
        ('en_cours', 'En Cours'),
        ('resolu', 'Résolu'),
        ('annule', 'Annulé'),
    ]
    PRIORITY_CHOICES = [
        ('faible', 'Faible'),
        ('moyenne', 'Moyenne'),
        ('elevee', 'Élevée'),
    ]
    TAG_CHOICES = [
        ('bug', 'Bug'),
        ('tache', 'Tâche'),
        ('amelioration', 'Amélioration'),
    ]

    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='issues')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='en_cours')
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='moyenne')
    assigned_user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True)
    tag = models.CharField(max_length=20, choices=TAG_CHOICES, default='bug')

class Comment(models.Model):
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()