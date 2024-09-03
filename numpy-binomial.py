"""
1. Start by importing the numpy library.
2. Call the random.binomial() method to simulate 
  - a single (1) coin toss 
  - using a biased coin that has a 0.8 probability of landing on heads. We will call heads successful.
  - conducted 500 times.
3. Now lets increase the number of trials per experiment.
Call the random.binomial() method to simulate
  - 100 tosses
  - using a biased coin that has a 0.8 probability of landing on heads. We will call heads successful.
  - conducted 500 times.
"""
import numpy

numpy.random.binomial(n=1, p=0.8, size=500)

numpy.random.binomial(n=100, p=0.8, size=500)