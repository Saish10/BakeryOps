

class BrandingManager:
    """
    Manager for tenant branding
    """
    def __init__(self, request):
        self.request = request

    def get_tenant_branding(self):
        """
        Get tenant branding
        """
        #get tenant from domain url
        