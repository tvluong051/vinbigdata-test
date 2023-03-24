from configtest import client, init_database
import json

def test_get_billing_no_user(client, init_database):
    path = "mobile/dummyuser/billing"
    response = client.get(path)
    assert response.status_code == 404

def test_get_billing_user(client, init_database):
    path = "mobile/user/billing"
    response = client.get(path)
    data = json.loads(response.data)
    assert 'call_count' in data
    assert 'block_count' in data
    assert data['call_count'] == 2
    assert data['block_count'] == 3

def test_put_call_user_wrong_format(client, init_database):
    path = "mobile/user/call"
    response = client.put(path,
        json = {
            "test":"test"
        }
    )
    assert response.status_code == 400
    assert b'Wrong input format' in response.data

def test_put_call_user(client, init_database):
    user = 'newuser'
    path = f"mobile/{user}/call"
    response = client.put(path,
        json = {
            "call_duration": 31000
        }
    )
    assert response.status_code == 200
    assert b'Success' in response.data

    # Try to query new entry
    path = f"mobile/{user}/billing"
    response = client.get(path)
    data = json.loads(response.data)
    assert 'call_count' in data
    assert 'block_count' in data
    assert data['call_count'] == 1
    assert data['block_count'] == 2
