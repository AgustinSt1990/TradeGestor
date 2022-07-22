# Trade Gestor: 17 de Julio de 2022 - inicio
def apalancamiento(volOp, volRisk, priceSL, priceActual):
    """
    Keyword arguments:
        volOp -- volumen operacion
        volRisk -- volumen arriesgado
        priceSL -- precio de salida
        priceActual -- precio de entrada
    Return: tuple
        riskOp -- volumen arriesgado (actualizado)
        riskOpp -- porcentaje arriesgado
        apal -- apalancamiento - leverage
        liq -- precio de liquidación
    """

    # identificar si es long o short - obtener el volumen apalancado, y el apalancamiento, also la cantidad de activos
    if priceSL < priceActual:  # Long
        opType = 'Long'
        for i in range(1, 125):
            volumen_operation = volOp * i
            asset_amount = volumen_operation / priceActual
            end_balance = volumen_operation - asset_amount*priceSL
            if end_balance >= volRisk:
                apal = i
                break

    elif priceSL > priceActual:  # Short
        opType = 'Short'
        for i in range(1, 125):
            volumen_operation = volOp * i
            asset_amount = volumen_operation / priceActual
            end_balance = asset_amount*priceSL - volumen_operation
            if end_balance >= volRisk:
                apal = i
                break

    else:
        print('posibles errores:\n- que 125x se quede corto\n- que priceSL sea igual a priceActual')

    # Actualizar riskOp, volRisk
    riskOp = end_balance
    riskOpp = riskOp/volOp * 100

    # Precio de liquidación
    liq = priceActual / apal
    if opType == 'Long':
        liq = priceActual - liq
    else:
        liq += priceActual

    result = {'Volumen Arriesgado': riskOp, 'Porcentaje Arriesgado': riskOpp,
              'Apalancamiento': apal, 'Precio liquidación': liq}

    return riskOp, riskOpp, apal, liq


if __name__ == '__main__':
    # Cuenta

    volOp: float = float(input('Volumen de la operación = '))
    riskOp: float = float(input('Volumen arriesgado = '))
    riskOpp: float = riskOp / volOp * 100

    print(riskOpp, '%')

    # precio actual y stop loss
    apalancamiento(volOp, riskOp, 32000, 31800)
