def get_admin_token(client):


    response=client.post(

        "/api/v1/auth/login",

        json={

            "email":"admin@gmail.com",

            "password":"Admin@123"

        }

    )


    return response.json()["access_token"]





def test_create_product(client):


    token=get_admin_token(client)



    response=client.post(

        "/api/v1/products",

        headers={

            "Authorization":
            f"Bearer {token}"

        },

        json={

            "name":"Laptop",

            "description":
            "Gaming Laptop",

            "price":80000,

            "stock":10,

            "category":
            "electronics"

        }

    )



    assert response.status_code==200



    data=response.json()



    assert data["name"]=="Laptop"




def test_get_products(client):


    response=client.get(

        "/api/v1/products"

    )


    assert response.status_code==200


    data=response.json()


    assert "data" in data
