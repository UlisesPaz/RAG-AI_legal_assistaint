# Prerequisitos

contar con ollama (<https://ollama.com/download>)
contar con las Build Tools (<https://visualstudio.microsoft.com/es/visual-cpp-build-tools/>)
tener un modelo cargado en ollama (<https://ollama.com/search>)
Nota en el caso concreto de el equipo usado fue *llama3.2-vision*

## Uso de otro modelo

reemplazar en la linea **llama3.2** por el modelo elegido

~~~
llm = ChatOllama(model='llama3.2', temperature=0)
~~~

## Instalación

```
pip install -r requirements.txt
```

## Ejecución

1. Es necesario cargar en la carpeta data los archivos que se desean agregar al modelo
2. Ejecutar el archivo **VectorDB.ipynb** y agregar un archivo para entrenar

```
py ./src/Inicio.py

```

## Mejorables

- [x] Mejorar la interfaz web
- [x] Contenerizar
- [ ] Automatizar carga de los archivos
