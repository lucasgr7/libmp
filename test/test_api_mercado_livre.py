import requests_mock
from libmp.api import __get_token__

PFX_JSON = 'test/json'


class TestApiMercadoLivre:

    def test_get_token(self, monkeypatch):
        monkeypatch.setenv('URL_OC_BASE', 'http://mock-oc.com.br/api.php')
        monkeypatch.setenv('OPENCART_TOKEN', '123')
        monkeypatch.setenv('AMBIENTE', '123')

        with requests_mock.Mocker() as m:
            m.get('http://mock-oc.com.br/api.php/token/mercadolivre',
                    text=open(f'{PFX_JSON}/body_token.json').read())
            token = __get_token__()
            assert token.access_token == 'A'
            assert token.refresh_token == 'B'

            token = __get_token__()
            assert token.access_token == 'A'
            assert token.refresh_token == 'B'
            assert m.call_count == 1

    def test_token_refresh(self):
        # 1 - chamada mercado livre
        # 2 - Mocka retorno 401 não autorizado para api
        # 3 - Chama método refresh_token
        # 4 - Deve fazer um PUT para atualizar o token
        pass

    def test_token_expirado(self):
        # 1 - chama __get_token__
        # 2 - altera mock da api do /token/mercadolivre
        # 3 - __get_token__ deve ainda trazer versão cacheada
        # 4 - executa comando de limpar o cache (nova feat)
        # 5 - __get_token__ deve trazer novo token chamando a api
        # 6 - m.call_count == 2
        pass
