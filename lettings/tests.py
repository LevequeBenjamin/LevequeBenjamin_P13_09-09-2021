import pytest
from django.urls import reverse
from lettings.models import Letting, Address


@pytest.mark.django_db
def test_letting_index_view(client):
    url = reverse('lettings_index')
    response = client.get(url)
    assert b"Lettings" in response.content
    assert response.status_code == 200


@pytest.mark.django_db
def test_letting_view(client):
    address = Address.objects.create(
        number=4856, street='Test Street',
        city='Test City',
        state='Test',
        zip_code=8562,
        country_iso_code='TEST'
    )
    letting = Letting.objects.create(
        title='Test Title',
        address_id=address.id
    )
    url = reverse('letting', args=(letting.id,))
    response = client.get(url)
    assert b'Test Title' in response.content
    assert response.status_code == 200
