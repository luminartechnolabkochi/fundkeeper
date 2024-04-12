from django.shortcuts import render,redirect

from django.views.generic import View

from budget.forms import ExpenseForm

from budget.models import Expense



class ExpenseCreateView(View):

    def get(self,request,*args,**kwargs):

        form_instance=ExpenseForm()

        # orm qury for fecthing all expenses

        qs=Expense.objects.all()


        return render(request,"expense_add.html",{"form":form_instance,"data":qs})
    
    def post(self,request,*args,**kwargs):

        form_instance=ExpenseForm(request.POST)

        if form_instance.is_valid():

            form_instance.save()

            print("expense has been created")

            return redirect("expense-add")
        else:
            return render(request,"expense_add.html",{"form":form_instance})
    


