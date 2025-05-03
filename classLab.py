#si-exercise
import numpy as np
import multiprocess as mp # This module is part of the
                          # python standard library
import timeit             # library for timing execution of code


def f(alpha,x1,x2,x3,epsilon):
  return alpha + x1 + 2 * x2 + 0.5 * x3 + epsilon


def average_y(nSample,f):
  alpha = np.random.normal(15,2,nSample) 
  #alpha[:10]

  x1 =  np.random.normal(3,5,nSample) 
  #x1[:10]

  x2 =  np.random.normal(10,1,nSample) 
  #x2[:10]

  x3 =  np.random.normal(8,8,nSample) 
  #x3[:10]

  epsilon =  np.random.normal(0,1,nSample) 
  #epsilon[:10]

  y = f(alpha,x1,x2,x3,epsilon)
  return y.mean()

#average_y(100000000)

def sCalc(n_bins, n_reps, f):
  return [average_y(n_bins, f) for _ in range(n_reps)]

def pCalc(processes, n_bins, n_reps, f):
  pool = mp.Pool(processes=processes)
  results = [pool.apply_async(average_y, (n_bins, f)) for _ in range(n_reps)]
  results = [p.get() for p in results]
  return results


sResults = sCalc(1000,100,f)
pResults = pCalc(1000,100,f)

benchmarks = [] # list to store our execution times

benchmarks.append(timeit.Timer('serial_average(10000, 100, f, 0, 1)','from __main__ import serial_average, serial_integral, f').timeit(number=1))
    # Note that we need to include a second line
    # that imports our functions from __main__.
    # This tells the timer what needs to be IN SCOPE

benchmarks.append(timeit.Timer('parallel_average(2, 10000, 100, f, 0, 1)','from __main__ import parallel_average, serial_integral, f').timeit(number=1))
    # Need to include number of processes
    # when timing the parallel implementation