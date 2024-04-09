from django.shortcuts import render

from django.views.generic import View

from budget.forms import ExpenseForm


class ExpenseCreateView(View):

    def get(self,request,*args,**kwargs):

        form_instance=ExpenseForm()

        return render(request,"expense_add.html",{"form":form_instance})
    


