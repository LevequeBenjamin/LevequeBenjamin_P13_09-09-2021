import pytest
from django.contrib.auth.models import User
from django.urls import reverse
from profiles.models import Profile


@pytest.mark.django_db
def test_profile_index_view(client):
    url = reverse('profiles_index')
    response = client.get(url)
    assert b"Profiles" in response.content
    assert response.status_code == 200


@pytest.mark.django_db
def test_profile_view(client):
    user = User.objects.create(username='Sangoku', first_name='Goku', last_name="San",
                               email='sangoku@test.com')
    Profile.objects.create(favorite_city='Annecy', user_id=user.id)
    url = reverse('profile', args=(user.username, ))
    response = client.get(url)
    assert b'Sangoku' in response.content
    assert response.status_code == 200
