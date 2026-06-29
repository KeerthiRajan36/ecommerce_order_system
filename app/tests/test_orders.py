def test_create_order(client):


    token=client.post(

        "/api/v1/auth/login",

        json={

            "email":
            "test@gmail.com",

            "password":
            "Test@123"

        }

    ).json()["access_token"]



    response=client.post(

        "/api/v1/orders",

        headers={

            "Authorization":
            f"Bearer {token}"

        }

    )



    assert response.status_code==200



    data=response.json()



    assert "total_amount" in data



def test_get_order(client):


    token=client.post(

        "/api/v1/auth/login",

        json={

            "email":
            "test@gmail.com",

            "password":
            "Test@123"

        }

    ).json()["access_token"]



    response=client.get(

        "/api/v1/orders/1",

        headers={

            "Authorization":
            f"Bearer {token}"

        }

    )


    assert response.status_code==200
