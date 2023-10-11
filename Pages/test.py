from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from time import sleep
# Configura las opciones de Edge para cargar la extensión
edge_options = Options()
edge_options.use_chromium = True  # Utiliza el motor Chromium de Edge

# Ruta a la carpeta que contiene la extensión (cambia esto a tu ruta real)
extension_path = './Extensiones/hCAPTCHA-Solver-auto-captcha-bypass.crx'

# # Agrega la extensión a las opciones de Edge
edge_options.add_extension(extension_path)
edge_options.add_argument("--user-data-dir=C:/Users/Diego/AppData/Local/Microsoft/Edge/User Data")

# Inicializa el servicio de Edge (cambia la ruta al ejecutable de Edge a tu ubicación real)

# Inicializa el navegador de Edge con las opciones y el servicio configurados
driver = webdriver.Edge(options=edge_options)

# Abre una página web (reemplaza 'https://www.ejemplo.com' con la URL que desees)
driver.get('https://www.ejemplo.com')
sleep(30)
# Interactúa con la extensión o realiza las acciones necesarias

# Cierra el navegador al final
driver.quit()