def test_register_user(client):


    response = client.post(

        "/api/v1/auth/register",

        json={

            "name":"Test User",

            "email":"test@gmail.com",

            "password":"Test@123"

        }

    )


    assert response.status_code == 200


    data=response.json()


    assert data["email"]=="test@gmail.com"




def test_login_user(client):


    response = client.post(

        "/api/v1/auth/login",

        json={

            "email":"test@gmail.com",

            "password":"Test@123"

        }

    )


    assert response.status_code == 200


    data=response.json()


    assert "access_token" in data
