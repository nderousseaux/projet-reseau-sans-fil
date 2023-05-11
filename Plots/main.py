import sys
from Scenario import *
import matplotlib.pyplot as plt
if __name__ == "__main__":	
	path = sys.argv[1]

	# On écrit en dur les scénarios
	scenarios = [
		Scenario(path + "/scenario1-nb-senders/1", 1, TSCH, 397, 600),
		Scenario(path + "/scenario1-nb-senders/2", 2, TSCH, 397, 600),
		Scenario(path + "/scenario0-etalon", 5, TSCH, 397, 600),
		Scenario(path + "/scenario1-nb-senders/10", 10, TSCH, 397, 600),
	]
	
	# On fait un histogramme de la consommation moyenne des senders get_power_mean_senders()
	plt.bar([str(s.nbSenders) for s in scenarios], [s.get_power_mean_senders() for s in scenarios])

	# Echelle logarithmique
	plt.yscale("log")
	# Titre
	plt.title("Consommation moyenne des senders en fonction du nombre de senders")

	# On affiche les labels
	plt.xlabel("Nombre de senders")
	plt.ylabel("Consommation moyenne des senders (W)")

	# On affiche le graphique
	plt.show()