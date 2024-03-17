from django.contrib import admin
from .models import Public, GlobalConfig, PoliceStation
from .models import PublicAdmin, GlobalConfigAdmin, PoliceStationAdmin

admin.site.register(Public, PublicAdmin)
admin.site.register(GlobalConfig, GlobalConfigAdmin)
admin.site.register(PoliceStation, PoliceStationAdmin)
