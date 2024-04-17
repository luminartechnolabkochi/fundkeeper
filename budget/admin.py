from django.contrib import admin

# Register your models here.
from budget.models import Expense


admin.site.register(Expense)