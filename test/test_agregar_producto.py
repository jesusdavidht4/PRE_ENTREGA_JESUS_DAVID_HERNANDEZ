from pages.login_pages import LoginPage
from pages.agregar_producto_page import AgregarProductoPage
from data.productos import PRODUCTOS
import pytest

@pytest.mark.parametrize("indice, nombre_esperado", PRODUCTOS)
def test_agregar_producto(driver, indice, nombre_esperado):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    agregar = AgregarProductoPage(driver)

    nombre_producto = agregar.obtener_nombre_producto(indice)
    assert nombre_producto == nombre_esperado

    agregar.agregar_producto(indice)

    assert agregar.obtener_badge() == "1"

    agregar.ir_al_carrito()

    assert agregar.obtener_nombre_en_carrito() == nombre_esperado