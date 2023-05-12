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
		# On récupère les noeuds
		self.get_nodes_power()
	
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
		return string
