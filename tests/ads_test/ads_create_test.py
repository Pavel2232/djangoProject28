import pytest

from categories.models import Categorie


@pytest.mark.django_db
def test_create_ad(client, hr_token):
    expected_response = {'id': 1, 'category': 'Cтихии123', 'image': '1', 'name': 'test567891011', 'price': 10, 'description': None, 'is_published': True, 'author': 1}


    Categorie.objects.create(slug="Стихии123")
    response = client.post("/ad/create/", data={
        "name": "test567891011",
        "author": 1,
        "price" : 10,
        "is_published" : True,
        "image" : "1",
        "category" : "Cтихии123"
    },content_type="application/json", HTTP_AUTHORIZATION="Bearer " + hr_token)

    assert response.status_code == 201
    assert response.data == expected_response