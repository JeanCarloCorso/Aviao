from random import Random
from time import time
from math import cos
from math import pi
from inspyred import ec
from inspyred.ec import terminators
import numpy as np
import os

def generate_(random, args):
	size = args.get('num_inputs', 12)
	return [random.randint(0, 34000) for i in range(size)]
	
def evaluate_(candidates, args):
	fitness = []
	for cs in candidates:
		fit = perform_fitness(cs[0], cs[1], cs[2], cs[3], cs[4],
		cs[5], cs[6], cs[7], cs[8], cs[9],
		cs[10], cs[11])
		
		fitness.append(fit)
	return fitness
	
def perform_fitness(cs0, cs1, cs2, cs3, cs4, cs5, cs6, cs7, cs8, cs9, cs10, cs11):
	
	cs0 = np.round(cs0)
	cs1 = np.round(cs1)
	cs2 = np.round(cs2)
	cs3 = np.round(cs3)
	cs4 = np.round(cs4)
	cs5 = np.round(cs5)
	cs6 = np.round(cs6)
	cs7 = np.round(cs7)
	cs8 = np.round(cs8)
	cs9 = np.round(cs9)
	cs10 = np.round(cs10)
	cs11 = np.round(cs11)
	
	fit = float((((cs0+cs4+cs8)*310/1000)+((cs1+cs5+cs9)*380/1000)+((cs2+cs6+cs10)*350/1000)
				+((cs3+cs7+cs11)*285/1000))/22750)
	h1 = np.maximum(0, float((cs0 + cs1 + cs2 + cs3) - 10000) / 10000)
	h2 = np.maximum(0, float((cs4 + cs5 + cs6 + cs7) - 16000) / 16000)
	h3 = np.maximum(0, float((cs8 + cs9 + cs10 + cs11) - 8000) / 8000)
	
	h4 = np.maximum(0, float((cs0 * 480 + cs1 * 650 + cs2 * 580 + cs3 * 390) / 1000 - 6800) / 6800)
	h5 = np.maximum(0, float((cs4 * 480 + cs5 * 650 + cs6 * 580 + cs7 * 390) / 1000 - 8700) / 8700)
	h6 = np.maximum(0, float((cs8 * 480 + cs9 * 650 + cs10 * 580 + cs11 * 390) / 1000 - 5300) / 5300)
	total = cs0+cs1+cs2+cs3+cs4+cs5+cs6+cs7+cs8+cs9+cs10+cs11
	f=cs0+cs1+cs2+cs3
	c=cs4+cs5+cs6+cs7
	t=cs8+cs9+cs10+cs11
	h7 = np.abs(f / total-10/34)+np.abs(c / total-16/34)+np.abs(t / total-8/34)
	
	fit = fit - (h1+h2+h3+h4+h5+h6+h7)/7
	
	return fit
	
def solution_evaluation(cs0, cs1, cs2, cs3, cs4, cs5, cs6, cs7, cs8, cs9, cs10, cs11):
	cs0 = np.round(cs0)
	cs1 = np.round(cs1)
	cs2 = np.round(cs2)
	cs3 = np.round(cs3)
	cs4 = np.round(cs4)
	cs5 = np.round(cs5)
	cs6 = np.round(cs6)
	cs7 = np.round(cs7)
	cs8 = np.round(cs8)
	cs9 = np.round(cs9)
	cs10 = np.round(cs10)
	cs11 = np.round(cs11)
	print
	print("..: RESUMO DA PRODUCAO: ..")
	print("Lucro total: ", float(((cs0 + cs4 + cs8) * 310/1000 +
	(cs1 + cs5 + cs9) * 380/1000 + 
	(cs2 + cs6 + cs10) * 350/1000 + (cs3 + cs7 + cs11) * 285/1000)))
	print("Quantia levada de cada carga:  \nC1= ",(cs0 + cs4 + cs8)/1000, "\nC2= ", 
	(cs1 + cs5 + cs9)/1000, "\nC3= ",(cs2 + cs6 + cs10)/1000,"\nC4= ",
	(cs3 + cs7 + cs11)/1000)
	print("Compartimentos: \n   Compartimento1 KG\n      * C1= ",cs0, "\n      * C2= ",cs1
	, "\n      * C3= ",cs2, "\n      * C4= ",cs3)
	print("Total Compartimento 1 em Ton: ",(cs0+cs1+cs2+cs3)/1000)
	print("\n   Compartimento2 KG\n      * C1= ",cs4, "\n      * C2= ",cs5
	, "\n      * C3= ",cs6, "\n      * C4= ",cs7)
	print("Total compartimento 2 em Ton: ",(cs4+cs5+cs6+cs7)/1000)
	print("\n   Compartimento3 KG\n      * C1= ",cs8, "\n      * C2= ",cs9
	, "\n      * C3= ",cs10, "\n      * C4= ",cs11)
	print("Total Compartimneto 3 em Ton :",(cs8+cs9+cs10+cs11)/1000)
def main():
	rand = Random()
	rand.seed(int(time()))

	ea = ec.GA(rand)
	ea.selector = ec.selectors.tournament_selection
	ea.variator = [ec.variators.uniform_crossover,
				   ec.variators.gaussian_mutation]
	ea.replacer = ec.replacers.steady_state_replacement

	ea.terminator = terminators.generation_termination
	
	ea.observer = [ec.observers.stats_observer, ec.observers.file_observer]

	final_pop = ea.evolve(generator=generate_,
					  evaluator=evaluate_,
					  pop_size=5000,
					  maximize=True,
					  bounder=ec.Bounder(0, 53000),
					  max_generations=20000,
					  num_inputs=12,
					  crossover_rate=1.0,
					  num_crossover_points=1,
					  mutation_rate=0.25,
					  num_elites=1,
					  num_selected=5,
					  tournament_size=2,
					  statistics_file=open("aviao_stats.csv", 'w'),
					  individuals_file=open("aviao_individuals.csv", 'w'))

	final_pop.sort(reverse=True)
	print(final_pop[0])

	perform_fitness(final_pop[0].candidate[0], final_pop[0].candidate[1],
	final_pop[0].candidate[2], final_pop[0].candidate[3],
	final_pop[0].candidate[4], final_pop[0].candidate[5], 
	final_pop[0].candidate[6], final_pop[0].candidate[7],
	final_pop[0].candidate[8], final_pop[0].candidate[9],
	final_pop[0].candidate[10], final_pop[0].candidate[11]
	)
	solution_evaluation(final_pop[0].candidate[0], final_pop[0].candidate[1],
	final_pop[0].candidate[2], final_pop[0].candidate[3],
	final_pop[0].candidate[4], final_pop[0].candidate[5], 
	final_pop[0].candidate[6], final_pop[0].candidate[7],
	final_pop[0].candidate[8], final_pop[0].candidate[9],
	final_pop[0].candidate[10], final_pop[0].candidate[11]
	)
	#solution_evaluation(final_pop[0].candidate[0], final_pop[0].candidate[1])

main() 
