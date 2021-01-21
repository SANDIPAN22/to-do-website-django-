from django import forms
from todo_app.models import taskModel

class task_add_form(forms.ModelForm):
    class Meta():
        model=taskModel
        fields='__all__'
        