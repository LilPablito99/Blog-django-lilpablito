from django.contrib import admin
from django.urls import path, include
from perfiles.views import SignUpView, BienvenidaView,SignInView,SignOutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', BienvenidaView.as_view(), name='bienvenida'),
    path('registrate/', SignUpView.as_view(), name='sign_up'),
    path('incia-sesion/', SignInView.as_view(), name='sign_in'),
    path('cerrar-sesion/', SignOutView.as_view(), name='sign_out'),
    path('post/', include('posts.urls'))
    
]
