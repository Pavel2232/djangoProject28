import pytest


@pytest.mark.django_db
def test_retrieve_ad(client, ad,hr_token):
    expected_response = {'id': 12, 'author': None, 'category': None, 'name': 'test', 'price': 10, 'description': None, 'is_published': True, 'image': None}


    response = client.get(f"/ad/{ad.pk}/",HTTP_AUTHORIZATION="Bearer " + hr_token)

    assert response.status_code == 200
    assert response.data == expected_response