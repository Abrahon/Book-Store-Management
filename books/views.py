from django.shortcuts import render,redirect
from books.forms import bookStoreForm
from books.forms import BookStoreModel
from django.views.generic import TemplateView

# Create your views here.
# function base view

# def home(request):
#     return render(request,'store_book.html')

# class base view
class MyTemplateView(TemplateView):
    template_name = 'home.html'
    def get_context_data(self , **kwargs):
        context = super().get_context_data()
        context = {'name' : 'Sujon', 'age': 21}
        print(context)
        context.update(kwargs)
        print(context)
        return context
    
def home(request) :
    return render(request,'home.html')      
   
def store_book(request):
    if request.method == 'POST':
        book =bookStoreForm(request.POST) 
        if book.is_valid():
            book.save(commit=True)
            print(book.cleaned_data)
            return redirect('show_book')
            
    else:
        book =bookStoreForm() 
    return render(request,'store_book.html',{'form':book})

def show_book(request):
    book = BookStoreModel.objects.all()
   
    print(book)
    return render(request,'show_book.html',{'data':book})

def edit_book(request, id):
    book = BookStoreModel.objects.get(pk=id)
    form = bookStoreForm(instance=book)
    if request.method == 'POST':
        form =bookStoreForm(request.POST,instance=book) 
        if form.is_valid():
            form.save(commit=True)
            return redirect('show_book')
    return render(request,'store_book.html',{'form':form})

def delete_book(request,id):
    book = BookStoreModel.objects.get(pk=id).delete()
    return redirect('show_book')
  
    
