from django.urls import path, include
from .views import index, StudentListView, result_add_index, result_add_pk

urlpatterns = [
    path('', index, name='addstudent'),
    path('details/', StudentListView, name = 'studentlist'),
    path('resultadd/', result_add_index, name='resultaddindex'),
    path('resultadd/<int:pk>', result_add_pk, name='resultaddpk')

]

handler404 = 'studentDetails.views.error_404_view'