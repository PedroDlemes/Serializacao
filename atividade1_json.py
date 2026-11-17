
import json

class DroneStatus:
    def __init__(self, codigoIdentificador, nivelBateria, latitude, longitude, emMissao):
        self.codigoIdentificador = codigoIdentificador
        self.nivelBateria = nivelBateria
        self.latitude = latitude
        self.longitude = longitude
        self.emMissao = emMissao

drone = DroneStatus("DR001", 85, -19.9167, -43.9345, True)

with open("status_drone.json", "w", encoding="utf-8") as arquivo:
    json.dump(drone.__dict__, arquivo, indent=4)

print("Arquivo JSON criado!")

with open("status_drone.json", "r", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)

drone_recuperado = DroneStatus(**dados)

print("\nDados do Drone:")
print("Codigo:", drone_recuperado.codigoIdentificador)
print("Bateria:", drone_recuperado.nivelBateria)
print("Latitude:", drone_recuperado.latitude)
print("Longitude:", drone_recuperado.longitude)
print("Em missao:", drone_recuperado.emMissao)
