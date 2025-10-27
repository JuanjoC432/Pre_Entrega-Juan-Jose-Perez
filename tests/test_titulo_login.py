import pytest
from selenium import webdriver
from pages.login_page import LoginPage


@pytest.fixture
def driver():
   # Abre y cierra el navegador automáticamente
    driver = webdriver.Firefox()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


def test_validar_titulo(driver):
    
    # Prueba que el título de la página de login sea 'Swag Labs'.
    
    login_page = LoginPage(driver)
    login_page.abrir_pagina().validar_titulo()
