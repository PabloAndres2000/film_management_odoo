## Stack Tecnologico

```
Lenguaje: Python.

Framework: Odoo.

Infraestructura: Docker.

Base de Datos: PostgreSQL.
```

## Descripción del Proyecto

Este proyecto es un Módulo de Gestión de Películas para Odoo, diseñado para obtener información sobre películas desde una API externa y almacenarla en una base de datos PostgreSQL. El módulo permite gestionar las películas, incluyendo su título, ranking y fecha de última actualización. La información de las películas se obtiene de manera periódica desde una API y se almacena en la base de datos de Odoo.

El sistema ejecuta una tarea programada (cron job) para hacer una consulta a la API de películas, obtener los datos y almacenarlos en la base de datos cada 1 minuto.

## Requisitos previos

Asegúrate de tener instalados los siguientes programas:

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [Git](https://git-scm.com/)

## Pasos para ejecutar el proyecto

### 1. Crear archivo .env

Debes crear el archivo `.env` para que funcione el proyecto completo, recuerda revisar el archivo:`.env.template`. Copia el contenido y dejalo en `.env`

### 2. Buildear y levantar el proyecto

#### **2.1. `docker-compose build`**

Sirve para construir las imagenes creadas en el docker-compose

#### **2.2. `docker-compose up -d`**

Una vez que las imágenes estén construidas, el siguiente paso es levantar los contenedores en segundo plano

### 3. Ingreso de Odoo

En este apartado es importante que puedas ingresar en **`Master Password`** lo siguiente: **`rc5y-mz9m-5nsj`**. Es sumamente importante ya que con eso podras ingresar a Odoo y crear tu cuenta. En caso de no hacerlo indicara: `Database creation error: Access Denied`. En **`Database Name`** debes colocar `db`.

### 3. Paso a paso para hacer funcionar la prueba:

En aplicaciones busca **`Movies Management`** y activalo, cuando lo tengas activado, lo ideal es dirigrte a **`API Settings`** para probar la conexion de la api externa de peliculas, la url se deja directa para que puedas probar la conexion, en caso que este bien indicara una alerta de exito, en caso de error, dira que la conexion es invalida. Cuando este todo configurado y ya la prueba de conexion sea exitosa, automaticamente se correra el cron cada 1 minuto para buscar registros desde la api externa, en caso que te demores en hacer el test de conexion y no se cree 10 registros, puedes hacerlo manualmente o indicar cuantas veces quieres que se creen el registro. Para eso ingresa a esta url: http://localhost:8069/web#action=13&model=ir.cron&view_type=list&cids=1. **`Ingresas a Import Random Movie Every Minute`** y podras configurar el numero de ejecuciones automaticamente o crearlos manualmente. ya cuando este todo okey, podras revisar el API REST creado, sigue el paso 5.

imagenes de referencia:
<img width="1440" alt="Captura de pantalla 2025-04-24 a la(s) 11 33 33 p m" src="https://github.com/user-attachments/assets/131d1a96-1876-442d-b2df-5d0e3a27ac29" />
<img width="1440" alt="Captura de pantalla 2025-04-24 a la(s) 11 34 16 p m" src="https://github.com/user-attachments/assets/6e7da025-a405-45d1-9f27-06d929b7360c" />
<img width="1439" alt="Captura de pantalla 2025-04-24 a la(s) 11 34 56 p m" src="https://github.com/user-attachments/assets/5a43aa2c-386f-4c15-a118-631c28b8b861" />
<img width="1439" alt="Captura de pantalla 2025-04-24 a la(s) 11 36 28 p m" src="https://github.com/user-attachments/assets/7694cb56-82dd-4ee3-b8ab-894167613294" />


### 4. Revision de logs

Cuanto tengas el proyecto ya runeado, veras una carpeta llamada: **`logs/odoo/odoo.log`**, Alli podras encontrar los logs del proyecto

### 5. Probar el Endpoint /api/top_movies en POSTMAN

Una vez que el proyecto esté en funcionamiento y tengas los 10 registros de las peliculas, se mostrara un JSON la información del top 10 de las películas con mejor ranking.

endpoint url: http://localhost:8069/api/top_movies

imagen:
<img width="1061" alt="Captura de pantalla 2025-04-24 a la(s) 11 36 47 p m" src="https://github.com/user-attachments/assets/855f30aa-fbb5-4fe3-81c2-6873825286a8" />

### Acceder a PGAdmin

1. Asegurate que PGAdmin este levantado (`docker-compose up -d`)
2. Accede a `http://localhost:5050/` y ingresa en el login estos datos: Email: `admin@admin.com`. Contraseña: `admin`.
3. En el apartado `Servers` click derecho -> `Register` -> `Server` Ingresas en `General` y en `Name` Colocas el nombre que quieras. Luego en el apartado `Connection` los datos a rellenar son lo siguiente: HostName: `db`, Username: `odoo`, Password: `odoo`
4. Ahora podras navegar a tu antojo y revisar la base de datos:
