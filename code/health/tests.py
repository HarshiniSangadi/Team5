from django.test import TestCase
from django.contrib.auth.models import User

class LoginTestCase(TestCase):
    def setUp(self):
        """Set up test user before running tests."""
        self.username = 'martin234'
        self.password = '1234'
        self.user = User.objects.create_user(username=self.username, password=self.password)

    def test_login_success(self):
        """Test successful login with valid credentials."""
        response = self.client.post('/view_patient/', {'uname': self.username, 'pwd': self.password})
        self.assertEqual(response.status_code, 302)  # Django redirects on success by default

    def test_login_failure_invalid_password(self):
        """Test login failure due to incorrect password."""
        response = self.client.post('/login/', {'uname': self.username, 'pwd': 'wrongpassword'})
        self.assertEqual(response.status_code, 200)  # Login form re-rendered on failure

    def test_login_failure_invalid_username(self):
        """Test login failure with a non-existent username."""
        response = self.client.post('/login/', {'uname': 'wronguser', 'pwd': self.password})
        self.assertEqual(response.status_code, 200)

    def test_login_required_redirect(self):
        """Test that an unauthenticated user is redirected from a protected page."""
        response = self.client.get('/patient_home/', follow=True)
        self.assertRedirects(response, '/login/?next=/patient_home/')
