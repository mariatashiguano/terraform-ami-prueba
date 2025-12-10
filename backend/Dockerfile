# Usamos una imagen ligera de Python
FROM python:3.9-slim

# Directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiamos los requerimientos primero (para aprovechar el caché de Docker)
COPY requirements.txt .

# Instalamos las librerías
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el resto del código (app.py, etc.)
COPY . .

# Exponemos el puerto 80
EXPOSE 80

# Comando para arrancar
CMD ["python", "app.py"]