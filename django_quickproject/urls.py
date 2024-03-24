from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from users.api.views import GerenteGeralViewSet, GerenteLocalViewSet
from estacionamentos.api.views import EmpresaViewSet, EstacionamentoViewSet, LocacaoViewSet

router = DefaultRouter()

router.register("GerenteGeral", GerenteGeralViewSet, basename="GerenteGeral")
router.register("GerenteLocal", GerenteLocalViewSet, basename="GerenteLocal")
router.register("api/empresas", EmpresaViewSet, basename="empresa-view-set")
router.register("api/estacionamentos", EstacionamentoViewSet, basename="estacionamento-view-set")
router.register("api/lotacoes", LocacaoViewSet, basename="lotacao-view-set")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/token-auth/", views.obtain_auth_token),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]+router.urls
