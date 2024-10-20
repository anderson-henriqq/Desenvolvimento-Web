import sys  

from django.conf import settings   

from django.urls import path   

from django.http import HttpResponse   

settings.configure(DEBUG=True, SECRET_KEY='segredo', 

ROOT_URLCONF=__name__)   

def index(request):   

    return HttpResponse('<h1>Olá!</h1><h3>Digite no final da sua URL "/tabuada/x", onde o x é o número que deseja saber a tabuada<h3>') 

def tabuada(request,num): 
    
    html = '<h1>Tabuada do {} </h1>'.format(num)
    html += "<table  border='1'>"
    for i in range(1,11):
        html += '<tr> <td>{} x {}<td> <td>{}<td><tr>'.format(num, i, num*1)
    html += '</table>'
    
    return HttpResponse(html) 

   

urlpatterns = [
                path('', index),
                path('tabuada/<int:num>',tabuada)
               ]   

 
if __name__ == '__main__':   

    from django.core.management import execute_from_command_line   

    execute_from_command_line(sys.argv)   