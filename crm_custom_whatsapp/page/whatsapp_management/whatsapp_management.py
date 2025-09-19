import frappe
from frappe import _

def get_context(context):
    """Get context for WhatsApp Management page"""
    context.title = _("WhatsApp Management")
    context.breadcrumbs = [
        {"label": _("Home"), "url": "/app"},
        {"label": _("WhatsApp Management"), "url": "/app/whatsapp-management"}
    ]

    # Get WhatsApp Management settings
    try:
        whatsapp_settings = frappe.get_doc("WhatsApp Management", "WhatsApp Management")
        context.settings = whatsapp_settings
    except frappe.DoesNotExistError:
        # Create default settings if they don't exist
        context.settings = create_default_settings()

    # Get basic statistics
    context.stats = get_whatsapp_stats()

def create_default_settings():
    """Create default WhatsApp Management settings"""
    settings = frappe.new_doc("WhatsApp Management")
    settings.title = "WhatsApp Management"
    settings.description = "Configuración principal para la gestión de WhatsApp"
    settings.status = "Inactive"
    settings.enabled = False
    settings.insert(ignore_permissions=True)
    return settings

def get_whatsapp_stats():
    """Get basic WhatsApp statistics"""
    return {
        "total_conversations": 0,
        "active_conversations": 0,
        "last_sync": None,
        "status": "Inactive"
    }
