Proyecto de Automatización Web con Selenium y Pytest
Este proyecto automatiza casos de prueba del sitio [SauceDemo](https://www.saucedemo.com/).  
Incluye validaciones de **login, título de la página y funcionalidades del carrito de compras**.

---

Tecnologías utilizadas

- Python 3.13**
- Pytest** – framework para ejecución de pruebas
- Selenium WebDriver** – automatización de navegadores
- pytest-html** – generación de reportes en formato HTML
Estructura del proyecto

preentrega/
│
├── pages/
│ ├── login_page.py # Page Object: página de login
│ └── inventory_page.py # Page Object: página de productos
│
├── tests/
│ ├── test_titulo_login.py # Valida título y login
│ ├── test_carrito.py # Agrega producto y verifica en carrito
│ └── init.py
│
├── conftest.py # Fixtures (driver, login_in_driver)
├── play_tests.py # Script para ejecutar pytest con reportes
├── pytest.ini # Configuración general de pytest
└── README.md # Documentación del proyecto
