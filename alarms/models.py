from django.db import models

from measurements.models import Measurement

class Alarm(models.Model):
    measurements = models.ManyToManyField(Measurement)
    
    def __str__(self):
        lista = ' | '.join(str(medida) for medida in self.measurements.all())
        return f'{lista}'