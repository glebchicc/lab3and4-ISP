import django
from django.db import models
from django.utils import timezone


def show_buses():
    buses = Bus.objects.order_by("departure_time")
    for i in buses:
        if i.departure_time < timezone.now():
            i.delete()
        else:
            break
    return buses


def generate_buses():
    for i in range(10):
        i = Bus(bus_number=i, departure_time=timezone.now() + timezone.timedelta(minutes=20 + 15 * i),
                arrival_time=timezone.now() + timezone.timedelta(minutes=80 + 15 * i),
                departure_place="Борисов, парковка Веста", arrival_place="Минск, ст. м. Борисовский тракт",
                place_cost="5.0", places=17, size_of_bus_id=2)
        i.save()
    for i in range(10):
        i = Bus(bus_number=i, departure_time=timezone.now() + timezone.timedelta(minutes=20 + 15 * i),
                arrival_time=timezone.now() + timezone.timedelta(minutes=80 + 15 * i),
                departure_place="Минск, ст. м. Борисовский тракт", arrival_place="Борисов, парковка Веста",
                place_cost="5.0", places=17, size_of_bus_id=2)
        i.save()


class SizeOfBus(models.Model):
    title = models.CharField("Название размера автобуса", max_length=50)

    def __str__(self):
        return self.title


class Bus(models.Model):
    bus_number = models.CharField("Номер автобуса", max_length=8)
    departure_time = models.DateTimeField("Время отправления", default=django.utils.timezone.now())
    arrival_time = models.DateTimeField("Время прибытия", default=django.utils.timezone.now())
    departure_place = models.CharField("Точка сбора", max_length=50)
    arrival_place = models.CharField("Место назначения", max_length=50)
    place_cost = models.CharField("Стоимость одного места", max_length=10)
    places = models.IntegerField("Количество мест")
    size_of_bus = models.ForeignKey(SizeOfBus, on_delete=models.CASCADE)

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
