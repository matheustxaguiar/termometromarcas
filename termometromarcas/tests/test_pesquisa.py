import json
from unittest import skip
from urllib import response

from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from termometromarcas.models.Filtro import Filtro
from termometromarcas.models.Pesquisa import Pesquisa
from termometromarcas.models.Tweet import Tweet

client = APIClient()

class PesquisaTest(APITestCase):
    """ Test module for Pesquisa model """
    
    def setUp(self):
        Tweet.objects.create(
            conteudo='Eu adoro futebol!', data='2022-18-10', like='3', visualizacao='4', retweet='2', usuario='Fulano', polaridade='1', subjetividade='0') 
        tweet = Tweet.objects.get(id=1)
        Filtro.objects.create(
            dataInicial='2022-10-10', dataFinal='2022-10-12') 
        filtro=Filtro.objects.get(id=1)
        Pesquisa.objects.create(
            data='2022-10-10', quantidade='40', termo='Futebol', tweet=tweet, filtro=filtro) 


    def pesquisa(self):
        pesquisa1 = Pesquisa.objects.get(termo='Futebol')
        self.assertEqual(
            pesquisa1.termo(), "Futebol")

class PesquisaAddTest(APITestCase):
    """ Test module for add pesquisa using API"""
    def test_add_pesquisa(self):
        
        self.valid_tweet = {
            "conteudo": "Eu adoro futebol!",
            "data": '2022-10-10',
            "like": 15,
            "visualizacao": 5,
            "retweet": 1,
            "usuario": "Fulano",
            "polaridade": 1,
            "subjetividade": 0
        }
        client.post('/tweet/', data=json.dumps(self.valid_tweet),content_type='application/json')

        self.valid_filtro = {
            "dataInicial": '2022-1-1',
            "dataFinal" : '2022-2-3'
        }     
        filtro = client.post('/tempo/', data=json.dumps(self.valid_filtro),content_type='application/json')   

        pesquisa = Pesquisa.objects.all()
        
        assert len(pesquisa) == 0

        self.valid_payload = {
            
            "data": '2022-10-10', 
            "quantidade": 40,
            "termo":'Futebol', 
            "tweet" : [1],
            "filtro" : [1]
        }

        response = client.post('/pesquisa/', data=json.dumps(self.valid_payload),content_type='application/json')
 
        assert response.status_code == status.HTTP_201_CREATED

        # ela restorna um dicionario, por isso o "response.data["<a chave do dado que vc quer>"]"
        assert response.data["termo"] == "Futebol"

        pesquisa = Pesquisa.objects.all()

        assert len(pesquisa) == 1
        
class PesquisaJsonInvalid(APITestCase):
    """ Test module for add Pesquisa using API"""
    def test_add_pesquisa_invalid_json(self):

        # RETORNA UMA QUERYSET NAO UM .JSON
        pesquisa = Pesquisa.objects.all()
        assert len(pesquisa) == 0

        # para realizar um post invalido foi necessário enviar um vazio
        response = client.post("/pesquisa/", data=json.dumps({}), content_type="application/json")
        
        assert response.status_code == status.HTTP_400_BAD_REQUEST

        pesquisa = Pesquisa.objects.all()
        assert len(pesquisa) == 0

class GetSinglePesquisa(APITestCase):  
    def test_get_single_pesquisa(self):
        
        self.valid_tweet = {
            "conteudo": "Eu adoro futebol!",
            "data": '2022-10-10',
            "like": 15,
            "visualizacao": 5,
            "retweet": 1,
            "usuario": "Fulano",
            "polaridade": 1,
            "subjetividade": 0
        }
        client.post('/tweet/', data=json.dumps(self.valid_tweet),content_type='application/json')

        self.valid_filtro = {
            "dataInicial": '2022-1-1',
            "dataFinal" : '2022-2-3'
        }     
        client.post('/tempo/', data=json.dumps(self.valid_filtro),content_type='application/json')   

        pesquisa = Pesquisa.objects.all()
        
        assert len(pesquisa) == 0

        self.valid_payload = {
            
            "data": '2022-10-10', 
            "quantidade": 40,
            "termo":'Futebol', 
            "tweet" : [1],
            "filtro" : [1]
        }

        response = client.post('/pesquisa/', data=json.dumps(self.valid_payload),content_type='application/json')

        # Caso deseje pegar uma entidade tweet especifica apenas coloque o id dela (Caso alguem descubrqa uma forma automatica usando pk pfvr avise)
        resp = client.get("/pesquisa/1/")
        assert resp.status_code == 200
        assert resp.data["termo"] == "Futebol"

    def test_get_single_tweet_incorrect_id(self):
        # Acessando um id inexistente
        resp = client.get("/pesquisa/88/")
        assert resp.status_code == 404
        
class getAllPesquisas(APITestCase):
    def test_get_all_Tweets(self):
        self.valid_tweet = {
            "conteudo": "Eu adoro futebol!",
            "data": '2022-10-10',
            "like": 15,
            "visualizacao": 5,
            "retweet": 1,
            "usuario": "Fulano",
            "polaridade": 1,
            "subjetividade": 0
        }
        client.post('/tweet/', data=json.dumps(self.valid_tweet),content_type='application/json')

        self.valid_filtro = {
            "dataInicial": '2022-1-1',
            "dataFinal" : '2022-2-3'
        }     
        client.post('/tempo/', data=json.dumps(self.valid_filtro),content_type='application/json')   

        self.valid_pesquisa = {
            
            "data": '2022-5-10', 
            "quantidade": 40,
            "termo":'Futebol', 
            "tweet" : [1],
            "filtro" : [1]
        }

        pesquisa1 = client.post('/pesquisa/', data=json.dumps(self.valid_pesquisa),content_type='application/json')
        
        self.valid_tweet2 = {
            "conteudo": "Eu odeio basquete!",
            "data": '2022-10-10',
            "like": 150,
            "visualizacao": 50,
            "retweet": 10,
            "usuario": "Ciclano",
            "polaridade": 0,
            "subjetividade": 1
        }
        client.post('/tweet/', data=json.dumps(self.valid_tweet2),content_type='application/json')

        self.valid_pesquisa2 = {
            
            "data": '2020-11-10', 
            "quantidade": 500,
            "termo":'Basquete', 
            "tweet" : [2],
            "filtro" : [1]
        }

        pesquisa2 = client.post('/pesquisa/', data=json.dumps(self.valid_pesquisa2),content_type='application/json')

        resp = client.get("/pesquisa/")

        assert resp.status_code == 200
        
        assert resp.data[0]["termo"] == pesquisa1.data['termo']
        assert resp.data[1]["termo"] == pesquisa2.data['termo']
        
class deletePesquisas(APITestCase):
    def test_remove_pesquisa(self):
        self.valid_tweet = {
            "conteudo": "Eu adoro futebol!",
            "data": '2022-10-10',
            "like": 15,
            "visualizacao": 5,
            "retweet": 1,
            "usuario": "Fulano",
            "polaridade": 1,
            "subjetividade": 0
        }
        client.post('/tweet/', data=json.dumps(self.valid_tweet),content_type='application/json')

        self.valid_filtro = {
            "dataInicial": '2022-1-1',
            "dataFinal" : '2022-2-3'
        }     
        client.post('/tempo/', data=json.dumps(self.valid_filtro),content_type='application/json')   

        pesquisa = Pesquisa.objects.all()
        
        assert len(pesquisa) == 0

        self.valid_payload = {
            
            "data": '2022-10-10', 
            "quantidade": 40,
            "termo":'Futebol', 
            "tweet" : [1],
            "filtro" : [1]
        }

        response = client.post('/pesquisa/', data=json.dumps(self.valid_payload),content_type='application/json')
        
        resp = client.get(f"/pesquisa/1/")
        assert resp.status_code == 200
        assert resp.data["termo"] == "Futebol"

        resp_two = client.delete(f"/pesquisa/1/")
        assert resp_two.status_code == status.HTTP_204_NO_CONTENT

        resp_three = client.get("/pesquisa/")
        assert resp_three.status_code == 200
        assert len(resp_three.data) == 0

    def test_remove_tweet_incorrect_id(self):
        resp = client.delete(f"/pesquisa/99/")
        assert resp.status_code == 404

class updatePesquisa(APITestCase):
    def test_update_pesquisa(self):
        self.valid_tweet = {
            "conteudo": "Eu adoro futebol!",
            "data": '2022-10-10',
            "like": 15,
            "visualizacao": 5,
            "retweet": 1,
            "usuario": "Fulano",
            "polaridade": 1,
            "subjetividade": 0
        }
        client.post('/tweet/', data=json.dumps(self.valid_tweet),content_type='application/json')

        self.valid_filtro = {
            "dataInicial": '2022-1-1',
            "dataFinal" : '2022-2-3'
        }     
        client.post('/tempo/', data=json.dumps(self.valid_filtro),content_type='application/json')   

        pesquisa = Pesquisa.objects.all()
        
        assert len(pesquisa) == 0

        self.valid_payload = {
            
            "data": '2022-10-10', 
            "quantidade": 40,
            "termo":'Futebol', 
            "tweet" : [1],
            "filtro" : [1]
        }

        response = client.post('/pesquisa/', data=json.dumps(self.valid_payload),content_type='application/json')
        
        resp = client.put(
            f"/pesquisa/1/",

            # PARA O METODO PUT FUNCIONAR É NECESSÁRIO ENVIAR TODOS OS CAMPOS DO OBJETO (MESMO QUE INALTERADOS)
            data=json.dumps({         
            "data": '2022-10-10', 
            "quantidade": 408,
            "termo":'Basquete', 
            "tweet" : [1],
            "filtro" : [1]
        }),
            content_type="application/json",
        )
        
        assert resp.status_code == 200
        assert resp.data["termo"] == "Basquete"
        assert resp.data["quantidade"] == 408

        resp_two = client.get(f"/pesquisa/1/")
        assert resp_two.status_code == 200
        assert resp_two.data["termo"] == "Basquete"
        assert resp.data["quantidade"] == 408

    def test_update_pesquisa_incorrect_id(self):
        resp = client.put(f"/pesquisa/99/")
        assert resp.status_code == 404

    def test_update_pesquisa_invalid_json(self):
        self.valid_tweet = {
            "conteudo": "Eu adoro futebol!",
            "data": '2022-10-10',
            "like": 15,
            "visualizacao": 5,
            "retweet": 1,
            "usuario": "Fulano",
            "polaridade": 1,
            "subjetividade": 0
        }
        client.post('/tweet/', data=json.dumps(self.valid_tweet),content_type='application/json')

        self.valid_filtro = {
            "dataInicial": '2022-1-1',
            "dataFinal" : '2022-2-3'
        }     
        client.post('/tempo/', data=json.dumps(self.valid_filtro),content_type='application/json')
        self.pesquisa1 = {
            "data": '2022-10-10', 
            "quantidade": 408,
            "termo":'Basquete', 
            "tweet" : [1],
            "filtro" : [1]
        }
        tweet = client.post('/pesquisa/', data=json.dumps(self.pesquisa1),content_type='application/json')
        resp = client.put(f"/pesquisa/1/", data=json.dumps({}), content_type="application/json",)
        assert resp.status_code == status.HTTP_400_BAD_REQUEST
