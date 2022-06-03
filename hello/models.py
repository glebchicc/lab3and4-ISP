from django.db import models


# Create your models here.
# class Bus:
#    def __init__(self, seats, id_number, departure_time, arrival_time):
#        self.seats = seats
#        self.id_number = id_number
#        self.departure_time = departure_time
#        self.arrival_time = arrival_time
#
#    def make_order(self):
#        if (self.seats > 0):
#            self.seats -= 1
#            # присвоить сидение пассажиру
#        else:
#            print("Нет мест.")
#
#    def cancel_order(self):
#        self.seats += 1
#        # отменить привязку места к пассажиру
#
#    def exchange_orger(self):
#        pass
#
#
# class Passenger:
#    def __init__(self):
#        pass


class Bus(models.Model):
    bus_number = models.CharField("Номер автобуса", max_length=8)
    departure_time = models.DateTimeField("Время отправления")
    arrival_time = models.DateTimeField("Время прибытия")
    departure_place = models.CharField("Точка сбора", max_length=50)
    arrival_place = models.CharField("Место назначения", max_length=50)
    place_cost = models.CharField("Стоимость одного места", max_length=10)
    places = models.IntegerField("Количество мест")

    class Meta:
        verbose_name = "Автобус"
        verbose_name_plural = "Автобусы"

    def find_short_departure(self):
        for i in range(len(self.departure_place)):
            if self.departure_place[i] == ',':
                return self.departure_place[:i]

    def find_short_arrival(self):
        for i in range(len(self.arrival_place)):
            if self.arrival_place[i] == ',':
                return self.arrival_place[:i]


class Passanger(models.Model):
    name = models.CharField("Фамилия и имя пассажира", max_length=50)
    ordered_buses = models.CharField("Заказанные автобусы", max_length=40)

    class Meta:
        verbose_name = "Пассажир"
        verbose_name_plural = "Пассажиры"
