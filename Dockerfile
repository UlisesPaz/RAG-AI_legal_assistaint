FROM python:3.9-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar los archivos del proyecto al contenedor
COPY . .

# Instalar las dependencias
RUN pip install -r requirements.txt

# Exponer el puerto en el que se ejecutará la app
EXPOSE 7860

# Comando para ejecutar la aplicación
CMD ["python", "src/Inicio.py"]