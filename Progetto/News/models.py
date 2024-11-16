from django.db import models

class Utente(models.Model):
    nome = models.CharField(max_length=25, blank=False)
    cognome = models.CharField(max_length=25, blank=False)
    residenza = models.CharField(max_length=25, blank=False)
    nascita = models.DateField()
    assunzione = models.DateField()
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
        return f"{self.nome} {self.ubicazione}"

class Magazzino(models.Model):
    codice_art = models.CharField(max_length=12, blank=False, null=False)
    descrizione = models.CharField(max_length=12, blank=False, null=False)  
    qta_sotto_scorta = models.IntegerField()
    qta = models.IntegerField()
    valore_unitario = models.IntegerField()
    ut_registrazione = models.ForeignKey(Utente, on_delete=models.CASCADE, related_name='Ut_magazzino')
    
    @property
    def valore_totale(self):
        return self.qta * self.valore_unitario
    
    @property
    def sotto_scorta(self):
        if self.qta < self.qta_sotto_scorta:
            return f"Quantità: {self.qta} da ordinare!"
        else:
            return f"Quantità: {self.qta} non serve ordinare!"

    def __str__(self):
        return f"{self.codice_art} {self.descrizione}"
    
    class Meta:
        verbose_name = 'Magazzino'
        verbose_name_plural = 'Magazzini'

class Ordine(models.Model):
    cliente = models.ForeignKey(Azienda, on_delete=models.CASCADE, related_name='c_ordine')
    articolo = models.ForeignKey(Magazzino, on_delete=models.CASCADE, related_name='a_ordine')
    qta = models.IntegerField()
    
    @property
    def verifica(self):
        if self.qta > self.articolo.qta:
            return f"Quantità: {self.qta} non presente a magazzino, da ordinare!"
        else:
            return f"Quantità: {self.qta} ok presente a magazzino procedere alla spedizione"

    data_consegna = models.DateField()
    data_inserimento = models.DateField()

    def __str__(self):
        return f"{self.cliente} {self.data_consegna}"
    
    class Meta:
        verbose_name = 'Ordine'
        verbose_name_plural = 'Ordini'

    

