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

Desde la raíz del proyecto, ejecutamos el siguiente comando.

```bash
python3 -m unittest discover -s tests
```

- `unittest`: Es el framework de pruebas unitarias que viene integrado en Python.
- `python3 -m unittest`: Ejecuta el módulo `unittest` como un script.
- `discover`: Es una subcomando de `unittest` que busca automáticamente archivos de prueba en el directorio especificado.
- `-s tests`: El parámetro `-s` indica el directorio donde se encuentran los archivos de prueba, que en este caso será el directorio `tests`.