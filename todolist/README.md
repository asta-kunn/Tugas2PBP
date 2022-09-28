# Live Demo Link 🚀
[TODOLIST page 💻]


## Apa kegunaan {% csrf_token %} pada elemen <form>? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?
    django memiliki tag {% csrf_token %} untuk menghindari serangan terhadap web aplication yang memanfaatkan bug atau vulnerability pada Web Application yang bekerja dengan cara mengeksploitasi suatu task dari sebuah Web dengan memanfaatkan Autentikasi yang dimiliki oleh korban. Hal ini biasanya di karenakan kode yang sangat buruk sewaktu developmentya sehingga menghasilkan bug tersebut yang dapat di salah gunakan oleh orang lain dengan maksud negatif. Django membuat proses ini mulus dengan penambahan tag sederhana ke form yang dihasilkan. Untuk menggunakanya sangat simple kita hanya perlu menyisipkanya di dalam <form> yang ingin kita insert atau update delete. apabila tidak ada potongan kode ini, serangan csrf tidak dapat dihindari senhinga mengancam keamanan post request dari user ke server

## Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual.
    Jawabannya mungkin bisa-bisa saja. Jika kita membuat elemen <form> tanpa menggunakan {{ form.as_table }} mungkin ada beberapa variable yang ada di database tidak memerlukan di-POST sehingga kita dapat membuat form manual untuk mengatasi hal tersebut. Kita harus menambahkan method post di form manual dan akan diisi csrf token. Kemudian kita harus melengkapi tag input sesuai dengan kebutuhan dan name untuk identifier. Form akan mengakses input ketika user mengklik submit dengan menggunakan method request.POST.get()

##  Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.

    1. user menekan tombol submit
    2. form mengakses data input dengan menggunakan method request.POST.get()
    3. membuat objek baru yang aan disimpan ke database dengan cara data = BarangTodolist(user=user, title=title, description=description)
    4. kita dapat mengakses data yang tersimpan di database django dengan cara "Models".objects.filter(user=request.user) 
    5. deliver data kedalam context dan kita return render dengan target html, setelah itu di html kita langsung bisa mengiterasi data menggunakan loop seperti yang diajarkan di lab dan data akan ditampilkan pada html

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
    1. Ketik di terminal directory Tugas2PBP python manage.py startapp todolist 

    2. nambahin path('todolist/', include('todolist.urls')), ke urls.py yang ada di project django

    3. Membuat class di todolist/models.py dan membuatnya field sesuai kriteria yang diminta

    4. buat fungsi login,logout,register yang dapat dihubungkan ke login.html dan register.html. kurang lebih sama kayak pengerjaan tutorial lab 3

    5. Kita akan membuat variable context yang akan menyimpan data-data yang diperlukan untuk ditampilkan pada html. pada todolist.html kita harus menampilkan data dengan cara mengiterasi field yang ada di model menggunakan for each loop kemudian menambahkan 2 buah button untuk create-task dan logout. Kemudian membuat tabel untuk menampilkan data-datanya. kurang lebih codingannya adalah :
    {% for todolist in todo_list %}
    <tr>
        <th>{{todolist.title}}</th>
        <th>{{todolist.date}}</th>
        <th>{{todolist.description}}</th>
        {% if todolist.status == False %}
        <th>Belum Selesai</th>
        {% else %}
        <th>Selesai</th>
        {% endif %}
        <th><a href="{% url 'todolist:cheklist' todolist.id %}"><button>Check</button></th>
        <th><a href="{% url 'todolist:hapus' todolist.pk%}"><button>Delete</button></th>
    </tr>
    {% endfor %}

    6. Pada create-task.html kita perlu menambahkan form input tittle dan description seperti ini:
        <tr>
            <td>Tittle: </td>
            <td><input type="text" name="title" placeholder="TITTLE" class="form-control"></td>
        </tr>
                
        <tr>
            <td>Description: </td>
            <td><input type="text" name="description" placeholder="DESCRIPTION" class="form-control"></td>
        </tr>
    kita juga harus menambahkan button submit buat yang akan diikirim ke fungsi tambah_input di views.py untuk ditambahkan kke database

    7. sama seperti point 2 tadi, kita akan menambahkan routing path /todolist/login,register,create-task,logout

## Akun dummy
    Akun 1 :
    ussername = icuncantik
    password = pbp@2022
    akun 2 :
    ussername : icunburik
    password = pbp@2022