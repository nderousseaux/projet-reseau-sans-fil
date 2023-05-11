import sys
from Scenario import *

if __name__ == "__main__":	
	path = sys.argv[1]

	# On écrit en dur les scénarios
	scenarios = [
		Scenario(path + "/tsch-orchestra-nb-senders/1", 1, TSCH, 397, 600),
		Scenario(path + "/tsch-orchestra-nb-senders/2", 2, TSCH, 397, 600),
		Scenario(path + "/scenario0-etalon", 5, TSCH, 397, 600),
		Scenario(path + "/tsch-orchestra-nb-senders/10", 10, TSCH, 397, 600),
	]
	# On affiche tout les scénarios
	[print(scenario) for scenario in scenarios]