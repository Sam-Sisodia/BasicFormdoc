
from django.shortcuts import render

# Create your views here.
from . form import *



'''
def  basicform(request):
    if request.method =="POST":
        form = BasicForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            print(name)
            return render(request, "yes.html")'''
    
      

    


def  basicform(request):
    form = BasicForm()
    return render(request, "wel.html",{'form':form})


''''
    THESE ALL ARE DEFINE IN VIEW.PY FILE 
    
    #configure Id of form

    form = BasicForm(auto_id='some_%s) 
    form = BasicForm(auto_id=True) 
    form = BasicForm(auto_id=False)
    form = BasicForm(auto_id="sajal")      work as  true

    #configure label tag 
    
    form = BasicForm(label_suffix= " -")  #add symbol to allof your label'


    # initial value give in your form -show defalut value if your form 
    form = BasicForm(iniial = {'name': "sajal', 'email':"saja@yga.com" , }


    ==================================================================
    form = BasicForm(auto_id=True,label_suffix="$" , intial={'name':'sajal" })


    #ordering form
    form.order_firelds(field_order=['email','name' ,'mobno'])

    
    
    '''