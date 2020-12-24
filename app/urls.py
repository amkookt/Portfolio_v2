from django.urls import path
from .views import IndexView,AboutView,ProjectView,DetailProjectView,UpdateAboutView,UpdateProjectView,contact,CreateProjectView,CreateServiceView,DeletingView,UpdateServiceView


urlpatterns = [
    
    path('',IndexView.as_view(),name='home'),
    path('about',AboutView.as_view(),name='about'),
    path('projects',ProjectView.as_view(),name='project'),
    path('Create',CreateProjectView.as_view(),name='create'),
    path('Create_service',CreateServiceView.as_view(),name='Create_service'),
    path('details/<int:pk>',DetailProjectView.as_view(),name='detail'),
    path('update/<int:pk>',UpdateProjectView.as_view(),name='update'),
    path('update_about/<int:pk>',UpdateAboutView.as_view(),name='update_about'),
    path('update_service/<int:pk>',UpdateServiceView.as_view(),name='update_service'),
    path('delete/<int:pk>',DeletingView.as_view(),name='delete'),
    path('contact',contact,name='contact'),
    
]
