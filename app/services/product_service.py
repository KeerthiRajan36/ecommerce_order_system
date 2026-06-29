from sqlalchemy.orm import Session


from app.models.product import Product


from app.schemas.product import (
    ProductCreate,
    ProductUpdate
)


from app.exceptions.custom import (
    ProductNotFoundException,
    ProductAlreadyExistsException
)





def create_product(

    db:Session,

    product_data:ProductCreate

):


    existing = db.query(Product).filter(

        Product.name == product_data.name

    ).first()



    if existing:

        raise ProductAlreadyExistsException()



    product = Product(

        **product_data.model_dump()

    )



    db.add(product)

    db.commit()

    db.refresh(product)



    return product





def get_products(

    db:Session,

    category:str=None,

    page:int=1,

    limit:int=10

):


    query=db.query(Product)



    if category:

        query=query.filter(

            Product.category==category

        )



    total=query.count()



    products=query.offset(

        (page-1)*limit

    ).limit(limit).all()



    return {

        "total_records":total,

        "current_page":page,

        "limit":limit,

        "data":products

    }





def get_product(

    db:Session,

    product_id:int

):


    product=db.query(Product).filter(

        Product.id==product_id

    ).first()



    if not product:

        raise ProductNotFoundException()



    return product





def update_product(

    db:Session,

    product_id:int,

    product_data:ProductUpdate

):


    product=get_product(

        db,

        product_id

    )



    updates=product_data.model_dump(
        exclude_unset=True
    )



    for key,value in updates.items():

        setattr(
            product,
            key,
            value
        )



    db.commit()

    db.refresh(product)



    return product





def delete_product(

    db:Session,

    product_id:int

):


    product=get_product(

        db,

        product_id

    )



    product.is_active=False



    db.commit()



    return {

        "message":
        "Product deleted successfully"

    }
