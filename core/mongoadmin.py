# myapp/mongoadmin.py

# Import the MongoAdmin base class
from mongonaut.sites import MongoAdmin

# Import your custom models
from core.models import Post, Tag, Comment
from core.views import PostListView

# Subclass MongoAdmin and add a customization
class PostAdmin(MongoAdmin):

    # Searches on the title field. Displayed in the DocumentListView.
    search_fields = ('title',)

    # provide following fields for view in the DocumentListView
    #list_fields = ('title', "published", "pub_date")
    list_fields = ('title', "text", "is_published")
    def has_view_permission(self, request):
        return True
    def has_edit_permission(self, request):
        return True
    def has_add_permission(self, request):
        return True
    def has_delete_permission(self, request):
        return True

class TagAdmin(MongoAdmin):

    # Searches on the title field. Displayed in the DocumentListView.
    search_fields = ('title',)

    # provide following fields for view in the DocumentListView
    #list_fields = ('title', "published", "pub_date")
    list_fields = ('title')

class CommentAdmin(MongoAdmin):

    # Searches on the title field. Displayed in the DocumentListView.
    search_fields = ('text',)

    # provide following fields for view in the DocumentListView
    #list_fields = ('title', "published", "pub_date")
    list_fields = ('text')


# Instantiate the PostAdmin subclass
# Then attach PostAdmin to your model
# Instantiate the MongoAdmin class
# Then attach the mongoadmin to your model
Post.mongoadmin = PostAdmin()
Tag.mongoadmin = TagAdmin()
Comment.mongoadmin = CommentAdmin()
PostListView.mongoadmin = MongoAdmin()
