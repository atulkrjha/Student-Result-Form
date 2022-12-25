from django.forms import ModelForm, SelectDateWidget, CheckboxSelectMultiple, RadioSelect, DateInput
from django.contrib.admin.widgets import AdminDateWidget
from .models import StudentDetail, ResultDetail
from datetime import date
from django.utils.safestring import mark_safe


class DateInput(DateInput):
    input_type = 'date'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.attrs.setdefault('min', '1900-01-01')

class StudentDetailForm(ModelForm):

     
    class Meta:
        model = StudentDetail
        fields = ("__all__")
        widgets = {
            'dob': DateInput(),
            #SelectDateWidget(years = list(range(1900, date.today().year-4))),
            'gender' : RadioSelect()
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = "Enter your Full name (Max 40 chars)"
        self.fields['studentclass'].widget.attrs['placeholder'] = "Choose Student Class"
        self.fields['rollno'].widget.attrs['placeholder'] = "Enter Roll no (only numbers) & Unique for student"
        self.fields['gender'].widget.attrs['placeholder'] = "Select Gender"
        self.fields['studentclass'].empty_label = "Choose Student Class"
        self.fields['mobilenumber'].widget.attrs['placeholder'] = "Enter Mobile number (format : 123-456-1234)"


class ResultDetailForm(ModelForm):

     
    class Meta:
        model = ResultDetail
        fields = ("__all__")
        
        """widgets = {
            'student': CheckboxSelectMultiple
        }"""


        