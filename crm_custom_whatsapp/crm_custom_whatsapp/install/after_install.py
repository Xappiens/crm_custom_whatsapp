import frappe

def after_install():
    """After installation tasks"""
    # Create default WhatsApp Management settings
    create_default_settings()

    # Set up permissions
    setup_permissions()

def create_default_settings():
    """Create default WhatsApp Management settings"""
    if not frappe.db.exists("WhatsApp Management", "WhatsApp Management"):
        settings = frappe.new_doc("WhatsApp Management")
        settings.title = "WhatsApp Management"
        settings.description = "Configuración principal para la gestión de WhatsApp"
        settings.status = "Inactive"
        settings.enabled = False
        settings.insert(ignore_permissions=True)

        frappe.msgprint("WhatsApp Management settings created successfully!")

def setup_permissions():
    """Set up basic permissions for the module"""
    # This will be handled by the DocType permissions
    pass
