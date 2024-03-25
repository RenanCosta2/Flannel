from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from users.api.views import GerenteGeralViewSet, GerenteLocalViewSet
from estacionamentos.api.views import EmpresaViewSet, EstacionamentoViewSet, LocacaoViewSet

router = DefaultRouter()

# Rotas dos gerentes
router.register(r"GerenteGeral", GerenteGeralViewSet, basename="GerenteGeral")
router.register(r"GerenteLocal", GerenteLocalViewSet, basename="GerenteLocal")

# Rotas do estacionamento
router.register(r"empresas", EmpresaViewSet, basename="empresas")
router.register(r"estacionamentos", EstacionamentoViewSet, basename="estacionamentos")
router.register(r"lotacoes", LocacaoViewSet, basename="lotação")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/token-auth/", views.obtain_auth_token),
    path('api/', include(router.urls)),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]
