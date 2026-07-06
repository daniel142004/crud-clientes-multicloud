# CRUD Clientes - Arquitectura Multi Cloud con Alta Disponibilidad

Evaluación 4 - Arquitectura Multi Cloud

Aplicación web CRUD para la gestión de clientes de **Clientes Digitales SpA**, desplegada con alta disponibilidad en AWS Academy con base de datos externa en Supabase.

---

## Arquitectura

- 2 instancias EC2 (Amazon Linux 2023) corriendo Flask, balanceadas por un Application Load Balancer (ALB)
- Supabase como proveedor de base de datos PostgreSQL gestionada con alta disponibilidad
- La contraseña de conexión se inyecta como variable de entorno (`DB_URI`) a través del User Data script — no está hardcodeada en el código



---

## Modelo de datos

Tabla: `clientes`

| Campo    | Tipo | Descripción          |
|----------|------|----------------------|
| rut      | TEXT | Llave primaria       |
| nombre   | TEXT | Nombre completo      |
| telefono | TEXT | Teléfono de contacto |

---

## Funcionalidades CRUD

| Operación  | Descripción                                              |
|------------|----------------------------------------------------------|
| Crear      | Formulario web que inserta un cliente nuevo              |
| Leer       | Tabla con todos los clientes registrados                 |
| Actualizar | Mismo formulario: si el RUT ya existe, actualiza los datos |
| Eliminar   | Botón con confirmación que borra el registro por RUT     |

---

## Stack tecnológico

| Capa        | Tecnología                        |
|-------------|-----------------------------------|
| Backend     | Python 3 + Flask                  |
| Frontend    | HTML + Bootstrap 5                |
| Base datos  | PostgreSQL (Supabase)             |
| Infra       | AWS EC2 + Application Load Balancer |
| Despliegue  | User Data script (bash)           |
| Versiones   | GitHub                            |

---

## Estructura del repositorio
crud-clientes-multicloud/
├── app.py               # Aplicación Flask con endpoints CRUD
├── templates/
│   └── index.html       # Interfaz web con Bootstrap
├── .gitignore           # Excluye .env con credenciales
└── README.md

---

## Despliegue en AWS Academy

1. Lanzar instancia EC2 con **Amazon Linux 2023**, tipo `t2.micro`.
2. Asociar Security Group con puerto **80 abierto** (HTTP).
3. En **"Datos de usuario"**, pegar el script `user_data.sh` con la variable `DB_URI` configurada.
4. La instancia instala dependencias, crea el entorno virtual y levanta Flask en el puerto 80 automáticamente.
5. Repetir para la segunda instancia.
6. Registrar ambas instancias en el **Target Group** del ALB.

---

## Variables de entorno

| Variable | Descripción                        |
|----------|------------------------------------|
| `DB_URI` | Connection string de Supabase PostgreSQL |

La variable se define directamente en el User Data script y no se almacena en ningún archivo del repositorio.

