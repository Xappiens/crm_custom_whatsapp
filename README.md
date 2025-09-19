# CRM Custom WhatsApp - Integración de Conversaciones de WhatsApp para Frappe CRM

## 📋 Descripción

Esta aplicación extiende **Frappe CRM** para incluir un nuevo menú en la barra lateral izquierda que muestra una lista de conversaciones de WhatsApp en la ventana principal. Permite a los usuarios gestionar y responder mensajes de WhatsApp directamente desde la interfaz de Frappe CRM, centralizando la comunicación con clientes en una sola plataforma.

## 🏗️ Arquitectura y Tecnologías

### Frappe Framework

**Frappe** es un framework web full-stack de código abierto escrito en **Python** y **JavaScript**. Se caracteriza por ser **meta-data driven**, lo que significa que utiliza metadatos para generar tablas de bases de datos, diseñar formularios y configurar características sin necesidad de escribir mucho código.

### Frappe CRM

**Frappe CRM** es una herramienta de gestión de relaciones con clientes (CRM) de código abierto, diseñada para equipos de ventas modernos. Construida sobre el Frappe Framework, ofrece una interfaz intuitiva y altamente personalizable.

### Stack Tecnológico

#### Backend

- **Python 3.10+** - Lenguaje principal del backend
- **Frappe Framework** - Framework web full-stack
- **MariaDB** - Sistema de gestión de bases de datos relacional
- **DocTypes** - Arquitectura orientada a documentos para definir entidades de negocio

#### Frontend

- **Vue.js 3** - Framework de JavaScript con Composition API
- **Pinia** - Gestión del estado de la aplicación
- **Vue Router** - Manejo de rutas en la aplicación
- **Frappe UI** - Biblioteca de componentes de interfaz basada en Vue
- **Tailwind CSS** - Framework de CSS para diseño responsivo
- **Vite** - Herramienta de construcción y desarrollo rápido
- **Socket.io-client** - Comunicación en tiempo real

#### Integraciones

- **WhatsApp Business API** - Para envío y recepción de mensajes
- **Twilio** - Servicios de comunicación (opcional)
- **Exotel** - Llamadas a través de teléfonos móviles (opcional)

## 🚀 Características Principales

- ✅ **Menú lateral personalizado** - Nuevo menú en el sidebar de Frappe CRM
- ✅ **Lista de conversaciones** - Visualización de conversaciones de WhatsApp
- ✅ **Interfaz integrada** - Gestión centralizada de comunicaciones
- ✅ **Tiempo real** - Sincronización automática de mensajes
- ✅ **Personalizable** - Adaptable a diferentes flujos de trabajo
- ✅ **Escalable** - Arquitectura robusta para equipos grandes

## 📦 Estructura del Proyecto

```
crm_custom_whatsapp/
├── crm_custom_whatsapp/
│   ├── __init__.py
│   ├── config/
│   │   └── __init__.py
│   ├── crm_custom_whatsapp/
│   │   └── __init__.py
│   ├── hooks.py              # Configuración de hooks de Frappe
│   ├── modules.txt           # Módulos de la aplicación
│   ├── patches.txt           # Parches de base de datos
│   ├── public/               # Archivos públicos (CSS, JS, imágenes)
│   └── templates/
│       ├── __init__.py
│       └── pages/            # Páginas personalizadas
│           └── __init__.py
├── pyproject.toml            # Configuración del proyecto
├── license.txt               # Licencia MIT
└── README.md                 # Este archivo
```

## 🛠️ Requisitos Previos

### Sistema

- **Python 3.10+**
- **Node.js 16+** (para desarrollo frontend)
- **MariaDB 10.3+**
- **Git**

### Frappe

- **Frappe Framework 15.0+**
- **Frappe CRM** instalado y funcionando
- **Bench** - Herramienta de gestión de aplicaciones Frappe

## 📥 Instalación

### 1. Configurar el entorno Frappe

```bash
# Instalar Bench (si no está instalado)
pip install frappe-bench

# Crear un nuevo sitio (si es necesario)
bench new-site tu-sitio.local
```

### 2. Instalar la aplicación

```bash
# Navegar al directorio de Bench
cd /ruta/a/tu/bench

# Obtener la aplicación
bench get-app crm_custom_whatsapp /ruta/al/repositorio

# Instalar en el sitio
bench --site tu-sitio.local install-app crm_custom_whatsapp
```

### 3. Configurar la integración de WhatsApp

1. **Obtener credenciales de WhatsApp Business API**
2. **Configurar webhook** para recibir mensajes
3. **Actualizar configuración** en Frappe CRM

## 🔧 Configuración

### Variables de Entorno

```bash
# WhatsApp Business API
WHATSAPP_ACCESS_TOKEN=tu_token_de_acceso
WHATSAPP_PHONE_NUMBER_ID=tu_id_de_telefono
WHATSAPP_WEBHOOK_VERIFY_TOKEN=tu_token_de_verificacion

# Base de datos
DB_HOST=localhost
DB_PORT=3306
DB_NAME=tu_base_de_datos
DB_USER=tu_usuario
DB_PASSWORD=tu_contraseña
```

### Configuración en Frappe

1. **Acceder a Configuración de la Aplicación**
2. **Configurar credenciales de WhatsApp**
3. **Establecer permisos de usuario**
4. **Configurar webhook de WhatsApp**

## 🎯 Uso

### Acceso al Menú de WhatsApp

1. Iniciar sesión en Frappe CRM
2. En la barra lateral izquierda, hacer clic en **"Conversaciones de WhatsApp"**
3. Visualizar la lista de conversaciones en la ventana principal

### Gestión de Conversaciones

- **Ver conversaciones** - Lista completa de chats
- **Responder mensajes** - Enviar respuestas directamente
- **Filtrar conversaciones** - Por estado, cliente, fecha
- **Buscar mensajes** - Búsqueda en tiempo real
- **Gestionar contactos** - Información de clientes

## 🔌 API y Desarrollo

### DocTypes Principales

#### WhatsApp Conversation

```python
# Estructura de datos para conversaciones
{
    "name": "CONV-2024-001",
    "phone_number": "+1234567890",
    "contact_name": "Juan Pérez",
    "last_message": "Hola, necesito información...",
    "last_message_time": "2024-01-15 10:30:00",
    "status": "Active",  # Active, Closed, Archived
    "unread_count": 2
}
```

#### WhatsApp Message

```python
# Estructura de datos para mensajes individuales
{
    "name": "MSG-2024-001",
    "conversation": "CONV-2024-001",
    "message_id": "wamid.xxx",
    "from_number": "+1234567890",
    "to_number": "+0987654321",
    "message_type": "text",  # text, image, document, etc.
    "content": "Mensaje de texto",
    "direction": "inbound",  # inbound, outbound
    "timestamp": "2024-01-15 10:30:00",
    "status": "delivered"  # sent, delivered, read, failed
}
```

### Hooks de Frappe

```python
# hooks.py
app_name = "crm_custom_whatsapp"
app_title = "CRM Custom WhatsApp"

# Configuración del menú lateral
desktop_icons = [
    {
        "module_name": "WhatsApp Conversations",
        "label": "WhatsApp",
        "icon": "octicon octicon-comment-discussion",
        "color": "#25D366",
        "link": "/app/whatsapp-conversations",
        "type": "module"
    }
]

# DocTypes de la aplicación
doctype_js = {
    "WhatsApp Conversation": "public/js/whatsapp_conversation.js",
    "WhatsApp Message": "public/js/whatsapp_message.js"
}
```

## 🧪 Testing

### Ejecutar Tests

```bash
# Tests del backend
bench --site tu-sitio.local run-tests --app crm_custom_whatsapp

# Tests del frontend
cd apps/crm_custom_whatsapp
npm test
```

### Tests de Integración

```bash
# Test de conexión con WhatsApp API
bench --site tu-sitio.local console
>>> from crm_custom_whatsapp.api.whatsapp import test_connection
>>> test_connection()
```

## 🚀 Despliegue

### Producción

```bash
# Compilar assets
bench --site tu-sitio.local build

# Migrar base de datos
bench --site tu-sitio.local migrate

# Reiniciar servicios
bench --site tu-sitio.local restart
```

### Docker

```dockerfile
# Dockerfile para contenedor de la aplicación
FROM frappe/frappe-socketio:latest

COPY . /home/frappe/frappe-bench/apps/crm_custom_whatsapp/
RUN cd /home/frappe/frappe-bench && bench build --app crm_custom_whatsapp
```

## 🤝 Contribuciones

### Cómo Contribuir

1. **Fork** el repositorio
2. **Crear** una rama para tu feature (`git checkout -b feature/nueva-funcionalidad`)
3. **Commit** tus cambios (`git commit -am 'Agregar nueva funcionalidad'`)
4. **Push** a la rama (`git push origin feature/nueva-funcionalidad`)
5. **Crear** un Pull Request

### Estándares de Código

- **Python**: Seguir PEP 8
- **JavaScript**: Seguir ESLint configurado
- **Vue.js**: Seguir Vue Style Guide
- **Commits**: Usar Conventional Commits

## 📄 Licencia

Este proyecto está licenciado bajo la **Licencia MIT** - ver el archivo [LICENSE](license.txt) para más detalles.

## 🆘 Soporte

### Documentación

- [Frappe Framework Docs](https://docs.frappe.io/framework/v13/user/en/basics)
- [Frappe CRM Docs](https://docs.frappe.io/crm/introduction)
- [WhatsApp Business API Docs](https://developers.facebook.com/docs/whatsapp)

### Comunidad

- [Frappe Forum](https://discuss.frappe.io/)
- [GitHub Issues](https://github.com/tu-usuario/crm-custom-whatsapp/issues)
- [Discord Community](https://discord.gg/frappe)

### Contacto

- **Email**: xappiens@xappiens.com
- **Website**: [Xappiens](https://xappiens.com)

## 🔄 Changelog

### v1.0.0 (2024-01-15)

- ✨ Implementación inicial
- ✨ Menú lateral personalizado
- ✨ Lista de conversaciones de WhatsApp
- ✨ Integración con WhatsApp Business API
- ✨ Interfaz de usuario responsiva

## 🗺️ Roadmap

### Próximas Versiones

#### v1.1.0

- [ ] Notificaciones en tiempo real
- [ ] Plantillas de mensajes
- [ ] Etiquetas y categorización
- [ ] Exportación de conversaciones

#### v1.2.0

- [ ] Integración con otros canales (Telegram, SMS)
- [ ] Analytics y reportes
- [ ] Automatización de respuestas
- [ ] API REST completa

#### v2.0.0

- [ ] Interfaz de chat en tiempo real
- [ ] Soporte para multimedia
- [ ] Integración con IA para respuestas automáticas
- [ ] Dashboard de métricas avanzado

---

**Desarrollado con ❤️ por Xappiens**
