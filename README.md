# ci-cd-python

Práctica de introducción a CI/CD.

## Cómo crear un virtualenv en Python

Creamos el entorno virtual.

```bash
python3 -m venv venv
```

Activamos el entorno virtual.

```bash
source venv/bin/activate
```

Instalamos las dependencias.

```bash
pip install -r requirements.txt
```

Para desactivar el entorno virtual.

```bash
deactivate
```

## Cómo ejecutar los tests

Para realizar los tests vamos a utilizar `unittest`, que es el framework de
pruebas unitarias que viene integrado en Python.

Desde la raíz del proyecto, ejecutamos el siguiente comando.

```bash
python3 -m unittest tests/*.py
```

Este comando ejecutará todos los tests que se encuentren en la carpeta `tests`.