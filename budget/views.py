from django.shortcuts import render,redirect

from django.views.generic import View

from budget.forms import ExpenseForm

from budget.models import Expense

from django.contrib import messages

from django.db.models import Sum

from django.db.models.functions import TruncMonth

from django.db.models import Sum

from django.utils import timezone



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

            messages.success(request,"expense created!!")


            print("expense has been created")

            return redirect("expense-add")
        else:
            messages.error(request,"expense adding failed ")
            return render(request,"expense_add.html",{"form":form_instance})
    



# url:localhost:8000/expense/{id}/change/

class ExpenseUpdateView(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        expense_object=Expense.objects.get(id=id)

        form_instance=ExpenseForm(instance=expense_object)

        return render(request,"expense_edit.html",{"form":form_instance})
    
    
    def post(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        expense_object=Expense.objects.get(id=id)

        form_instance=ExpenseForm(instance=expense_object,data=request.POST)

        if form_instance.is_valid():

            form_instance.save()

            messages.success(request,"message changed ")

            return redirect("expense-add")
        
        else:

            messages.error(request,"updating failed")

            return render(request,"expense_edit.html",{"form":form_instance})


# expense detail view

# url:localhost:8000/expense/{id}/


class ExpenseDetailView(View):

    def get(self,request,*args,**kwargs):

        id = kwargs.get("pk")

        qs = Expense.objects.get(id=id)

        return render(request,"expense_detail.html",{"data":qs})


# url:localhost:8000/expense/{id}/remove/

class ExpenseDeleteView(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        Expense.objects.get(id=id).delete()

        messages.success(request,"expense removed")

        return redirect("expense-add")


# class ExpenseSummaryView(View):

#     def get(self,request,*args,**kwargs):

#         monthly_expenses = Expense.objects.annotate(
#             month=TruncMonth("created_date")
#         ).values("month").annotate(total_expense=Sum("amount"))

#         print(monthly_expenses)
        
#         print([expense["month"].strftime("%Y-%m") for expense in monthly_expenses])

#         return redirect("expense-add")





class ExpenseSummaryView(View):

    def get(self,request,*args,**kwargs):

        current_month = timezone.now().month

        current_year = timezone.now().year

        expense_list=Expense.objects.filter(created_date__month=current_month,
                                            created_date__year=current_year
                                            )
        
        expense_total=expense_list.values("amount").aggregate(total=Sum("amount"))

        print(expense_total)

        category_summary=expense_list.values("category").annotate(total=Sum("amount"))

        print("cat summary",category_summary)

        priority_summary=expense_list.values("priority").annotate(total=Sum("amount"))

        print("priority summary",priority_summary) 

        data={
            "expense_total":expense_total,
            "category_summary":category_summary,
            "priority_summary":priority_summary           
            }


        return render(request,"expense_summary.html",data)
    

       


