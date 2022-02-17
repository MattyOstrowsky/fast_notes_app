
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from notes import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('note/', views.getNotes, name="notes"),
    path('note/<str:pk>/', views.getNote, name="note"),
]

urlpatterns += [
    re_path(r'^.*', TemplateView.as_view(template_name='index.html'))
]