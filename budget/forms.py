
from django import forms

from budget.models import Expense

class ExpenseForm(forms.ModelForm):

    class Meta:

        model=Expense

        exclude=("id","created_date")

        widgets={

            "title":forms.TextInput(attrs={"class":"form-control"}),

            "amount":forms.NumberInput(attrs={"class":"form-control"}),

            "category":forms.Select(attrs={"class":"form-control form-select"}),

            "owner":forms.TextInput(attrs={"class":"form-control"}),

            "priority":forms.Select(attrs={"class":"form-control form-select"})
        }

    


