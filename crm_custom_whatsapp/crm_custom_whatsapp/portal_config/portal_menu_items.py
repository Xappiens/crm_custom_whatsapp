import frappe

def get_portal_menu_items():
    """Get portal menu items for WhatsApp Management"""
    return [
        {
            "title": "WhatsApp Management",
            "route": "/app/whatsapp-management",
            "icon": "fa fa-whatsapp",
            "color": "#25D366",
            "description": "Gestiona tus conversaciones de WhatsApp"
        }
    ]
