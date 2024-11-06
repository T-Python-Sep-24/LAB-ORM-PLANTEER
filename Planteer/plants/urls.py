from django.urls import path
from . import views

app_name = "plant"

urlpatterns = [
    path("new/", views.newPlantView, name="newPlantView"),
    # path("plantdetails/<int:plantid>/", views.plantDetailsView, name="plantDetailsView"),
    # path("update/<int:plantid>/", views.updatePlantView, name="updatePlantView"),
    # path("delete/<int:plantid>/", views.deletePlantView, name="deletePlantView"),
    # path("all/", views.allView, name="allView"),
    #path("category/<category>/", views.categoryFilterView, name="categoryFilterView"),
]