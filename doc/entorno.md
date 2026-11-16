# Guía de configuración del entorno virtual

Guía para preparar el entorno de Python del proyecto **BigData_Roimer**.

## Datos del sistema

| | |
|---|---|
| Sistema operativo | Windows |
| Terminal | MSYS2 UCRT64 (bash) |
| Python | CPython 3.15 (64 bits), llamado con el launcher `py` |
| Herramienta de entornos | `virtualenv` |
| Nombre del entorno | `.venv` |

---

## 1. ¿Qué es un entorno virtual?

Un entorno virtual es una carpeta aislada con su propio intérprete de Python y sus propios paquetes. Así cada proyecto tiene sus dependencias (y versiones) sin mezclarse con otros proyectos ni con el Python del sistema.

### `virtualenv` vs `venv`

| | `venv` (`py -m venv .venv`) | `virtualenv` (`py -m virtualenv .venv`) |
|---|---|---|
| Instalación | Viene con Python (3.3+) | Se instala con `pip install virtualenv` |
| Velocidad | Más lento | Más rápido (usa caché) |
| Python 2 / versiones viejas | No | Sí |
| Elegir versión de Python | `py -3.11 -m venv .venv` | `virtualenv -p 3.11 .venv` |
| Funciones extra | Las básicas | Más opciones y plugins |

En este proyecto se usa **`virtualenv`**.

---

## 2. Instalar `virtualenv`

```bash
py -m pip install virtualenv
```

> Se usa `py -m <modulo>` para llamar a las herramientas como módulo de Python. Así
> funcionan aunque su carpeta `Scripts` no esté en el PATH.

---

## 3. Crear el entorno

Ubicarse en la carpeta del proyecto y crear el entorno:

```bash
cd /d/unc/topico/BigData_Roimer
py -m virtualenv .venv
```

### ¿Por qué el nombre `.venv`?

- Es la **convención estándar** (la usa la documentación oficial de Python).
- **VS Code, PyCharm** y otras herramientas lo detectan como intérprete sin configurar nada.
- Los `.gitignore` típicos de Python ya lo incluyen.
- El punto lo deja oculto y separado visualmente del código.
- Usar el mismo nombre en todos los proyectos hace que siempre se active igual.

### Contenido de `.venv/`

```
.venv/
├── Include/
├── Lib/            # paquetes instalados (site-packages)
├── Scripts/        # python.exe, pip.exe y scripts de activación
├── .gitignore      # hace que Git ignore el entorno
├── CACHEDIR.TAG
└── pyvenv.cfg      # configuración del entorno (versión de Python, etc.)
```

> `virtualenv` crea un `.gitignore` dentro de `.venv/`, así que **Git ignora el entorno
> automáticamente** y no se sube al repositorio.

---

## 4. Activar y desactivar el entorno

| Terminal | Comando |
|---|---|
| MSYS2 / Git Bash | `source .venv/Scripts/activate` |
| PowerShell | `.venv\Scripts\Activate.ps1` |
| CMD | `.venv\Scripts\activate.bat` |

Cuando está activo, el prompt empieza con `(.venv)`. Para comprobarlo:

```bash
which python
# /d/unc/topico/BigData_Roimer/.venv/Scripts/python
```

Para salir del entorno:

```bash
deactivate
```

---

## 5. Gestionar dependencias

Con el entorno activado:

```bash
python -m pip install --upgrade pip   # actualizar pip
pip install <paquete>                 # instalar dependencias
pip freeze > requirements.txt         # guardar la lista de dependencias
pip install -r requirements.txt       # recrear el entorno en otra máquina
```

---

## 6. Usar el entorno en VS Code

1. Abrir la carpeta del proyecto en VS Code.
2. `Ctrl + Shift + P` → **Python: Select Interpreter**.
3. Elegir el intérprete de `.venv`.

---

## 7. Posibles problemas y cómo corregirlos

### `virtualenv: command not found`

`virtualenv` está instalado, pero la carpeta `Scripts` donde está el ejecutable no está en el PATH de la terminal.

**Corrección:** llamarlo como módulo de Python:

```bash
py -m virtualenv .venv
```

### `pip install` falla con *externally-managed-environment*

En MSYS2 el comando `python` puede apuntar al Python propio de MSYS2 (`/ucrt64/bin/python`), que bloquea instalar paquetes.

**Corrección:** usar el Python de Windows con el launcher `py`, o trabajar siempre dentro del entorno activado. Para ver qué Python se está usando:

```bash
which python
```

### La activación en PowerShell es bloqueada

PowerShell puede impedir ejecutar scripts como `Activate.ps1`.

**Corrección** (una sola vez):

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

### Los paquetes se instalan fuera del entorno

El entorno no estaba activado al ejecutar `pip install`.

**Corrección:** verificar que aparece `(.venv)` en el prompt y que `which python` apunta a `.venv`.

### Se quiere cambiar el nombre del entorno

Un entorno virtual **no se puede renombrar** moviendo la carpeta, porque guarda rutas absolutas adentro.

**Corrección:** borrarlo y crearlo de nuevo con el nombre deseado:

```bash
deactivate
rm -rf <nombre_viejo>
py -m virtualenv .venv
pip install -r requirements.txt
```

### El entorno quedó dañado o con paquetes incorrectos

**Corrección:** eliminarlo y recrearlo:

```bash
deactivate
rm -rf .venv
py -m virtualenv .venv
source .venv/Scripts/activate
pip install -r requirements.txt
```

### VS Code no detecta el entorno

**Corrección:** ejecutar **Python: Select Interpreter** y elegir `.venv`. Si no aparece, cerrar y volver a abrir VS Code en la carpeta del proyecto.

---

## Resumen rápido (recrear el entorno desde cero)

```bash
cd /d/unc/topico/BigData_Roimer
py -m pip install virtualenv
py -m virtualenv .venv
source .venv/Scripts/activate
pip install -r requirements.txt   # cuando exista
```

---

© 2026 Juan Roimer Bautista Huingo
