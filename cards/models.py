from django.db import models

# Create your models here.
class Subject(models.Model):
  subject = models.CharField(max_length=100, null=False)

  def __str__(self):
    return self.subject

  def save_subject(self):
    self.save()

  @classmethod
  def delete_subject(cls, id):
    cls.objects.filter(id=id).delete()

  @classmethod
  def update_subject(cls, id, updated):
    cls.objects.filter(id=id).update(subject=updated)

class Flashcard(models.Model):
  title = models.CharField(max_length=200, null=False)
  body = models.CharField(max_length=1000, null=False)
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now_add=True)
  subjects = models.ForeignKey(Subject, null=False, on_delete=models.CASCADE)

  def __str__(self):
    return self.title

  def save_flashcard(self):
    self.save()

  @classmethod
  def delete_flashcard(cls, id):
    cls.objects.filter(id=id).delete()

  @classmethod
  def update_flashcard(cls, id, update_body):
    cls.objects.filter(id=id).update(body=update_body)