from django.db import models


# Create your models here.
class Person(models.Model):
    name = models.TextField()
    age = models.PositiveIntegerField()
    fav_color = models.TextField()
    is_friend = models.BooleanField()


def create_person(name, age, fav_color, is_friend):
    person = Person(name=name, age=age, fav_color=fav_color, is_friend=is_friend)
    person.save()
    return person


def all_people():
    return Person.objects.all()


def find_person_by_name(name):
    try:
        return Person.objects.get(name=name)
    except Person.DoesNotExist:
        return None


def same_fav_color(fav_color):
    return Person.objects.filter(fav_color=fav_color)


def update_person_age(name, new_age):
    person = Person.objects.get(name=name)
    person.age = new_age
    person.save()
    return person


def delete_person(name):
    person = Person.objects.get(name=name)
    person.delete()
