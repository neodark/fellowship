# myapp/mongoadmin.py

# Import the MongoAdmin base class
from mongonaut.sites import MongoAdmin

# Import your custom models
from core.models import User
from bubbles.models import Bubble

# Subclass MongoAdmin and add a customization
class BubbleAdmin(MongoAdmin):
    # Searches on the names
    search_fields = ('description', 'author')
    # list names
    list_fields = ('description', "created_at", "attendees", "author")
    def has_view_permission(self, request):
        return True
    def has_edit_permission(self, request):
        return True
    def has_add_permission(self, request):
        return True
    def has_delete_permission(self, request):
        return True

# Instantiate the MongoAdmin class
# Then attach the mongoadmin to your model
Bubble.mongoadmin = BubbleAdmin()
