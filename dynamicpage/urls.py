from . import views
from rest_framework.routers import DefaultRouter

app_name = 'dynamicpage'

router = DefaultRouter()
router.register('books', views.BookViewSet)
router.register('authors', views.AuthorViewSet)


urlpatterns = router.urls