from django.test import TestCase

from .models import *

class StudentTestCase(TestCase):
    def setUp(self):
        StudentDetails.objects.create(name='roy', age=23, roll_no=56, class_name='12')
        StudentDetails.objects.create(name='roy1', age=20, roll_no=50, class_name='11')

    def create_student(self, name='raj', age=22, roll_no=52, class_name='9'):
        return StudentDetails.objects.create(name=name, age=age, roll_no=roll_no, class_name=class_name)

    def test_student_test(self):
        obj1 = StudentDetails.objects.get(name='roy', age=23, roll_no=56, class_name='12')
        obj2 = StudentDetails.objects.get(name='roy1', age=20, roll_no=50, class_name='11')
        self.assertEqual(obj1.name, "roy")
        self.assertEqual(obj2.name, "roy1")
        self.assertEqual(obj1.age, 23)
        self.assertEqual(obj2.age, 20)

    def test_student_qs(self):
        name='jayesh'
        age = 23
        roll_no = 56
        class_name = '12'
        object1 = self.create_student(name=name)
        object2 = self.create_student(name=name)

        qs = StudentDetails.objects.filter(name=name)
        self.assertEqual(qs.count(),2)

