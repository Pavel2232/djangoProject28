import pytest

from ads.models import Ad


@pytest.mark.django_db
def test_create_compilation(client, hr_token):
    expected_response = {'id': 1, 'ads': ['test567891011'], 'name': 'test'}
    # ad = Ad.create(name= "test567891011",
    #     price = 10,)


    Ad.objects.create(id = 1,name= "test567891011",
        price = 10,)
    response = client.post("/selection/create/", data={
        "name": "test",
        "ads" : [1],
    },content_type="application/json", HTTP_AUTHORIZATION="Bearer " + hr_token)

    assert response.status_code == 201
    assert response.data == expected_response
