from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Agregar un producto al carrito y verificar que esté en el carrito

def test_carrito(login_in_driver):
    
    driver = login_in_driver
    wait = WebDriverWait(driver, 10)

    try:
        # Esperar productos visibles

        productos = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item")))
        assert len(productos) > 0, " No se encontraron productos."

        # Seleccionar primer producto

        primer_producto = productos[0]
        nombre = primer_producto.find_element(By.CLASS_NAME, "inventory_item_name").text
        precio = primer_producto.find_element(By.CLASS_NAME, "inventory_item_price").text
        print(f" Primer producto: {nombre} - {precio}")

        # Agregar producto al carrito 

        primer_producto.find_element(By.TAG_NAME, "button").click()

        # Verificar contador del carrito 

        contador = wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
        ).text
        assert contador == "1", f" Contador incorrecto: {contador}"
        print(" Contador del carrito = 1")

        # Ir al carrito

        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "cart_item")))

        # Verificar producto dentro del carrito 
        
        nombre_carrito = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
        precio_carrito = driver.find_element(By.CLASS_NAME, "inventory_item_price").text

        assert nombre == nombre_carrito, f" Nombre distinto: {nombre_carrito}"
        assert precio == precio_carrito, f" Precio distinto: {precio_carrito}"
        print(f" Producto verificado en carrito: {nombre_carrito} - {precio_carrito}")

    except Exception as e:
        print(f" Error en el test del carrito: {e}")
        raise