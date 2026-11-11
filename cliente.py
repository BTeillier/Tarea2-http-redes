import urllib3

http = urllib3.PoolManager()

print("Enviando petición GET al servidor Apache...")

response = http.request("GET", "http://localhost:8080/")

print(f"Estado de la respuesta: {response.status}")
print(f"Datos recibidos:\n{response.data.decode('utf-8')[:150]}...")
