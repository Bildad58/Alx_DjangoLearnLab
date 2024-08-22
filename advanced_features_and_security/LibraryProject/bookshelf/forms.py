from django import forms
from .models import Student

class BookForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["name", "age", "date_of_admission", "isbn"]
        widget = {
            "admission_date": forms.DateInput(attrs={"type":"date"}),
        }
