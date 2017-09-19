from django.db import models


# Create your models here.
class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=128)
    datanascimento = models.DateField()
    email = models.EmailField(max_length=254)

class Agenda_Institucional(models.Model):
    nome_empresa=models.TextField()


class Agenda(models.Model):
    PRIVADA ='PR'
    PUBLICA='PB'
    TIPO_DE_AGENDA = (
        (PRIVADA,'Privada'),
        (PUBLICA,'Pública')

    )
    visivel=models.CharField(max_length=2,choices=TIPO_DE_AGENDA,default=PRIVADA)
    user = models.ForeignKey(Usuario)



class Compromisso(models.Model):
    agenda=models.ForeignKey(Agenda,related_name=u'fk_agenda_compromissos')
    institucinal=models.ForeignKey(Agenda_Institucional,related_name=u'fk_institucional_compromissos')
    data = models.DateField()
    descricao = models.TextField()


