# CRUD Clientes - Arquitectura Multi Cloud con Alta Disponibilidad

Evaluación 4 - Arquitectura Multi Cloud  
Aplicación web CRUD para la gestión de clientes de **Clientes Digitales**, desplegada con alta disponibilidad en AWS Academy con base de datos externa en Supabase.

---

## Arquitectura

- **2 instancias EC2** (Amazon Linux 2023) corriendo la app en contenedores **Docker**, balanceadas por un **Application Load Balancer (ALB)**
- **Amazon ECR** como registro de imágenes Docker
- **Supabase** como proveedor de base de datos PostgreSQL gestionada con alta disponibilidad
- La contraseña de conexión se inyecta como variable de entorno (`DB_URI`) en tiempo de ejecución del contenedor — no está hardcodeada en el código

---

## Modelo de datos

Tabla: `clientes`

| Campo    | Tipo | Descripción               |
|----------|------|---------------------------|
| rut      | TEXT | Llave primaria            |
| nombre   | TEXT | Nombre completo           |
| telefono | TEXT | Formato telefónico de Chile |

---

## Funcionalidades CRUD

| Operación  | Descripción                                                |
|------------|------------------------------------------------------------|
| Crear      | Formulario web que inserta un cliente nuevo                |
| Leer       | Tabla con todos los clientes registrados                   |
| Actualizar | Mismo formulario: si el RUT ya existe, actualiza los datos |
| Eliminar   | Botón con confirmación que borra el registro por RUT       |

---

## Stack tecnológico

| Capa          | Tecnología                          |
|---------------|-------------------------------------|
| Backend       | Python 3 + Flask                    |
| Frontend      | HTML + Bootstrap 5                  |
| Contenedor    | Docker (imagen python:3.11-alpine)  |
| Registro img. | Amazon ECR                          |
| Base de datos | PostgreSQL (Supabase)               |
| Infra         | AWS EC2 + Application Load Balancer |
| Despliegue    | User Data script (bash)             |
| Versiones     | GitHub                              |

---

## Estructura del repositorio
crud-clientes-multicloud/
├── app.py               # Aplicación Flask con operaciones CRUD
├── Dockerfile           # Imagen Docker basada en python:3.11-alpine
├── templates/
│   └── index.html       # Interfaz web con Bootstrap 5
├── .gitignore           # Excluye .env con credenciales
└── README.md

---

## Despliegue en AWS Academy

1. Construir la imagen Docker: `docker build -t crud-clientes .`
2. Subir la imagen a **Amazon ECR**: `docker push <uri-ecr>/crud-app:latest`
3. Lanzar 2 instancias EC2 con **Amazon Linux 2023**, tipo `t3.micro`, asignando el perfil IAM **LabInstanceProfile**.
4. Asociar Security Group con puerto **80 abierto** (HTTP).
5. En **"Datos de usuario"**, pegar el User Data script con la variable `DB_URI` configurada — el script instala Docker, descarga la imagen desde ECR y ejecuta el contenedor automáticamente.
6. Registrar ambas instancias en el **Target Group** del ALB.

---

## Variables de entorno

| Variable | Descripción                              |
|----------|------------------------------------------|
| `DB_URI` | Connection string de Supabase PostgreSQL |

La variable se define en el User Data script y se pasa al contenedor con la opción `-e` de Docker. No se almacena en ningún archivo del repositorio.
