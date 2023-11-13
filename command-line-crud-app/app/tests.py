from django.test import TestCase
from app import models


class TestPerson(TestCase):
    def test_create_person(self):
        person = models.create_person("Apple", 18, "Red", True)
        self.assertEqual(person.id, 1)
        self.assertEqual(person.name, "Apple")
        self.assertEqual(person.age, 18)
        self.assertEqual(person.fav_color, "Red")
        self.assertEqual(person.is_friend, True)

    def test_all_people(self):
        people_data = [
            {
                "name": "Orange",
                "age": 21,
                "fav_color": "Orange",
                "is_friend": True,
            },
            {
                "name": "Grapefruit",
                "age": 99,
                "fav_color": "Purple",
                "is_friend": False,
            },
            {
                "name": "Banana",
                "age": 7,
                "fav_color": "Yellow",
                "is_friend": True,
            },
        ]

        for person_data in people_data:
            models.create_person(
                person_data["name"],
                person_data["age"],
                person_data["fav_color"],
                person_data["is_friend"],
            )

        people = models.all_people()

        self.assertEqual(len(people), len(people_data))

    def test_find_person_by_name(self):
        people_data = [
            {
                "name": "Orange",
                "age": 21,
                "fav_color": "Orange",
                "is_friend": True,
            },
            {
                "name": "Grapefruit",
                "age": 99,
                "fav_color": "Purple",
                "is_friend": False,
            },
            {
                "name": "Banana",
                "age": 7,
                "fav_color": "Yellow",
                "is_friend": True,
            },
        ]

        for person_data in people_data:
            models.create_person(
                person_data["name"],
                person_data["age"],
                person_data["fav_color"],
                person_data["is_friend"],
            )

        self.assertIsNone(models.find_person_by_name("Apple"))

        person = models.find_person_by_name("Orange")

        self.assertIsNotNone(person)
        self.assertEqual(person.fav_color, "Orange")

    def test_same_fav_color(self):
        people_data = [
            {
                "name": "Apple",
                "age": 18,
                "fav_color": "Red",
                "is_friend": True,
            },
            {
                "name": "Adrian",
                "age": 18,
                "fav_color": "Red",
                "is_friend": False,
            },
            {
                "name": "Mina",
                "age": 18,
                "fav_color": "Pink",
                "is_friend": True,
            },
        ]

        for person_data in people_data:
            models.create_person(
                person_data["name"],
                person_data["age"],
                person_data["fav_color"],
                person_data["is_friend"],
            )

        self.assertEqual(len(models.same_fav_color("Red")), 2)

    def test_update_person_age(self):
        people_data = [
            {
                "name": "Apple",
                "age": 18,
                "fav_color": "Red",
                "is_friend": True,
            },
            {
                "name": "Adrian",
                "age": 18,
                "fav_color": "Red",
                "is_friend": False,
            },
            {
                "name": "Mina",
                "age": 18,
                "fav_color": "Pink",
                "is_friend": True,
            },
        ]

        for person_data in people_data:
            models.create_person(
                person_data["name"],
                person_data["age"],
                person_data["fav_color"],
                person_data["is_friend"],
            )

        models.update_person_age("Apple", 19)
        self.assertEqual(models.find_person_by_name("Apple").age, 19)

    def test_delete_person(self):
        people_data = [
            {
                "name": "Orange",
                "age": 21,
                "fav_color": "Orange",
                "is_friend": True,
            },
            {
                "name": "Grapefruit",
                "age": 99,
                "fav_color": "Purple",
                "is_friend": False,
            },
            {
                "name": "Banana",
                "age": 7,
                "fav_color": "Yellow",
                "is_friend": True,
            },
        ]

        for person_data in people_data:
            models.create_person(
                person_data["name"],
                person_data["age"],
                person_data["fav_color"],
                person_data["is_friend"],
            )

        models.delete_person("Grapefruit")
        self.assertEqual(len(models.all_people()), 2)
