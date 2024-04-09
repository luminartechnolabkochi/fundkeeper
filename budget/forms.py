
from django import forms

from budget.models import Expense

class ExpenseForm(forms.ModelForm):

    class Meta:

        model=Expense

        exclude=("id","created_date")

    


