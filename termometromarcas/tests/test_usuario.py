import json
from unittest import skip
from termometromarcas.models import Usuario, Fisico, Juridico
from rest_framework import status
from rest_framework.test import APIClient, APITestCase


client = APIClient()

class UsuarioTest(APITestCase):
    """ Test module for Tweet model """

    def setUp(self):
        
        Fisico.objects.create(
        usuario='Fulano', email='fulaninhoplays@gmail.com', senha='ihhhuuuul', pesquisas=[], cpf='15478842155'
            ) 
        Juridico.objects.create(
        usuario='Metais', email='metais@gmail.com', senha='ihhhuuuul', pesquisas=[], cnpj='71885582000189'
            ) 

    def usuario(self):
        fisico1 = Fisico.objects.get(usuario='Fulano')
        self.assertEqual(
            fisico1.usuario(), "Fulano")
        juridico1 = Juridico.objects.get(usuario='Fulano')
        self.assertEqual(
            juridico1.usuario(), "Metais")

class UsuarioAddTest(APITestCase):
    """ Test module for add Tweet using API"""
    def usuario_add_tweet(self):
        #Teste Físico
        fisico = Fisico.objects.all()
        
        assert len(fisico) == 0
        
        self.valid_fisico = {
        "usuario": "Fulano",
        "email": "fulano@gmail.com",
        "senha": "ibuuu",
        "cpf": '15478842155',
        "pesquisas": []
        }
        # é necessário colocar o data=json.dumps(<o que vc quer adicionar aqui>) POIS A API ENTENDE O FORMATO JSON
        response = client.post('/fisico/', data=json.dumps(self.valid_fisico),content_type='application/json')
        assert response.status_code == status.HTTP_201_CREATED
        
        assert response.data["usuario"] == "Fulano"

        fisico = Fisico.objects.all()

        assert len(fisico) == 1
        
        #Teste Juridico
        juridico = Juridico.objects.all()
        
        assert len(juridico) == 0
        
        self.valid_juridico = {
        "usuario": "Metais",
        "email": "Metais@gmail.com",
        "senha": "ibuuu",
        "cnpj": '71885582000189',
        "pesquisas": []
        }
        # é necessário colocar o data=json.dumps(<o que vc quer adicionar aqui>) POIS A API ENTENDE O FORMATO JSON
        response = client.post('/juridico/', data=json.dumps(self.valid_juridico),content_type='application/json')
        assert response.status_code == status.HTTP_201_CREATED
        
        assert response.data["usuario"] == "Fulano"

        fisico = Juridico.objects.all()

        assert len(fisico) == 1
        
class UsuarioJsonInvalid(APITestCase):
    """ Test module for add tweet using API"""
    def test_add_fisico_invalid_json(self):

        # RETORNA UMA QUERYSET NAO UM .JSON
        fisico = Fisico.objects.all()
        assert len(fisico) == 0

        # para realizar um post invalido foi necessário enviar um vazio
        response = client.post("/fisico/", data=json.dumps({}), content_type="application/json")
        assert response.status_code == status.HTTP_400_BAD_REQUEST

        tweet = Fisico.objects.all()
        assert len(fisico) == 0
    def test_add_juridico_invalid_json(self):

        # RETORNA UMA QUERYSET NAO UM .JSON
        juridico = Juridico.objects.all()
        assert len(juridico) == 0

        # para realizar um post invalido foi necessário enviar um vazio
        response = client.post("/juridico/", data=json.dumps({}), content_type="application/json")
        assert response.status_code == status.HTTP_400_BAD_REQUEST

        juridico = Juridico.objects.all()
        assert len(juridico) == 0
        
@skip       
class GetSingleUser(APITestCase): 

    def test_get_single_user(self):
        self.valid_fisico = {
        "usuario": "Fulano",
        "email": "fulano@gmail.com",
        "senha": "ibuuu",
        "cpf": '15478842155',
        "pesquisas": []
        } 
        self.valid_juridico = {
        "usuario": "Metais",
        "email": "Metais@gmail.com",
        "senha": "ibuuu",
        "cnpj": '71885582000189',
        "pesquisas": []
        }

        fisico = client.post('/fisico/', data=json.dumps(self.valid_fisico),content_type='application/json')
        juridico = client.post('/juridico/', data=json.dumps(self.valid_juridico),content_type='application/json')

        # Caso deseje pegar uma entidade tweet especifica apenas coloque o id dela (Caso alguem descubrqa uma forma automatica usando pk pfvr avise)
        resp = client.get("/fisico/1/")

        assert resp.status_code == 200
        assert resp.data["usuario"] == "Fulano"
        
        resp2 = client.get("/juridico/1/")
        print(resp2)
        assert resp2.status_code == 200
        assert resp2.data["usuario"] == "Metais"

    def test_get_single_tweet_incorrect_id(self):
        # Acessando um id inexistente
        resp = client.get("/fisico/88/")
        assert resp.status_code == 404