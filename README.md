# Stochastic Processes
A collection of Python code and reports completed as homework assignments for UCSB's PSTAT 160A - Stochastic Processes (Fall 2016).

# What are stochastic processes?
In an introduction to probability theory, you were probably taught about things called random variables.
Stochastic processes are collections of these random variables indexed by time. They are useful for modelling
random processes which take place over a certain time period, e.g. weather.

## Classifying Stochastic Processes
We can differentiate various types of stochastic processes from each other by considering their:
* State space
* Time indices (discrete or continuous)

The *state space* is simply a collection of different "states" our process can be in. For example, in a weather model, possibles states 
might include "raining," "snowning," or "sunny."

## How Stochastic Processess Work
Every stochastic process starts at a certain initial state, e.g. a weather model might start on a sunny day. Then, for every unit of time going
forward, there is a probability we will move to another state.

## Specific Types of Stochastic Processes
In PSTAT 160A, we covered two types of stochastic processes:
* Markov Chains
 * Markov Chains are, at the basic level, a discrete time, discrete space stochastic process
 * Each state of a Markov Chain depends only on the previous state
 * For every stating state, we define a probability the random process moves into a different state (for every possible resultant state)
   by the next unit of time.
    * We call these probabilities **transition probabilities**
    * For every initial state, the sum of transition probabilities must equal 1.
 
* Poisson Process
 * A continuous time, discrete space stochastic process
 * A type of counting process, i.e. a Poisson Process counts the number of events that have occured time x.
  * Example: The number of earthquakes in California
  * By the nature of a counting process, a Poisson process can only increase in value.
 * The expected number of events in any time interval is a Poisson random variable.
  * The expected number of events in any time intervals of similar length are identically and independently distributed Poisson random variables.
 * The average time between two events (called the **waiting times** or **interval arrival times**) are identical and independent
  Exponential random variables.
