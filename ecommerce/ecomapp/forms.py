from django import forms

class registerform(forms.Form):
    username=forms.CharField(max_length=25)
    email=forms.EmailField()
    password=forms.CharField(max_length=20)
    confirmpassword=forms.CharField(max_length=20)

class loginform(forms.Form):
    username = forms.CharField(max_length=25)
    password = forms.CharField(max_length=20)

class shopform(forms.Form):
    shopname=forms.CharField(max_length=35)
    email=forms.EmailField()
    password=forms.CharField(max_length=20)
    confpassword=forms.CharField(max_length=20)

class shoploginform(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=20)


class uploadform(forms.Form):
    productname=forms.CharField(max_length=25)
    price=forms.CharField(max_length=25)
    description=forms.CharField(max_length=25)
    image=forms.ImageField()

# -----------------------------------------------------------------------------------------------------------------


# Email

class ContactusForm(forms.Form):
    Name = forms.CharField(max_length=30)
    Email = forms.EmailField()
    Message = forms.CharField(max_length=500,
                              widget=forms.Textarea(attrs={'rows':3,'cols':30}))


