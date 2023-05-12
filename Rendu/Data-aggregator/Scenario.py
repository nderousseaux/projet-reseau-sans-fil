# Classe représentant un scenario
import os
from Node import *

TSCH = "tsch"
CSMA = "csma"
NULLMAC = "nullmac"

class Scenario:
	

	# Constructeur
	def __init__(self, path, nbSenders=5, protocol=TSCH, slotSize=397, time=600):
		self.nbSenders = nbSenders
		self.protocol = protocol
		self.slotSize = slotSize
		self.time = time
		self.path = path
		self.nodes_power = []
		self.nodes_logs = []
		# On récupère les noeuds
		self.get_nodes_power()

		# On récupère les logs
		self.get_nodes_logs()
	
	# Génère les noeuds
	def get_nodes_power(self):
		# On rentre dans le dossier power
		for file in os.listdir(self.path + "/power/exp1/logs"):
			# On récupère le nom du fichier
			file_name = os.path.splitext(file)[0]
			# On récupère le numéro du noeud
			node = file_name.split("_")[1]
			# On cherche la ligne contenant le rôle du noeud
			with open(self.path + "/power/exp1/logs/" + file, "r") as f:
				for l in f:
					if "Flash firmware on OpenOCD" in l:
						# On récupère le rôle du noeud (dernier mot de la ligne)
						role = l.split("_")[-1].split(".")[0].strip()
						break
						
			# On crée le noeud
			self.nodes_power.append(Node(
				node,
				role,
				self.path + "/power/exp1/logs/" + file,
				self.path + "/power/exp1/consumption/m3_" + node + ".oml",
				POWER,
				self.time)
			)

	# Génère 
	def get_nodes_logs(self):
		# On rentre dans le dossier logs
		for file in os.listdir(self.path + "/logs"):
			# Si ce n'est pas un fichier txt
			if not file.endswith(".txt"):
				continue

			# Si le nom du fichier est "coordinator"
			if file == "coordinator.txt":
				role = COORDINATOR
				num = -1
			else:
				role = SENDER
				# Le numéro du noeud est les caractères après sender
				num = file[6:]
				# On récupère le numéro du noeud
				num = num.split(".")[0]
				# On récupère le numéro du noeud
				num = int(num)
				
							
			# On crée le noeud
			self.nodes_logs.append(Node(
				num,
				role,
				'',
				self.path + "/logs/" + file,
				LOGS,
				self.time)
			)

	def get_power(self):
		# On calcule la somme de la puissance
		return sum([node.get_power() for node in self.nodes_power])

	def get_power_mean(self):
		# On calcule la moyenne de la puissance
		return self.get_power() / len(self.nodes_power)
	
	def get_power_senders(self):
		# On calcule la somme de la puissance
		return sum([node.get_power() for node in self.nodes_power if node.role == SENDER])

	def get_power_mean_senders(self):
		# On calcule la moyenne de la puissance
		return self.get_power_senders() / self.nbSenders
	
	def get_power_coordinator(self):
		# On calcule la somme de la puissance
		return sum([node.get_power() for node in self.nodes_power if node.role == COORDINATOR])

	def get_consumption(self):
		# On calcule la consommation totale
		return sum([node.get_consumption() for node in self.nodes_power])

	def get_consumption_mean(self):
		# On calcule la moyenne de la consommation
		return self.get_consumption() / len(self.nodes_power)
	
	def get_consumption_senders(self):
		# On calcule la consommation totale
		return sum([node.get_consumption() for node in self.nodes_power if node.role == SENDER])
	
	def get_consumption_mean_senders(self):
		# On calcule la moyenne de la consommation
		return self.get_consumption_senders() / self.nbSenders
	
	def get_consumption_coordinator(self):
		# On calcule la consommation totale
		return sum([node.get_consumption() for node in self.nodes_power if node.role == COORDINATOR])
	
	def get_mean_useful_throughput(self):
		# On calcule la moyenne du débit utile
		return sum([node.get_useful_throughput() for node in self.nodes_logs]) / len(self.nodes_logs)
	
	def get_mean_useful_throughput_senders(self):
		# On calcule la moyenne du débit utile
		return sum([node.get_useful_throughput() for node in self.nodes_logs if node.role == SENDER]) / self.nbSenders
	
	def get_mean_useful_throughput_coordinator(self):
		# On calcule la moyenne du débit utile
		return sum([node.get_useful_throughput() for node in self.nodes_logs if node.role == COORDINATOR])
	
	def get_useful_throughput(self):
		# On calcule la somme du débit utile
		return sum([node.get_useful_throughput() for node in self.nodes_logs if node.role == SENDER])

	def get_mean_loss_rate(self):
		# On calcule la moyenne du taux de perte (uniquement sur les noeuds envoyeurs)
		return sum([node.get_loss_rate() for node in self.nodes_logs if node.role == SENDER]) / self.nbSenders

	def get_mean_delay(self):
		# On calcule la moyenne du délai (uniquement sur les noeuds envoyeurs)
		return sum([node.get_delai() for node in self.nodes_logs if node.role == SENDER]) / self.nbSenders

	def __str__(self):
		string = "====== " + self.path + " ======\n"
		string += "Nb nodes: " + str(len(self.nodes_power)) + "\n"
		string += "Nb senders: " + str(self.nbSenders) + "\n"
		string += "Protocol: " + self.protocol + "\n"
		string += "Slot size: " + str(self.slotSize) + "\n"
		string += "Time: " + str(self.time) + "s\n\n"
		string += "=== Power ===\n"
		string += "Power: " + str(self.get_power()) + " W\n"
		string += "Power mean: " + str(self.get_power_mean()) + " W\n"
		string += "Power senders: " + str(self.get_power_senders()) + " W\n"
		string += "Power mean senders: " + str(self.get_power_mean_senders()) + " W\n"
		string += "Power coordinator: " + str(self.get_power_coordinator()) + " W\n"
		string += "Consumption: " + str(self.get_consumption()) + " Wh\n"
		string += "Consumption mean: " + str(self.get_consumption_mean()) + " Wh\n"
		string += "Consumption senders: " + str(self.get_consumption_senders()) + " Wh\n"
		string += "Consumption mean senders: " + str(self.get_consumption_mean_senders()) + " Wh\n"
		string += "Consumption coordinator: " + str(self.get_consumption_coordinator()) + " Wh\n"

		string += "\n=== Network ===\n"
		string += "Mean useful throughput: " + str(self.get_mean_useful_throughput()) + " B/s\n"
		string += "Mean useful throughput senders: " + str(self.get_mean_useful_throughput_senders()) + " B/s\n"
		string += "Mean useful throughput coordinator: " + str(self.get_mean_useful_throughput_coordinator()) + " B/s\n"
		string += "Useful throughput senders: " + str(self.get_useful_throughput()) + " B/s\n"
		string += "Mean loss rate: " + str(self.get_mean_loss_rate()) + " %\n"
		string += "Mean delay: " + str(self.get_mean_delay()) + " ms\n"
		return string
