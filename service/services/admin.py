from django.contrib import admin

from .models import Service, TariffPlan, Subscription

admin.site.register(Service)
admin.site.register(TariffPlan)
admin.site.register(Subscription)

