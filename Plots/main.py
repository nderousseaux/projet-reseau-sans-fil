import sys
from Scenario import *
import matplotlib.pyplot as plt

scenario_etalon = None

def analyse_nb_senders(path):

	# On écrit en dur les scénarios
	scenarios = [
		Scenario(path + "/s1-nb-senders/1", 1, TSCH, 397, 600),
		Scenario(path + "/s1-nb-senders/2", 2, TSCH, 397, 600),
		scenario_etalon,
		Scenario(path + "/s1-nb-senders/10", 10, TSCH, 397, 600),
	]
	
	# # On fait un histogramme de la consommation moyenne des senders get_power_mean_senders()
	# plt.bar([str(s.nbSenders) for s in scenarios], [s.get_power_mean_senders() for s in scenarios])

	# # Echelle logarithmique
	# plt.yscale("log")
	# # Titre
	# plt.title("Consommation moyenne des senders en fonction du nombre de senders")

	# # On affiche les labels
	# plt.xlabel("Nombre de senders")
	# plt.ylabel("Consommation moyenne des senders (W)")

	# On affiche le graphique
	plt.show()

	# On fait un histogramme du débit utile du réseau
	plt.bar([str(s.nbSenders) for s in scenarios], [s.get_useful_throughput() for s in scenarios])

	# Titre
	plt.title("Débit utile du réseau en fonction du nombre de senders")

	# On affiche les labels
	plt.xlabel("Nombre de senders")
	plt.ylabel("Débit utile du réseau (kbps)")

	# On affiche le graphique
	plt.show()

	
def analyse_size_slot(path):
		# On écrit en dur les scénarios
	scenarios = [
		Scenario(path + "/s3-size-slot/100", 5, TSCH, 100, 600),
		Scenario(path + "/s3-size-slot/200", 5, TSCH, 200, 600),
		scenario_etalon,
		Scenario(path + "/s3-size-slot/1000", 5, TSCH, 1000, 600),
	]
	
	# On fait un histogramme de la consommation moyenne des senders get_power_mean_senders()
	plt.bar([str(s.slotSize) for s in scenarios], [s.get_power_mean_senders() for s in scenarios])

	# Echelle logarithmique
	plt.yscale("log")
	# Titre
	plt.title("Consommation moyenne des senders en fonction de la taille des slots")

	# On affiche les labels
	plt.xlabel("Taille des slots")
	plt.ylabel("Consommation moyenne des senders (W)")

	# On affiche le graphique
	plt.show()


if __name__ == "__main__":	
	# On écrit en dur le scénario étalon
	# scenario_etalon = Scenario(path + "/s0-etalon", 5, TSCH, 397, 600)

	# # On analyse le nombre de senders
	# analyse_nb_senders(path)

	# Exemple
	s = Scenario("Scenario/s1-nb-senders/2", 2, TSCH, 397, 600)

	print(s)


