from django import forms

from student.models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields="__all__"
        widgets={
            "first_name":forms.TextInput(attrs={"class":"form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.TextInput(attrs={"class": "form-control"}),

            "phone_number": forms.NumberInput(attrs={"class": "form-control"}),
            "address1": forms.TextInput(attrs={"class": "form-control"}),
            "address2": forms.TextInput(attrs={"class": "form-control"}),

        }
