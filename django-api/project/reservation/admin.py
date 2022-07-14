from django.contrib import admin
from reservation.models.Table import Table
from reservation.models.Seat import Seat
from reservation.models.Restaurant import Restaurant

from reservation.models.Reservation import Reservation


class TableInline(admin.StackedInline):
    model = Table

class SeatInline(admin.StackedInline):
    model = Seat

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    inlines = [TableInline,]

@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    inlines = [SeatInline,]

@admin.register(Seat)
class SeatAdmin(admin.ModelAdmin):
    pass

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    pass
