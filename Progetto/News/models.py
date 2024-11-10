from django.db import models

class Utente(models.Model):
    nome = models.CharField(max_length=25, blank=False)
    cognome = models.CharField(max_length=25, blank=False)
    residenza = models.CharField(max_length=25, blank=False)
    nascita = models.DateField(auto_now_add=False)
    assunzione = models.DateField(auto_now_add=False)
    ruolo = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Utente'
        verbose_name_plural = 'Utenti'

    def __str__(self):
        return f"{self.nome} {self.cognome} {self. ruolo}"

class Azienda(models.Model):
    ut_registrazione = models.ForeignKey(Utente, on_delete=models.CASCADE, related_name='AUtente')
    nome = models.CharField(max_length=20, null=False)
    ubicazione = models.CharField(max_length=50, null=False)
    p_iva = models.IntegerField()
    descrizione = models.TextField(max_length=250)

    class Meta:
        verbose_name = 'Azienda'
        verbose_name_plural = 'Aziende'

    def __str__(self):
        return f"{self.nome} {self.descrizione}"