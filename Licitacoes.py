from MongoConnect import MongoConnect
import matplotlib.pyplot as plt
from datetime import datetime
import json

class Licitacoes:

    def __init__(self) -> None:
        self.mongo_connect = MongoConnect()
        self.collection = self.mongo_connect.get_collection()

    def load_licitacoes(self):
        json_licitacoes = json.loads(open("licitacoes.json", "r", encoding="iso-8859-1").read())

        for licitacao in json_licitacoes["licitacoes"]:

            date = licitacao["DataAbertura"].split("/")

            date = datetime(
                int(date[2]),
                int(date[1]),
                int(date[0]),
                0,
                0,
                0
            )

            month_licitacao = date.month

            doc_licitacao = {
                "titulo" : licitacao["Titulo"],
                "modalidade" : licitacao["Modalidade"],
                "nr_licitacao" : licitacao["NrLicitacao"],
                "nr_processo" : licitacao["NrProcesso"],
                "secretaria_licitante" : licitacao["SecretariaLicitante"],
                "data_abertura" : date,
                "mes" : month_licitacao
            }

            self.collection.insert_one(doc_licitacao)

        print("insert completed")
    
    def plot_graphic(self):
        print("Licitações x Mês")

        months_licitacoes = self.collection.distinct("mes")

        x_points = []
        y_points = []

        for month in months_licitacoes:
            quantity = self.collection.count_documents(
                {
                    "mes" : month
                }
            )

            x_points.append(month)
            y_points.append(quantity)
        
        plt.plot(x_points, y_points)
        plt.xlabel("Mês licitação")
        plt.ylabel("Quantidade de licitações")
        plt.show()

    def delete_data(self):
        self.collection.delete_many({})

        print("delete completed")

