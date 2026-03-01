from django.contrib import admin
from .models import Motamage


# ადმინ პანელის სახელები
admin.site.site_header = "მომხმარებლების მართვა"
admin.site.site_title = "ადმინ პანელი"
admin.site.index_title = "გამარჯობა, ადმინ!"


# აქშენები - სტატუსის შეცვლა
@admin.action(description="აქტიურად მონიშვნა")
def gaxade_aktive(modeladmin, request, queryset):
    queryset.update(statusi='aktive')


@admin.action(description="არააქტიურად მონიშვნა")
def gaxade_araaktive(modeladmin, request, queryset):
    queryset.update(statusi='araaktive')


@admin.action(description="დაბლოკვა")
def dablokireba(modeladmin, request, queryset):
    queryset.update(statusi='blocked')


@admin.register(Motamage)
class MotamageAdmin(admin.ModelAdmin):
    # სვეტები სიაში
    list_display = ('saxeli', 'gvari', 'email', 'asaki', 'qalaqi', 'statusi', 'sheqmnilia')

    # გვერდითა ფილტრები
    list_filter = ('statusi', 'sheqmnilia', 'qalaqi')

    # ძიების ველები
    search_fields = ('saxeli', 'gvari', 'email')

    # დალაგება
    ordering = ('-sheqmnilia',)

    # სიაში პირდაპირ რედაქტირება
    list_editable = ('statusi',)

    actions = [gaxade_aktive, gaxade_araaktive, dablokireba]
