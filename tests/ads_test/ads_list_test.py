
import pytest

from ads.serializer import AdListSerializer
from tests.factories import AdFactory, AuthorFactory


@pytest.mark.django_db
def test_list_ads(client):
    ads = AdFactory.create_batch(10)

    response =client.get("/ad/")

    extend_response = {
        'count': 10,
        'next': None,
        'previous': None,
        'results': AdListSerializer(ads,many=True).data
    }

    assert response.status_code == 200
    assert response.data == extend_response