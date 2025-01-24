import os
from datetime import datetime

def obter_resposta(texto: str) -> str:
    comando: str = texto.lower()

    # Verifica se o comando é uma saudação
    if comando in ('olá', 'boa tarde', 'bom dia'):
        return 'Olá tudo bem!'
    
    # Verifica se o comando é uma pergunta sobre o estado
    if comando == 'como estás':
        return 'Estou bem, obrigado!'
    
    # Verifica se o comando é uma pergunta sobre o nome
    if comando == 'como te chamas?':
        return 'O meu nome é: Bot :)'
    
    # Verifica se o comando é uma pergunta sobre o tempo
    if comando == 'tempo':
        return 'Está um dia de sol!'
    
    # Verifica se o comando é uma despedida
    if comando in ('bye', 'adeus', 'tchau'):
        return 'Gostei de falar contigo! Até breve...'
    
    # Verifica se o comando contém a palavra 'horas'
    if 'horas' in comando:
        return f'São: {datetime.now():%H:%M} horas'
    
    # Verifica se o comando contém a palavra 'data'
    if 'data' in comando:
        return f'Hoje é dia: {datetime.now():%d-%m-%Y}'

    # Resposta padrão para comandos não reconhecidos
    return f'Desculpa, não entendi a questão! {texto}'

"""
    respostas = {
        ('olá', 'boa tarde', 'bom dia'): 'Olá tudo bem!',
        'como estás': 'Estou bem, obrigado!',
        'capital de portugal': "Lisboa",
        'como te chamas': 'O meu nome é: Bot :)',
        'tempo': 'Está um dia de sol!',
        ('bye', 'adeus', 'tchau'): 'Gostei de falar contigo! Até breve...',
        'historia de portugal': 'Portugal tem uma rica história...',
    }

    for chave, resposta in respostas.items():
        if isinstance(chave, tuple):
            if comando in chave:
                return resposta
        elif chave in comando:
            return resposta

    if 'horas' in comando:
        return f'São: {datetime.now():%H:%M} horas'

    if 'data' in comando:
        return f'Hoje é dia: {datetime.now():%d-%m-%Y}'

    return f'Desculpa, não entendi a questão! {texto}'
"""

def chat() -> None:
    pass