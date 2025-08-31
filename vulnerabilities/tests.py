from django.test import TestCase
from django.urls import reverse
from .models import Vulnerability

class VulnerabilityTests(TestCase):

    def setUp(self):
        self.vulnerability = Vulnerability.objects.create(
            title="Insecure Direct Object Reference",
            description="Example of insecure direct object reference."
        )

    def test_insecure_direct_object_reference(self):
        response = self.client.get(reverse('vulnerabilities:insecure_direct_object_reference'))
        self.assertEqual(response.status_code, 200)

    def test_broken_authentication(self):
        response = self.client.get(reverse('vulnerabilities:broken_authentication'))
        self.assertEqual(response.status_code, 200)

    def test_cross_site_scripting(self):
        response = self.client.get(reverse('vulnerabilities:cross_site_scripting'))
        self.assertEqual(response.status_code, 200)

    def test_sql_injection(self):
        response = self.client.get(reverse('vulnerabilities:sql_injection'))
        self.assertEqual(response.status_code, 200)

    def test_security_misconfiguration(self):
        response = self.client.get(reverse('vulnerabilities:security_misconfiguration'))
        self.assertEqual(response.status_code, 200)