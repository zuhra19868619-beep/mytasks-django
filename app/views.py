from django.shortcuts import render

def index(request):
    tasks = [
        {
            "title": "Python",
            "description": "Надо изучить Python, чтобы стать хорошим разработчиком"
        },
        {
            "title": "Django",
            "description": "Надо изучить Django, чтобы стать хорошим разработчиком"
        },
    ]

    if request.method == 'POST':
        title = request.POST.get('title')
        print(title)

        if title == "":
            print("Пустое поле")
        else:
            tasks.append({
                "title": title,
                "description": "Описание задачи"
            })
    context = {"tasks": tasks}
    return render(request, 'index.html', context)






