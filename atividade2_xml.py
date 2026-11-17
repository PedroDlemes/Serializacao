
import xml.etree.ElementTree as ET

class RelatorioAnalise:
    def __init__(self, idAmostra, tipoMaterial, dataColeta,
                 nomeCientista, registroProfissional, resultados):

        self.idAmostra = idAmostra
        self.tipoMaterial = tipoMaterial
        self.dataColeta = dataColeta
        self.nomeCientista = nomeCientista
        self.registroProfissional = registroProfissional
        self.resultados = resultados

relatorio = RelatorioAnalise(
    101,
    "Sangue",
    "17/11/2026",
    "Carlos Mendes",
    "CRBio 12345",
    ["Proteína X", "Enzima Y", "Vitamina D"]
)

raiz = ET.Element("relatorio")

amostra = ET.SubElement(raiz, "amostra")
ET.SubElement(amostra, "idAmostra").text = str(relatorio.idAmostra)
ET.SubElement(amostra, "tipoMaterial").text = relatorio.tipoMaterial
ET.SubElement(amostra, "dataColeta").text = relatorio.dataColeta

responsavel = ET.SubElement(raiz, "responsavel")
ET.SubElement(responsavel, "nomeCientista").text = relatorio.nomeCientista
ET.SubElement(responsavel, "registroProfissional").text = relatorio.registroProfissional

resultados = ET.SubElement(raiz, "resultados")

for item in relatorio.resultados:
    ET.SubElement(resultados, "componente").text = item

arvore = ET.ElementTree(raiz)
arvore.write("relatorio_amostra.xml", encoding="utf-8", xml_declaration=True)

print("Arquivo XML criado!")

arvore = ET.parse("relatorio_amostra.xml")
raiz = arvore.getroot()

print("\nRelatório da Amostra:")
print("ID:", raiz.find("amostra/idAmostra").text)
print("Material:", raiz.find("amostra/tipoMaterial").text)
print("Data:", raiz.find("amostra/dataColeta").text)
print("Cientista:", raiz.find("responsavel/nomeCientista").text)
print("Registro:", raiz.find("responsavel/registroProfissional").text)

print("Resultados:")
for item in raiz.findall("resultados/componente"):
    print("-", item.text)
