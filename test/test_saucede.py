from utils.helpers import login
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_loging(driver):
    login(driver, "standard_user", "secret_sauce")
    assert "inventory.html" in driver.current_url
    title = driver.find_element(By.CLASS_NAME, "title").text
    assert title == "Products"


def test_catalogo_productos(driver):
    login(driver, "standard_user", "secret_sauce")
    productos = driver.find_elements(By.CSS_SELECTOR, "[data-test='inventory-item']")
    assert len(productos) > 0
    nombre = productos[0].find_element(By.CSS_SELECTOR, "[data-test='inventory-item-name']")
    assert nombre.text == "Sauce Labs Backpack"


def test_agregar_al_carrito(driver):
    login(driver, "standard_user", "secret_sauce")
    wait = WebDriverWait(driver, 10)

    nombre_producto = driver.find_element(By.CSS_SELECTOR, "[data-test='inventory-item-name']").text

    btn_add = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Add to cart')]"))
    )
    btn_add.click()

    badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
    assert badge.text == "1"

    driver.find_element(By.CSS_SELECTOR, "[data-test='shopping-cart-link']").click()
    producto_carrito = driver.find_element(By.CSS_SELECTOR, "[data-test='inventory-item-name']")
    assert producto_carrito.text == nombre_producto