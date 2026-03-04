from django.db import models


class Motamage(models.Model):

    STATUSI = [
        ('aktive', 'აქტიური'),
        ('araaktive', 'არააქტიური'),
        ('blocked', 'დაბლოკილი'),
    ]

    saxeli = models.CharField(max_length=100)
    gvari = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    asaki = models.PositiveIntegerField()
    qalaqi = models.CharField(max_length=100, default='თბილისი')
    statusi = models.CharField(max_length=20, choices=STATUSI, default='aktive')
    sheqmnilia = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-sheqmnilia']
        verbose_name = 'მომხმარებელი'
        verbose_name_plural = 'მომხმარებლები'

    def __str__(self):
        return f"{self.saxeli} {self.gvari}"
