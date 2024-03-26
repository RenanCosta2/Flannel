from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from users.api.views import GerenteGeralViewSet, GerenteLocalViewSet
from estacionamentos.api.views import EmpresaViewSet, EstacionamentoViewSet, LocacaoViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()

# Rotas dos gerentes
router.register(r"gerentegeral", GerenteGeralViewSet, basename="gerente_geral")
router.register(r"gerentelocal", GerenteLocalViewSet, basename="gerente_local")

# Rotas do estacionamento
router.register(r"empresas", EmpresaViewSet, basename="empresas")
router.register(r"estacionamentos", EstacionamentoViewSet, basename="estacionamentos")
router.register(r"lotacoes", LocacaoViewSet, basename="lotação")

urlpatterns = [
    path("admin/", admin.site.urls),
    #path("api/token-auth/", views.obtain_auth_token),
    #Rota de autenticação JWT.
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    #Rota para consumir a API do DRF
    path('api/', include(router.urls)),
    #Rota de documentação
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]
