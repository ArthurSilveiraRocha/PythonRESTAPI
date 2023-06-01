from flask_restful import Resource

hoteis = [
    {
        'hotel_id':'alpha',
        'nome':'Alpha Hotel',
        'estrelas':4.5,
        'diaria': 420,
        'cidade':'Rio de Janeiro'
    },
    {
        'hotel_id':'bravo',
        'nome':'Bravo Hotel',
        'estrelas':3,
        'diaria': 120,
        'cidade':'Balneário Camburiú'
    },
    {
        'hotel_id':'charlie',
        'nome':'Charlie Hotel',
        'estrelas':4,
        'diaria': 400,
        'cidade':'Carapicuíba'
    }
]

class Hoteis(Resource):
    def get(self):
        return{'Hoteis': hoteis}