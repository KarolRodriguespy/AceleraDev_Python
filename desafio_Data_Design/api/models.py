from django.db import models


class User(models.Model):
    name = models.CharField('name', max_length=50)
    last_login = models.DateTimeField('Last Login', auto_now=True)
    email = models.EmailField('email', max_length=254)
    password = models.CharField('password', max_length=50)

    def __str__(self):
        return self.name


class Agent(models.Model):
    name = models.CharField('name', max_length=50)
    status = models.BooleanField(default=False)
    env = models.CharField('env', max_length=20)
    version = models.CharField('version', max_length=5)
    address = models.CharField('address', max_length=39)

    def __str__(self):
        return self.name

class Event(models.Model):
    level = models.CharField('level', max_length=20)
    data = models.TextField('data')
    arquivado = models.BooleanField(default=False)
    date = models.DateTimeField('date', auto_now_add=True)

    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.deletion.CASCADE)


class Group(models.Model):
    name = models.CharField('name', max_length=50)

    def __str__(self):
        return self.name


class GroupUser(models.Model):
    group = models.ForeignKey(
        Group,
        on_delete=models.deletion.CASCADE
    )

    user = models.ForeignKey(
        User,
        on_delete=models.deletion.CASCADE
    )
