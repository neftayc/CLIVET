# coding: utf-8 _*_
from django.utils import timezone
from django.test import TestCase
from django.core.urlresolvers import reverse
from apps.clinica.models.colamedica import ColaMedica
from apps.clinica.models.mascota import Mascota
from apps.clivet.models.cliente import Cliente
from apps.params.models import Person

# Create your tests here.
def create_poll(question, days):
    """
    Creates a poll with the given `question` published the given number of
    `days` offset to now (negative for polls published in the past,
    positive for polls that have yet to be published).
    """
    return ColaMedica.objects.create(question=question,
        pub_date=timezone.now() + date.datetime.timedelta(days=days))

class PollViewTests(TestCase):
    def test_index_view_with_no_polls(self):
        """
        If no polls exist, an appropriate message should be displayed.
        """
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_poll_list'], [])

    def test_index_view_with_a_past_poll(self):
        """
        Polls with a pub_date in the past should be displayed on the index page.
        """
        create_poll(question="Past poll.", days=-30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_poll_list'],
            ['<Poll: Past poll.>']
        )

    def test_index_view_with_a_future_poll(self):
        """
        Polls with a pub_date in the future should not be displayed on the
        index page.
        """
        create_poll(question="Future poll.", days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, "No polls are available.", status_code=200)
        self.assertQuerysetEqual(response.context['latest_poll_list'], [])

    def test_index_view_with_future_poll_and_past_poll(self):
        """
        Even if both past and future polls exist, only past polls should be
        displayed.
        """
        create_poll(question="Past poll.", days=-30)
        create_poll(question="Future poll.", days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_poll_list'],
            ['<Poll: Past poll.>']
        )

    def test_index_view_with_two_past_polls(self):
        """
        The polls index page may display multiple polls.
        """
        create_poll(question="Past poll 1.", days=-30)
        create_poll(question="Past poll 2.", days=-5)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_poll_list'],
             ['<Poll: Past poll 2.>', '<Poll: Past poll 1.>']
        )

"""
class MascotaTestCase(TestCase):
    def setUp(self):
        a1 = Person.objects.create(first_name="J.K. Rowling")
        a2 = Cliente.objects.create(persona=a1)
        Mascota.objects.create(nombre="tarzan", color="negro", dueño=a2)
        Mascota.objects.create(nombre="golen", color="blanco", dueño=a2)

    def test_animals_can_speak(self:
        tarzan = Mascota.objects.get(nombre="tarzan")
        golen = Mascota.objects.get(nombre="golen")
        self.assertEqual(tarzan.color, 'negro')
        self.assertEqual(golen.color, 'blanco')"""
