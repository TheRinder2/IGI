from django.contrib import admin
from .models import FAQ, Contact, Banner, New, Vacancion, Discount, Rent, RequestRent, RequestImm, Immovables, Comment, Report

admin.site.register(FAQ)
admin.site.register(Contact)
admin.site.register(New)
admin.site.register(Vacancion)
admin.site.register(Discount)
admin.site.register(Rent)
admin.site.register(Immovables)
admin.site.register(RequestRent)
admin.site.register(RequestImm)
admin.site.register(Comment)
admin.site.register(Report)
admin.site.register(Banner)
