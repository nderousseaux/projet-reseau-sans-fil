# Classe représentant un noeud
import pandas as pd


COORDINATOR = "coordinator"
SENDER = "sender"

POWER = "power"
RSSI = "rssi"

class Node:
    
	# Name
	name = ""
	role = ""

	log = ""
	data = ""
	type = ""
	time = 600

	# Constructeur
	def __init__(self, name, role, log, data, type, time=600):
		self.name = name
		self.role = role
		self.log = log
		self.data = data
		self.type = type
		self.time = time
	
	def get_power(self):
		# On calcule la moyenne de la consommation
		with open(self.data, "r") as f:
			# On charge toutes les données après les 9 premières lignes dans un dataframe pandas
			df = pd.read_csv(f, skiprows=9, sep="\t", names=["time", "what", "index", "timestamp_s", "timestamp_us", "power", "voltage", "current"])

			# On calcule la moyenne de la consommation
			return df["power"].mean()
		
	def get_consumption(self):
		# On calcule la moyenne de la consommation en wat par heure
		return self.get_power() * (self.time / 3600)
		
	def __str__(self):
		return self.name + " (" + self.role + ")"