from django.urls import path
from todolist.views import show_todolist, tambah_input, hapus_input, cheklist_todolist, registrasi, login_user, logout_user
app_name = "todolist"
urlpatterns = [
    path('', show_todolist, name="show_todolist"),
    path('create-task/', tambah_input, name="create-task"),
    path('hapus/<int:pk>', hapus_input, name="hapus"),
    path('cheklist/<int:pk>', cheklist_todolist, name="cheklist"),
    path('registrasi/', registrasi, name="registrasi"),
    path('login/', login_user, name="login"),
    path('logout/', logout_user, name="logout"),
] 