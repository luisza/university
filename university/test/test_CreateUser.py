from django.contrib.auth.models import AnonymousUser, User
from django.test import TestCase, RequestFactory
from university.student.enrollment import enrollment as my_view
from university.models import *
from datetime import datetime

class SimpleTest(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='jacob', email='jacob@example.com', password='top_secret')

        self.instructor = Instructor.objects.create(user=self.user,
                                                    hire_date=datetime.now(),
                                                    office = Office.objects.create(location="CI-2012"),
                                                    departament = Departament.objects.create(name="mi dep", budget=2.0,start_date = datetime.now() )
                                                    )


        self.student = Student.objects.create(user=self.user)

    def test_list_courses(self):
        self.client.login(username='jacob', password='top_secret')
        response = self.client.get('/university/student/'+str(self.student.pk), follow=True)
        self.assertEqual(response.status_code, 200)


    def test_details(self):
        # Create an instance of a GET request.
        request = self.factory.get('/university/student/enrollment')

        # Recall that middleware are not supported. You can simulate a
        # logged-in user by setting request.user manually.
        request.user = self.user

        # Test my_view() as if it were deployed at /customer/details
        response = my_view(request)
        self.assertEqual(response.status_code, 200)
