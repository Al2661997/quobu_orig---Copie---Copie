from django.db import models


class Auteur(models.Model):
    name = models.CharField(max_length = 30)
    # avatar = 

    def __str__(self):
        return self.name



class Question(models.Model):
    question = models.TextField(max_length = 250)
    auteur = models.CharField(max_length = 34)
    date = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.question


class Reponse(models.Model):
    body = models.TextField(max_length = 300)
    auteur = models.CharField(max_length = 34)
    date = models.DateTimeField(auto_now = True)
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.body

    
class Like(models.Model):
    reponse = models.ForeignKey(Reponse,related_name = 'likes', on_delete = models.CASCADE)
    likes = models.IntegerField(default = 0)
    dislikes = models.IntegerField(default = 0)

    def __str__(self):
        return str(self.reponse)



        








