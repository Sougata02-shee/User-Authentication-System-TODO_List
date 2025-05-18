from django import forms
from .models import TaskModel

class TaskForm(forms.ModelForm):
    class Meta:
        model=TaskModel
        fields='__all__'
        widgets={
            'host':forms.TextInput(attrs={'type':'hidden'})
        }

    img=forms.ImageField(required=False)