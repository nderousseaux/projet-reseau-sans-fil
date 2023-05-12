# Classe représentant un noeud
import pandas as pd


COORDINATOR = "coordinator"
SENDER = "sender"

POWER = "power"
LOGS = "rssi"

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
	
	# Renvoie le débit utile
	def get_useful_throughput(self):
		data = 0;

		# On ouvre le fichier
		with open(self.data, "r") as f:
			# On cherche les lignes qui commencent par [INFO: TSCH-LOG  ]
			lines = [l for l in f if l.startswith("[INFO: TSCH-LOG  ]")]
			
			# On cherche les paquets de type data 
			# Le premier mot après '}': 1
			for l in lines:
				try:
					# Le mot juste après len est la taille du paquet
					l = l.split("}")[1]

					if l.split("-")[1] == "1":
						if "len" in l:
							size = l.split("len ")[1].split(",")[0]
							data += int(size)
				except:
					pass
		
		# On calcule le débit utile en ko/s
		return data * 8 / self.time / 1000
		
	def __str__(self):
		return self.name + " (" + self.role + ")"
	
	def get_loss_rate(self):

		# On ouvre le fichier
		with open(self.data, "r") as f:
			# On compte le nombre de ligne ou il y a st 0
			# On compte le nombre de ligne ou il y a st 2

			no_st0 = 0
			no_st2 = 0

			for l in f:
				if "st 0" in l:
					no_st0 += 1
				elif "st 2" in l:
					no_st2 += 1
			
		# On calcule le taux de perte
		return no_st2 / (no_st0 + no_st2)
