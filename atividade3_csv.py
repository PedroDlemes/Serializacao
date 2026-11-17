
import csv

class LoteProducao:
    def __init__(self, numeroLote, tipoLiga, pesoTotal,
                 temperaturaFundicao, statusQualidade):

        self.numeroLote = numeroLote
        self.tipoLiga = tipoLiga
        self.pesoTotal = pesoTotal
        self.temperaturaFundicao = temperaturaFundicao
        self.statusQualidade = statusQualidade

lotes = [
    LoteProducao(1, "Aço carbono", 500, 1500.5, "Aprovado"),
    LoteProducao(2, "Aço inox", 600, 1520.0, "Aprovado"),
    LoteProducao(3, "Liga de ferro", 450, 1480.5, "Reprovado"),
    LoteProducao(4, "Aço especial", 700, 1550.0, "Aprovado"),
    LoteProducao(5, "Liga metálica", 550, 1510.0, "Aprovado")
]

with open("producao_turno.csv", "w", newline="", encoding="utf-8") as arquivo:
    escritor = csv.writer(arquivo, delimiter=";")

    escritor.writerow([
        "numeroLote",
        "tipoLiga",
        "pesoTotal",
        "temperaturaFundicao",
        "statusQualidade"
    ])

    for lote in lotes:
        escritor.writerow([
            lote.numeroLote,
            lote.tipoLiga,
            lote.pesoTotal,
            lote.temperaturaFundicao,
            lote.statusQualidade
        ])

print("Arquivo CSV criado!")

lotes_lidos = []

with open("producao_turno.csv", "r", encoding="utf-8") as arquivo:
    leitor = csv.DictReader(arquivo, delimiter=";")

    for linha in leitor:
        lote = LoteProducao(
            int(linha["numeroLote"]),
            linha["tipoLiga"],
            float(linha["pesoTotal"]),
            float(linha["temperaturaFundicao"]),
            linha["statusQualidade"]
        )

        lotes_lidos.append(lote)

print("\nLotes de produção:")

for lote in lotes_lidos:
    print(lote.numeroLote, lote.tipoLiga,
          lote.pesoTotal, lote.temperaturaFundicao,
          lote.statusQualidade)

media = sum(lote.temperaturaFundicao for lote in lotes_lidos) / len(lotes_lidos)

print("\nMédia das temperaturas:", media)
