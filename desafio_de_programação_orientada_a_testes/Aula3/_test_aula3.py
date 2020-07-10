# ciclo:
#    Escreve um teste
#    implementa o mínimo para que o teste passe
#    refatore
#    repita

import pytest


def e_bissexto(ano):
    resto = ano % 4
    resto100 = ano % 100
    resto400 = ano % 400

    if not resto:
        if not resto400:
            return True
        elif resto100:
            return True
    return False


@pytest.mark.parametrize('ano', [1600, 1732, 1888, 1944, 2008])
def test_deve_ser_bissexto(ano):
    resp = e_bissexto(ano)

    assert resp is True


@pytest.mark.parametrize('ano', [500,1742,1889,1951,2011])
def test_nao_deve_ser_bi(ano):
    resp = e_bissexto(ano)

    assert resp is False

