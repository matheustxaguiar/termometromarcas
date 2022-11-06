import json
from unittest import skip

from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from termometromarcas.models.Tweet import Tweet

client = APIClient()

class TweetTest(APITestCase):
    """ Test module for Tweet model """

    def setUp(self):
        Tweet.objects.create(
            conteudo='Eu adoro futebol!', data='2022-10-10', like='3', visualizacao='4', retweet='2', usuario='Fulano', polaridade='1', subjetividade='0') 


    def tweet(self):
        tweet1 = Tweet.objects.get(usuario='Fulano')
        self.assertEqual(
            tweet1.usuario(), "Fulano")

class TweetAddTest(APITestCase):
    """ Test module for add Tweet using API"""
    def test_add_tweet(self):

        tweet = Tweet.objects.all()
        
        assert len(tweet) == 0

        self.valid_payload = {
            "conteudo": "Eu adoro futebol!",
            "data": '2022-10-10',
            "like": 15,
            "visualizacao": 5,
            "retweet": 1,
            "usuario": "Fulano",
            "polaridade": 1,
            "subjetividade": 0
        }

        # é necessário colocar o data=json.dumps(<o que vc quer adicionar aqui>) POIS A API ENTENDE O FORMATO JSON
        response = client.post('/tweet/', data=json.dumps(self.valid_payload),content_type='application/json')
        assert response.status_code == status.HTTP_201_CREATED

        # ela restorna um dicionario, por isso o "response.data["<a chave do dado que vc quer>"]"
        assert response.data["usuario"] == "Fulano"

        tweets = Tweet.objects.all()

        assert len(tweets) == 1

class TweetJsonInvalid(APITestCase):
    """ Test module for add tweet using API"""
    def test_add_tweet_invalid_json(self):

        # RETORNA UMA QUERYSET NAO UM .JSON
        tweet = Tweet.objects.all()
        assert len(tweet) == 0

        # para realizar um post invalido foi necessário enviar um vazio
        response = client.post("/tweet/", data=json.dumps({}), content_type="application/json")
        assert response.status_code == status.HTTP_400_BAD_REQUEST

        tweet = Tweet.objects.all()
        assert len(tweet) == 0

class GetSingleTweet(APITestCase):  
    def test_get_single_user(self):
        self.valid_payload = {
            "conteudo": "Eu adoro futebol!",
            "data": '2022-10-10',
            "like": 15,
            "visualizacao": 5,
            "retweet": 1,
            "usuario": "Fulano",
            "polaridade": 1,
            "subjetividade": 0
        }

        tweet = client.post('/tweet/', data=json.dumps(self.valid_payload),content_type='application/json')

        # Caso deseje pegar uma entidade tweet especifica apenas coloque o id dela (Caso alguem descubrqa uma forma automatica usando pk pfvr avise)
        resp = client.get("/tweet/1/")
        assert resp.status_code == 200
        assert resp.data["usuario"] == "Fulano"

    def test_get_single_tweet_incorrect_id(self):
        # Acessando um id inexistente
        resp = client.get("/tweet/88/")
        assert resp.status_code == 404
        

class getAllTweets(APITestCase):
    def test_get_all_Tweets(self):
        self.tweet1 = {
            "conteudo": "Eu adoro futebol!",
            "data": '2022-10-10',
            "like": 15,
            "visualizacao": 500,
            "retweet": 1,
            "usuario": "Fulano",
            "polaridade": 1,
            "subjetividade": 0
        }
        self.tweet2 = {
            "conteudo": "Eu odeio futebol!",
            "data": '2022-11-10',
            "like": 17,
            "visualizacao": 88,
            "retweet": 8,
            "usuario": "Ciclano",
            "polaridade": 0,
            "subjetividade": 1
        }
        tweet1 = client.post('/tweet/', data=json.dumps(self.tweet1),content_type='application/json')
        tweet2 = client.post('/tweet/', data=json.dumps(self.tweet2),content_type='application/json')
        resp = client.get("/tweet/")

        assert resp.status_code == 200

        # Para acessar o json do response apenas coloque o response.data e acesse o atributo que deseja com apenas []
        assert resp.data[0]["usuario"] == tweet1.data['usuario']
        assert resp.data[1]["usuario"] == tweet2.data['usuario']

class deleteTweet(APITestCase):
    def test_remove_tweet(self):
        self.tweet1 = {
            "conteudo": "Eu adoro futebol!",
            "data": '2022-7-10',
            "like": 15,
            "visualizacao": 500,
            "retweet": 1,
            "usuario": "Fulano",
            "polaridade": 1,
            "subjetividade": 0
        }

        tweet1 = client.post('/tweet/', data=json.dumps(self.tweet1),content_type='application/json')

        resp = client.get(f"/tweet/1/")
        assert resp.status_code == 200
        assert resp.data["usuario"] == "Fulano"

        resp_two = client.delete(f"/tweet/1/")
        assert resp_two.status_code == status.HTTP_204_NO_CONTENT

        resp_three = client.get("/tweet/")
        assert resp_three.status_code == 200
        assert len(resp_three.data) == 0

    def test_remove_tweet_incorrect_id(self):
        resp = client.delete(f"/tweet/99/")
        assert resp.status_code == 404

class updateTweet(APITestCase):
    def test_update_tweet(self):
        self.tweet1 = {
            "conteudo": "Eu adoro futebol!",
            "data": '2022-1-10',
            "like": 15,
            "visualizacao": 500,
            "retweet": 1,
            "usuario": "Fulano",
            "polaridade": 1,
            "subjetividade": 0
        }

        tweet = client.post('/tweet/', data=json.dumps(self.tweet1),content_type='application/json')

        resp = client.put(
            f"/tweet/1/",

            # PARA O METODO PUT FUNCIONAR É NECESSÁRIO ENVIAR TODOS OS CAMPOS DO OBJETO (MESMO QUE INALTERADOS)
            data=json.dumps({
            "conteudo": "Eu adoro futebol!",
            "data": '2022-8-10',
            "like": 222,
            "visualizacao": 500,
            "retweet": 1,
            "usuario": "Fulano",
            "polaridade": 1,
            "subjetividade": 0
        }),
            content_type="application/json",
        )

        assert resp.status_code == 200
        assert resp.data["usuario"] == "Fulano"
        assert resp.data["like"] == 222

        resp_two = client.get(f"/tweet/1/")
        assert resp_two.status_code == 200
        assert resp_two.data["usuario"] == "Fulano"
        assert resp.data["like"] == 222

    def test_update_tweet_incorrect_id(self):
        resp = client.put(f"/tweet/99/")
        assert resp.status_code == 404


    def test_update_tweet_invalid_json(self):
        self.tweet1 = {
            "conteudo": "Eu adoro futebol!",
            "data": '2022-10-10',
            "like": 222,
            "visualizacao": 500,
            "retweet": 1,
            "usuario": "Fulano",
            "polaridade": 1,
            "subjetividade": 0
        }
        tweet = client.post('/tweet/', data=json.dumps(self.tweet1),content_type='application/json')
        resp = client.put(
            f"/tweet/1/", data=json.dumps({}), content_type="application/json",
        )
        assert resp.status_code == status.HTTP_400_BAD_REQUEST
