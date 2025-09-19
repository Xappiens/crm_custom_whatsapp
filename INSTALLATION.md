# Instalación de CRM Custom WhatsApp

## 📋 Requisitos Previos

- Frappe Framework 15.0+
- Frappe CRM instalado
- Python 3.10+
- MariaDB 10.3+

## 🚀 Instalación

### 1. Instalar la aplicación

```bash
# Navegar al directorio de Bench
cd /ruta/a/tu/bench

# Obtener la aplicación
bench get-app crm_custom_whatsapp /ruta/al/repositorio

# Instalar en el sitio
bench --site tu-sitio.local install-app crm_custom_whatsapp
```

### 2. Migrar la base de datos

```bash
bench --site tu-sitio.local migrate
```

### 3. Reiniciar el servidor

```bash
bench --site tu-sitio.local restart
```

## 🎯 Uso

### Acceder al Menú de WhatsApp

1. Iniciar sesión en Frappe CRM
2. En la barra lateral izquierda, buscar el ícono de **WhatsApp** (color verde)
3. Hacer clic en "WhatsApp Management"

### Funcionalidades Disponibles

- **Dashboard**: Vista general de estadísticas de WhatsApp
- **Configuración**: Configurar la integración con WhatsApp
- **Estadísticas**: Ver métricas de conversaciones
- **Estado**: Verificar el estado de la integración

## 🔧 Configuración

### Configurar WhatsApp Management

1. Acceder a la página de WhatsApp Management
2. Hacer clic en "Configure WhatsApp"
3. Ingresar las credenciales de WhatsApp Business API
4. Guardar la configuración

### Permisos

La aplicación crea automáticamente los permisos necesarios para:

- System Manager: Acceso completo
- Usuarios regulares: Acceso de solo lectura

## 🐛 Solución de Problemas

### El menú no aparece

1. Verificar que la aplicación esté instalada correctamente
2. Verificar que el usuario tenga permisos adecuados
3. Limpiar caché del navegador

### Error de página no encontrada

1. Verificar que la migración se haya ejecutado correctamente
2. Reiniciar el servidor Frappe
3. Verificar los logs de error

## 📞 Soporte

Para soporte técnico, contactar a:

- Email: xappiens@xappiens.com
- GitHub Issues: [Crear un issue](https://github.com/tu-usuario/crm-custom-whatsapp/issues)
