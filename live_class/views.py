from datetime import datetime
from django.http import HttpResponse
from django.template import Template, Context

def hello_world(request):
    return HttpResponse("Hello, world. You're at the Django - CoderHouse first view.")


def segunda_vista(request):
    return HttpResponse("<br><br>Ya entendimos esto, es muy simple :) ")


def diaDeHoy(request):

        dia = datetime.now()

        documentoDeTexto = f"Hoy es día: <br> {dia}"

        return HttpResponse(documentoDeTexto)


def miNombreEs(self, nombre, edad):
    # edad = int(edad)
    documentoDeTexto = f"Mi nombre es: <br><br>  {nombre} <br><br> Mi edad multiplicada por 2: {edad*2}"

    return HttpResponse(documentoDeTexto)


def calculate_birth_year(self, age: int):
    current_year = datetime.now().year
    # birth_year = current_year - int(age)
    birth_year = current_year - age
    return HttpResponse(f"<br><br> My birth year is: {birth_year}")

def calculate_age(self, birth_day):
    birth_day = datetime.strptime(birth_day, '%Y-%m-%d')
    print(type(birth_day))
    delta_time = datetime.now() - birth_day
    days_by_year = 365.25

    http_response = '''
    <br><br>
    I'm {years} years, {months} months, {days} days old.
    '''.format(
        years=int(delta_time.days // days_by_year),
        months=int((delta_time.days % days_by_year) // 30),
        days=int((delta_time.days % days_by_year) % 30),
    )
    return HttpResponse(http_response)

def probandoTemplate(self):

    miHtml = open("/home/jfpinedap/coderhouse/class_17_Django_I/live_class/live_class/templates/template.html")

    template = Template(miHtml.read()) #Se carga en memoria nuestro documento, template1
    ##OJO importar template y contex, con: from django.template import Template, Context

    miHtml.close() #Cerramos el archivo

    miContexto = Context() #EN este caso no hay nada ya que no hay parametros, IGUAL hay que crearlo

    render = template.render(miContexto) #Aca renderizamos la plantilla en documento

    return HttpResponse(render)
