import pytest
from app.application import Application


@pytest.fixture
def app(request):
    app = Application()
    request.addfinalizer(app.quit)
    return app

def test_add_and_del_products_at_cart(app):
    app.add_products_to_cart(3)
    app.delete_all_products_at_cart()