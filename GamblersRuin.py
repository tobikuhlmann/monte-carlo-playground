import numpy as np

class GamblersRuin(object):
	"""
	Three fair coins tossed. Heads gets +1, tails -1, pay-offs are added and net pay-off added to equity.
	The 3 tosses are repeated 1000 times. Initial equity is 10 dollars
	p: probability that gambler is successful/ wins at each round.
	i: gambler's initial amount of money/reserves
	"""

	def __init__(self, p, init_bal):
		self.p = p
		self.init_bal = init_bal
		self.bal = init_bal
		self.q = 1 - self.p
		self.realizations = np.array(self.init_bal)
		self.simulation_results = []

	def coin_toss(self):
		"""
		One coin flip with payoff (1, -1) with probability (p,q)
		"""
		outcome = np.random.uniform(0, 1)

		if outcome < self.p:
			result = 1
		else:
			result = -1

		return result

	def play_one_round(self):
		"""
		Three coin tosses in one round round
		"""
		result_round = 0
		for i in range(0,3):
			result_round += self.coin_toss()
		return result_round

	def gamble(self, no_rounds):
		"""
		One round is played until ruin or no_rounds times
		"""
		self.realizations = np.array(self.init_bal)
		self.bal = self.init_bal

		round = 1
		while round < no_rounds:
			round_result = self.play_one_round()
			if (self.bal + round_result) >= 0:
				self.bal += round_result
			else:
				break
			self.realizations = np.append(self.realizations, self.bal)
			round += 1

	def simulate(self, no_simulations, no_rounds):
		# Gamble multiple times and store realization paths
		self.simulation_results = []

		for game in range(1,no_simulations+1):
			self.gamble(no_rounds=no_rounds)
			self.simulation_results.append(self.realizations)

	def probability_ruin(self):
		# Analytical solution for calculating probability of ruin if you play infinite games
		if self.p > 0.5:
			prob_ruin_analytical = 1 - ((self.q/self.p) ** self.init_bal)
		else:
			prob_ruin_analytical = 1

		# Probability of ruin in simulation
		# number of ruin / number of still in the game
		no_ruin = self.simulation_results
		return prob_ruin_analytical


if __name__ == "__main__":
	# probability of success
	p = 0.5
	# initial amount
	init_bal = 10
	# number of rounds
	no_rounds = 100
	# number of simulations
	no_simulations = 100

	gr = GamblersRuin(p=float(p), init_bal=int(init_bal))
	#result = gr.coin_toss()
	#result = gr.play_one_round()
	#print(result)
	#gr.gamble(no_rounds=no_rounds)
	#print(gr.realizations)
	gr.simulate(no_simulations=no_simulations, no_rounds=no_rounds)
	print(gr.simulation_results)