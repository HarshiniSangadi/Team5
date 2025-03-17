import pytest
from django.contrib.auth.models import User

@pytest.fixture
def test_user(db):
    """Fixture to create a test user."""
    user = User.objects.create_user(username='testuser', password='TestPassword123')
    return user
