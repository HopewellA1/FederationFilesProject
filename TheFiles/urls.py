from django.urls import path
from . import views




urlpatterns = [
    path('', views.home, name="home"),
    path('FederationCreate/', views.FederationCreate, name="FederationCreate"),
    path('createFed', views.createFed, name="createFed"),
    path('FedList', views.FedList, name="FedList"),
    path('FederationDetail/<int:pk>/', views.FederationDetail, name="FederationDetail"),
    path('viewFed/<int:fedId>',views.viewFed, name="viewFed")
    
    
	# path('', views.apiOverview, name="api-overview"),
	# path('task-list/', views.taskList, name="task-list"),
	# path('task-detail/<str:pk>/', views.taskDetail, name="task-detail"),
	# path('task-create/', views.taskCreate, name="task-create"),

	# path('task-update/<str:pk>/', views.taskUpdate, name="task-update"),
	#path('task-delete/<str:pk>/', views.taskDelete, name="task-delete"),
]
