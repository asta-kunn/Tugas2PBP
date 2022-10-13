
## README TUGAS 6

## 1. Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.
    Synchronus web communication : setiap ada event atau request dari user ke server, maka user menunggu dari server untuk mengenerate yang di req tersebut. Kalau di slide urutan nya : user klick, menunggu server untuk request selanjutnya, refresh halaman (response)

    Asynchronous : gunain ajax asynchronous javascript dan xml. Di sini ada partial page untuk bagian yang diminta saja, jadi gak ngejalanin keseluruhan dari halaman. Bisa sih berinteraksi tapi pada saat loding sm download. Jadi user dapat berinteraksi tanpa harus menunggu page ngerefresh secara keseluruhan

## 2. Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.
    Event-Driven Programming adalah  paradigma pemrograman di mana eksekusi program ditentukan oleh peristiwa pengguna baru (klik mouse, penekanan tombol), output sensor, atau pesan yang lewat dari program lain. Dalam program ini ada event listener klik yang mendengarkan tombol dengan id tertentu untuk melakukan fungsi tertentu. Misalnya, "create task"

## 3. Jelaskan penerapan asynchronous programming pada AJAX.
    Tambahkan <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script> ke header html. kemudian Tambahkan <script> tag di dalam badan html Anda. Tulis sintaks ajax JQuery di dalam skrip Anda, seperti $.ajax() ke POST, DELETE, dll. Ajax akan membaca event yang kita request dalam script untuk melakukan tindakan yang Anda inginkan. Tindakan dan respons/data itu akan diproses secara asinkron di server. Data akan ditampilkan di halaman tanpa perlu di refresh.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
    1. fungsi show json
    @login_required(login_url='/todolist/login/')
    def show_json(request):
        todolist_data = BarangTodolist.objects.filter(user=request.user)
        
        return HttpResponse(serializers.serialize("json", todolist_data), content_type='application/json')

    2. update fungsi show_todolist
    @login_required(login_url='/todolist/login/')
        def show_todolist(request):
        context = { 
            "nama": request.user,
        }
        return render(request, "todolist.html", context)

    3. menambahkan script ajax ke base 
     <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
    
    4. membuat fungsi add_task_ajax untuk posting data dengan Ajax
    @login_required(login_url='/todolist/login/')
    def add_task_ajax(request):
    if request.method ==  "POST":
            title = request.POST.get("title")
            description = request.POST.get("description")
            user = request.user
            data = BarangTodolist.objects.create(user=user, title=title, description=description, date=datetime.datetime.today())    
            return JsonResponse({
                "pk": data.pk,
                "fields": {
                    "title": data.title,
                    "description": data.description,
                    "status": data.status,
                    "date": data.date,
                },
            },
            status=200,
            )
    
    5. todolist.html
![image](./assets/tugas61.png)
![image](./assets/tugas62.png)
![image](./assets/tugas63.png)
![image](./assets/tugas64.png)
![image](./assets/tugas65.png)
![image](./assets/tugas66.png)
![image](./assets/tugas67.png)

