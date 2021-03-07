from django.template.loader import get_template
from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context
import datetime
import django
from django.db.models import Q
# django.setup()
from django import forms
from myDjangoProject.models import Libro

def current_datetime(request):
    print("ehecyta current_datetime")
    now = datetime.datetime.now()
#    html = "<html><body>It is now %s.</body></html>" % now
    fp = open('/opt/systems/django-demo/myDjangoProject/template.html')
    t = Template(fp.read())
#    t = Template("<html><body>It is now {{ current_date }}.</body></html>")
    html = t.render(Context({'current_date': now}))

    return HttpResponse(html)


def hours_ahead(request, offset):
    print("ejecuta ahead")
    offset = int(offset)
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s</body></html>" % (offset, dt)
    return HttpResponse(html)


def home(request, nombre=''):
    if nombre:
        nombre = str(nombre)
    else:
        nombre = ''
    return render(request, "inicio.html", {'nombre': nombre})


def search(request):
    print("se ejecuta search")
    query = request.GET.get('q', '')
    if query:
        qset = (
            Q(titulo__contains=query) |
            Q(autores__nombre__contains=query) |
            Q(autores__apellido__contains=query)
            )
        results = Libro.objects.filter(qset).distinct()
    else:
        results = []
    return render(request, "search.html", {'results': results, 'query': query})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
    else:
        form = ContactForm(request)
    return render(request, 'contact.html', {'form': form})


class ContactForm(forms.Form):
    TOPIC_CHOICES = (
        ('general', 'General enquiry'),
        ('bug', 'Bug report'),
        ('suggestion', 'Suggestion')
    )

    topic = forms.ChoiceField(choices=TOPIC_CHOICES)
    message = forms.CharField(widget=forms.Textarea())
    sender = forms.EmailField(required=False)
