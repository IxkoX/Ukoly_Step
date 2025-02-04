from django.http import HttpResponse
from django.shortcuts import render
import random
import datetime as dt
import locale

# start serveru: python manage.py runserver

def index_page(request):
    print(request.method)
    print(request.path)
    
    number = random.randint(1, 100)
    d = dt.datetime.now()

    return HttpResponse(f'''
                        <h1>Hello From Django: {number} | {d}</h1>
                        <img src="https://picsum.photos/200/300">
                        ''')


"""
úkol: vytvořte zde view s názvem time_page
pamatujte: na vstupu musí být request a na výstupu HttpResponse
"""
def time_page(requests):
    locale.setlocale(locale.LC_TIME, 'cs_CZ.UTF-8')
    now = dt.datetime.now()
    date = now.strftime('%d. %B %Y')  # Např. "24. dubna 2024"
    time = now.strftime('%H:%M:%S')   # Např. "16:45:30"
    return render(requests, 'time_page.html', {'date': date, 'time': time})

from django.shortcuts import render
from datetime import datetime

def age_page(request):
    result = None
    error = None

    if request.method == "POST":
        year = request.POST.get("birth_year")

        # Server-side validation
        try:
            birth_year = int(year)
            current_year = dt.datetime.now().year

            if birth_year < 1900:
                error = "Již jste asi po smrti zadejte 1900–současný rok."
            elif birth_year > current_year:
                error = "Ještě jste se nenarodily zadejte menší než současný rok"
            else:
                age = current_year - birth_year
                result = f"Je vám přibližně {age} let."
        except ValueError:
            error = "Zadejte prosím číslo."

    return render(request, "age_page.html", {"result": result, "error": error})



def url_paths(requests):

    print(requests.GET)
    print(requests.GET['xyz'])
    print(requests.GET.getlist('xyz'))

    return HttpResponse('This page is working')

def my_math(request):
    """
    /my-math/?operation=plus&a=10&b=100
    operation=plus | minus | multiple | divide
    a=první číslo
    b=druhé číslo
    """

    a = int(request.GET['a'])
    b = int(request.GET['b'])
    operation = request.GET['operation']

    if operation == 'plus':
        result= a + b
    elif operation == 'minus':
        result= a-b
    elif operation == 'ultiple':
        result= a*b
    elif operation == 'divide':
        result= a/b
    return HttpResponse(f'RESULT: {result}')

def test_template(request):
    name = request.GET.get('name', 'World')
    age = request.GET.get('age', '0')
    if age == '':
        age = 0

    context = {
        'date': dt.datetime.now(),
        'name': name,
        'age' : age
    }

    return render(request, 'test_template.html', context)

def calculator(request):
    try:
        operation = request.GET['operation']
        a = int(request.GET['a'])
        b = int(request.GET['b'])
        
        if operation == 'plus':
            result = a + b
        elif operation == 'minus':
            result = a - b
        elif operation == 'multiple':
            result = a * b
        elif operation == 'divide':
            result = a / b
    except (KeyError, TypeError):
        result= ''
    except ZeroDivisionError:
        result='Division by zero is not allowed'


    context = {
        'result': result
    }


    return render(request, 'calculator.html', context)

def login (request):

    username = request.POST.get('username', '')
    password = request.POST.get('password', '')

    # print(request._body)
    print(request.FILES, '<<<< Files')
    print(request.POST)
    print(username, password)

    if username == 'fanda' and password == 'heslo':
        return render(request, 'login_success.html')

    return render(request, 'login.html')

def my_page(reqest, name):

    return render(reqest, 'my_page.html', {'name': name})

def article(reques, name, number):
    
    return HttpResponse(
        f"""
        <h1>{name} - {number}</h1>

        """
    )

def pages(reques, number, name):
    
    return HttpResponse(
        f"""
        <h1>{number} / {name}</h1>

        """
    )

    
