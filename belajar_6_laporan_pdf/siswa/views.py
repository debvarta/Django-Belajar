from django.shortcuts import render
#print modul
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML
#Import Model Siswa
from .models import SiswaModel
# Create your views here.
def index(request):
    
    return render(request, 'siswa/index.html')

def print(request):
    AllSiswa=SiswaModel.objects.all()
    context = {
        "AllSiswa":AllSiswa
    }

    html_string = render_to_string('siswa/pdf_template.html',context)
    html = HTML(string=html_string, base_url=request.build_absolute_uri())
    html.write_pdf(target='/tmp/mypdf.pdf');
    fs = FileSystemStorage('/tmp')
    with fs.open('mypdf.pdf') as pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'filename=Report.pdf'
        return response

    return response
