from django.contrib import admin
from .models import CustomUser, Scenario, ScenarioSolution
# Register your models here.
#useless comment
admin.site.register(CustomUser)
admin.site.register(Scenario)
admin.site.register(ScenarioSolution)
