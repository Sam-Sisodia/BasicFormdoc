from ctypes import resize
from distutils.command.clean import clean
from wsgiref.validate import validator
from django import forms



class BasicForm(forms.Form):
    name = forms.CharField()

    Email =forms.EmailField()
    
    key  = forms.CharField(widget=forms.HiddenInput())

    name = forms.CharField(min_length=10,max_length=20,strip=True)

    name = forms.CharField(error_messages={'required': 'Enter your name pls '})

    Agree = forms.BooleanField(label="I Agree" )
    roll = forms.IntegerField(min_value=10, max_value=20)
    price= forms.DecimalField(min_value=10, max_value=20)
    comment = forms.SlugField()

    website = forms.URLField(min_length=20, max_length=20)

    descripion = forms.CharField(widget=forms.Textarea)

    feedback = forms.CharField(min_length=20,widget=forms.Textarea(attrs={'rows':3 ,'cols':50}))

      

      #validate field

    def clean_name(self):
        valname= self.cleaned_data['name']
        if len(valname)<4:
            raise forms.ValidationError("Eneter more then or equal to 4 charecter")
        return valname

    def clean(self):
        cleaned_data = super().clean()
        valname = self.cleaned_data['name']
        if len(valname)<4:
            raise forms.ValidationError("Eneter more then or equal to 4 charecter")
        valemail = self.cleaned_data['email']
        if len(valemail)>10:
            raise forms.ValidationError("Email should be more then or equal 10 ")
       
        

    #builtin validator

    name = forms.CharField(validators=[validator.MaxLengthValidator(10)])

    password = forms.CharField(widget=forms.PasswordInput)
    repassword = forms.CharField(widget=forms.PasswordInput)


    def clean(self):
        clean_data = super().clean()

        valpwd = clean_data['password']
        valrpwd = clean_data['repassword']

        if valpwd !=valrpwd:
            raise  forms.ValidationError("password Not match")










'''

FORM FIELD TYPE

name = forms.CharField(strip=True)   -Use for trim the space 

name = forms.CharField(empty_value="sjal")     - give default value 

name = forms.CharField(min_length=10,max_length=20,strip=True)

name = forms.CharField(error_messages={'required': 'Enter your name pls '})


#BoolField 


'''




#form  method 
'''  

{{form }}   - wll render  them all 
{{form.as_p}}
{{form.as_table}}
{{form_as_ul}}
{{form.as_name_of_field}} will render field menually as given {{form.name}} ,{{form.email}}

'''


##############
'''
for loop in form

{% for i in  form %}
{{form.name }}         ,   {{i}}

{% endfor%}


Therse form  loop show all the filds in our page if we hide input fields we must use the loppl
like 

{%  for i in form.hideen_fields  %}
{{i}}  - it hide that field which is hidden in form (check Key in form )



'''




#############
'''
FORM  FIELD


name = forms.CharField(label="FIRSTNAME")

name = forms.CharField(label_suffix= " $" )

name = forms.CharField()


name = forms.CharField(label="FIRSTNAME",label_suffix= " $" , initial = "sonam" ,
                        required= False , desable = True , help_text="limit 20 char" 
                         )

WIDGET -Work like input tag in  html

name = forms.CharField(wedget=forms.PasswordInput)
name = forms.CharField(wedget=forms.HiddenInput)
name = forms.CharField(wedget=forms.Textarea)
name = forms.CharField(wedget=forms.CheckBoxInput)
name = forms.CharField(wedget=forms.FileInput)

USE Of attrs - we use this to give extra attribute in our form field like -class,id or use of css

name = forms.CharField(wedget=forms.TextInput(attrs={'class':'class1 , 'id' : 'sajal' }))

'''



###################################

'''

cLEAN AND VAIDATING SPECIFIC FIELD 

name = forms.CharField()
    def clean_name(self):
        valname= self.cleaned_data['name']
        if len(valname)<4:
            raise forms.ValidationError("Eneter more then or equal to 4 charecter")
        return valname



# - Validate all the fields at a one time 


    def clean(self):
        cleaned_data = super().clean()
        valname = self.cleaned_data['name']
        if len(valname)<4:
            raise forms.ValidationError("Eneter more then or equal to 4 charecter")
        valemail = self.cleaned_data['email']
        if len(valemail)>10:
            raise forms.ValidationError("Email should be more then or equal 10 ")


#builtin validator

    name = forms.CharField(validators=[validator.MaxLengthValidator(10)])



#CREATE  CUSTOME FORM VALIDATOR 



def start_with_s(value):
    if value[0] != 's':
        raise forms.ValidationError('Name Should be start with s )


class Studentreg(forms.Form):
    name = forms.CharField(validators=[start_with_s ] )



# FORM  VALIDATOR MATCH  TWO FIELDS 



name = forms.CharField(validators=[validator.MaxLengthValidator(10)])

    password = forms.CharField(widget=forms.PasswordInput)
    repassword = forms.CharField(widget=forms.PasswordInput)


    def clean(self):
        clean_data = super().clean()

        valpwd = self.clean_data['password']
        valrpwd = self.clean_data['repassword']

        if valpwd !=valrpwd:
            raise  forms.ValidationError("password Not match

'''



#  MODEL  FORM  ###

'''
override model field 
#if we set max_lenth 20 in model we can change it own form -form priority is high 

class StudentRegister(forms.ModelForm):
    name  = form.CharField(max_length=10, required=True)
    class Meta:
        model = Student 
        fields = ['name','email' ,'password']





class   Studentreg(forms.ModelForm):
    class  Meta:
        model = User
        fields = ['name','email',]


        #for label (user labels not label)
        labels = {'name':'Enter the Name', 'email':'enter the email' ,}

        help_text = {'name':'Enter your name '}

        error_messages = {'name': {'required' : 'name  is manadatory','max_length':'20'},
                           'password' :{'required' :'Password is Mandatory'} ,
                           'address'  : {'required' : 'addrss can be empty ' },
                                                                    }


        widgets = {'password':'forms.PasswordInput,
                   'name':forms.TextInput(attrs={'class' : 'myclass' , 'placeholder':'Enter 
                   name here'})}






#SELECTING FIELDS 


class StudentRegister(forms.ModelForm):
    class Meta:
    model  =User
   exclude = ['name'] 


#########################################

##MODEL FORM  INHERTANCE 
class User(models.Model):
    student_name = models.CharFied(max_langth=10)
    teacher_name = models.CharFied(max_langth=10)
    email = models.CharFied(max_langth=10)
    password = models.CharFied(max_langth=10)



class studentregister(forms.ModelForm):
    class Meta:
        Model=User
        fields =  ['student_name','email','password']


class TeacherRegistarion(studentregister):       
        class Meta()studentregister.Meta:         #we also inhert user model also
            fields=['teacher_name',]


'''