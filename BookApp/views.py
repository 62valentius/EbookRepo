import os.path

from django.http import FileResponse
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from .models import Book
from .forms import UploadBookForm
from django.http import HttpResponse

# Create your views here.
class CreateBookView(CreateView):
    model = Book
    fields = '__all__'

def uploadBookView(request):
    form = UploadBookForm()
    if request.method == 'POST':
        print(request.POST)
        print(request.FILES['pdf'])
        form = UploadBookForm(request.POST,request.FILES)
        form.save()
        return redirect('all_books')
    template_name = 'BookApp/book_form.html'
    context = {'form':form}
    return render(request,template_name,context)

def allBooksView(request):
    books = Book.objects.all()
    template_name = 'BookApp/book_list.html'
    context = {'books':books}
    return render(request,template_name,context)

def showBookView(request):
    filepath = os.path.join("media","VaibhavFH.pdf")##toolbar=0")
    '''
    print(filepath)
    template_name = 'BookApp/book_show.html'
    context = {"file":open(filepath,"rb").read()}
    return render(request, template_name,context,content_type="application/pdf")
    # return HttpResponse(open(filepath,"rb"),content_type="application/pdf")
   
    with open(filepath, 'rb') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        # response['Content-Disposition'] = 'filename=some_file.pdf#toolbar=0'
        response['#toolbar'] = 0
        # response["Content-Disposition"]="toolbar=0"
        # response['Content-Disposition'] = 'inline;filename=some_file.pdf'
        # print(response.content)
        response.setdefault("#toolbar",0)
        print(response.headers)
        return response
    '''
    template_name = 'BookApp/book_show.html'
    context = {"filepath":filepath}
    return render(request, template_name,context)


