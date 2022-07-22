# Trade Gestor: 17 de Julio de 2022 - inicio
import json
import requests
# from pprint import pprint


def priceBTC():
    URL = 'https://api.coindesk.com/v1/bpi/currentprice.json'

    r = requests.get(URL)

    data = json.loads(r.content.decode('utf-8'))

    bitcoin_price = data['bpi']['USD']['rate_float']

    #print(f'BTC price = {bitcoin_price}')
    return bitcoin_price


"""
En este ejemplo vamos a vender $35.000 ARS en USD, especulando una suba de 270usd a 400usd el USD.
El stop loss está en 230usd el resultado sería de $29.000 si la operación se fuera en contra y el apalancamiento fuera 1x.
Nosotros estamos dispuestos a arriesgar $17.500 en esta operacion.
Calculame el apalancamiento
"""


def apalancamiento(volOp, volRisk, priceSL, priceActual):
    # identificar si es long o short - obtener el volumen apalancado, y el apalancamiento, also la cantidad de activos
    if priceSL < priceActual:  # Long
        for i in range(1, 125):
            volumen_operation = volOp * i
            asset_amount = volumen_operation / priceActual
            end_balance = volumen_operation - asset_amount*priceSL
            if end_balance >= volRisk:
                apal = i
                break

    elif priceSL > priceActual:  # Short
        for i in range(1, 125):
            volumen_operation = volOp * i
            asset_amount = volumen_operation / priceActual
            end_balance = asset_amount*priceSL - volumen_operation
            if end_balance >= volRisk:
                apal = i
                break

    else:
        print('posibles errores:\n- que 35x se quede corto\n- que priceSL sea igual a priceActual')

    # Actualizar riskOp, volRisk, calcular RB (solo si se tiene target TP)
    riskOp = end_balance
    riskOpp = riskOp/volOp * 100

    print(riskOp, 'Un')
    print(riskOpp, '%')
    print(apal, 'x')
    # return {'Monto Arriesgado': volRisk, 'Porcentaje Arriesgado': riskOp, 'Apalancamiento': apal}
    return 'hola mundo'


if __name__ == '__main__':
    # Cuenta
    # print('HolaMundo')
    #volOp: float = float(input('Volumen de la operación = '))
    #riskOp: float = float(input('Volumen arriesgado = '))
    #riskOpp: float = riskOp / volOp * 100

    #print(riskOpp, '%')

    # precio actual y stop loss
    # priceActual = 32000; priceSL = 31800

    #apalancamiento(volOp, riskOp, 32000, 31800)

    pass
