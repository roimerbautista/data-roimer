# Guía de instalación de Ubuntu en WSL

Guía para instalar y preparar Ubuntu dentro de Windows con **WSL** (Windows Subsystem for Linux) para el curso de **Tópicos de Big Data**.

## Datos del sistema

| | |
|---|---|
| Sistema operativo | Windows 11 |
| WSL | 3.0.5 (WSL 2, kernel 6.18) |
| Distribución | Ubuntu 26.04 LTS |
| Nombre de la distribución | `Ubunto-topico` |
| Usuario Linux | `bahuro` |

---

## 1. ¿Qué es WSL?

WSL permite ejecutar un sistema Linux real dentro de Windows, sin máquina virtual ni arranque dual. Es útil para Big Data porque herramientas como Hadoop, Spark o Kafka están pensadas para Linux.

---

## 2. Verificar qué hay instalado

En **PowerShell**:

```powershell
wsl --version   # versión de WSL
wsl -l -v       # distribuciones instaladas
wsl -l -o       # distribuciones disponibles para instalar
```

> Si aparece solo `docker-desktop`, **Ubuntu no está instalado**. Esa distribución la crea
> Docker Desktop para uso interno y no sirve para trabajar.

---

## 3. Instalar Ubuntu con un nombre personalizado

La opción `--name` permite elegir el nombre de la distribución (sin espacios):

```powershell
wsl --install -d Ubuntu-26.04 --name Ubunto-topico
```

Opcionalmente, `--location` permite instalarla en otro disco:

```powershell
wsl --install -d Ubuntu-26.04 --name Ubunto-topico --location D:\WSL\Ubunto-topico
```

Durante la instalación se pide:

1. **Usuario de Linux** (por ejemplo `bahuro`). Puede ser distinto del de Windows.
2. **Contraseña**. Se usa para `sudo`. Al escribirla no se ve nada en pantalla; es normal.
3. Si se quiere enviar métricas anónimas a Canonical (`Y/n`). Es opcional.

Salida esperada:

```
Descargando: Ubuntu 26.04 LTS
Instalando: Ubuntu 26.04 LTS
Distribución instalada correctamente. Se puede iniciar a través de "wsl.exe -d Ubunto-topico"
Provisioning the new WSL instance Ubunto-topico
Create a default Unix user account: bahuro
passwd: password updated successfully
```

---

## 4. Entrar y salir de Ubuntu

```powershell
wsl -d Ubunto-topico      # entrar
```

```bash
exit                      # salir
```

También se puede abrir buscando la distribución en el menú Inicio o en Windows Terminal.

Otros comandos útiles (desde PowerShell):

```powershell
wsl --set-default Ubunto-topico   # usarla por defecto al escribir solo "wsl"
wsl --terminate Ubunto-topico     # apagar la distribución
wsl --shutdown                    # apagar todo WSL
```

---

## 5. Actualizar el sistema

Es lo primero que hay que hacer después de instalar:

```bash
sudo apt update && sudo apt upgrade -y
```

| Comando | Qué hace |
|---|---|
| `sudo` | Ejecuta como administrador (pide la contraseña de Linux) |
| `apt update` | Descarga la lista actualizada de paquetes |
| `apt upgrade -y` | Instala las actualizaciones sin pedir confirmación |

---

## 6. Archivos entre Windows y Linux

| Desde | Ruta |
|---|---|
| Linux → disco D de Windows | `/mnt/d/` (ej. `D:\unc\topico` = `/mnt/d/unc/topico`) |
| Windows → archivos de Linux | `\\wsl$\Ubunto-topico\home\bahuro` |

> **Tip de rendimiento:** los proyectos que se ejecutan en Linux van mucho más rápido si
> están dentro del sistema de archivos de Linux (`~/`) que en `/mnt/d/`.

---

## 7. Repositorio del curso

Repositorio del docente, clonado en `D:\unc\topico\Topicos_BigData`:

```powershell
cd D:\unc\topico
git clone https://github.com/jllanosb/Topicos_BigData.git
```

Desde Ubuntu se accede en `/mnt/d/unc/topico/Topicos_BigData`.

---

## 8. Posibles problemas y cómo corregirlos

### `wsl -l -v` muestra caracteres raros

La salida de `wsl` está en UTF-16. **Corrección:** en PowerShell, ejecutar antes `$env:WSL_UTF8=1`.

### Se quiere cambiar el nombre de la distribución

WSL no permite renombrarla directamente. **Corrección:** exportarla e importarla con otro nombre:

```powershell
wsl --export Ubunto-topico D:\WSL\backup.tar
wsl --unregister Ubunto-topico
wsl --import <NuevoNombre> D:\WSL\<NuevoNombre> D:\WSL\backup.tar
```

> Después de importar, el usuario por defecto puede quedar como `root`. Para volver a
> `bahuro`, agregar en `/etc/wsl.conf`:
> ```
> [user]
> default=bahuro
> ```

### Se olvidó la contraseña de Linux

```powershell
wsl -d Ubunto-topico -u root
```

```bash
passwd bahuro
```

### Eliminar la distribución por completo

> **Cuidado:** borra todos los archivos de Linux de esa distribución.

```powershell
wsl --unregister Ubunto-topico
```

---

## Resumen rápido

```powershell
wsl --install -d Ubuntu-26.04 --name Ubunto-topico
wsl -d Ubunto-topico
```

```bash
sudo apt update && sudo apt upgrade -y
```

---

© 2026 Juan Roimer Bautista Huingo
