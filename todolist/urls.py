from django.urls import path
from todolist.views import show_todolist, tambah_input, hapus_input, cheklist_todolist, registrasi, login_user, logout_user, show_json, add_task_ajax
app_name = "todolist"
urlpatterns = [
    path('', show_todolist, name="show_todolist"),
    path('create-task/', tambah_input, name="create-task"),
    path('hapus/<int:pk>', hapus_input, name="hapus"),
    path('cheklist/<int:pk>', cheklist_todolist, name="cheklist"), #update
    path('register/', registrasi, name="register"),
    path('login/', login_user, name="login"),
    path('logout/', logout_user, name="logout"),
    path('json/', show_json, name='show_json'),
    path('add/', add_task_ajax, name='add_task')
] 