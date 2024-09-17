# add_products.py
from app import app, db, Product

with app.app_context():
    # Clear existing data
    db.drop_all()
    db.create_all()

    # Add new products
    products = [
        Product(name='Product 1', description='Description for Product 1', category='Category 1', price=10.0),
        Product(name='Product 2', description='Description for Product 2', category='Category 2', price=20.0),
        Product(name='Product 3', description='Description for Product 3', category='Category 3', price=30.0),
    ]

    db.session.bulk_save_objects(products)
    db.session.commit()
    print("Products added!")
