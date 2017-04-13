from django.core.urlresolvers import reverse
from django.test import TestCase
from .models import Course, Step
from django.utils import timezone


# Create your tests here.


class CourseModelTest(TestCase):
    def test_course_creation(self):
        course = Course.objects.create(
            title='some fake title',
            description='fake description',
        )
        now = timezone.now()
        self.assertLessEqual(course.created_at, now)


class stepModelTest(TestCase):
    def setUp(self):
        self.course = Course.objects.create(
            title='some fake title',
            description='fake description',
        )

    def test_step_creation(self):
        step = Step.objects.create(
            title='fake step title',
            description='fake step description',
            course=self.course
        )
        self.assertIn(step, self.course.step_set.all())


class ViewTest(TestCase):
    def setUp(self):
        self.course = Course.objects.create(
            title='some fake title',
            description='fake description',
        )
        self.course1 = Course.objects.create(
            title='some fake title 1',
            description='fake description',
        )
        self.step = step = Step.objects.create(
            title='fake step title',
            description='fake step description',
            course=self.course
        )

    def test_course_list_view(self):
        resp = self.client.get(reverse('courses:course_list'))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.course, resp.context['courses'])
        self.assertIn(self.course1, resp.context['courses'])
        self.assertContains(resp, self.course.title)
        self.assertTemplateUsed(resp, 'courses/course_list.html')

    def test_step_detail_view(self):
        resp = self.client.get(reverse('courses:course_step', kwargs={
            'course_pk': self.course.pk,
            'step_pk': self.step.pk
        }))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(self.step, resp.context['step'])
