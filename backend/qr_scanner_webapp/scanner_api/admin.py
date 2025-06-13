from django.contrib import admin
from .models import ScanLog

# Set the ScanLog table to save logs each time someone's scan a QR
@admin.register(ScanLog) 
class ScanLogAdmin(admin.ModelAdmin):
    # Items to show (columns of the table)
    list_display = ('user_email', 'qr_content', 'to_email', 'timestamp')
    
    # First field = ForeignKey (user.email)
    # Fields allowed to be used to search
    search_fields = ('user__email', 'qr_content', 'to_email')
    
    # Lateral filters (to quickly query all the items)
    list_filter = ('timestamp', 'user')
    
    # Order the table by timestamp (DESCENDANT) (tuple)
    ordering = ('-timestamp',) 

    def user_email(self, obj):
        return obj.user.email