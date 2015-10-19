Sub-organization information 
============================

-   Sub-organization with whom you hope to work(\*): pgmpy

Student Information
===================

-   Name(\*): Pratyaksh Sharma
-   Email(\*): psharma1707@gmail.com
-   Telephone(\*): +91 720 804 9809
-   Time zone(\*): GMT +5:30
-   IRC nick on freenode.net: pratyash
-   Source control username(s)(\*): Github:
    [pratyakshs](https://www.google.com/url?q=http://www.github.com/pratyakshs&sa=D&usg=AFQjCNHD_xB9RDGl5X8_w5p4UI7I0nXN7g)
-   Instant Messaging information: Google Hangouts:
    [psharma1707@gmail.com](mailto:psharma1707@gmail.com)
-   Any other ways we can reach you: Skype: psharma1707
-   Blog(s)(\*):
    [Blogger](https://www.google.com/url?q=http://pratyaksh-gsoc2015.blogspot.com&sa=D&usg=AFQjCNEukKJ24Sm8_0mIw8E_HZKVD1x6Gg)
-   GSoC Blog RSS feed(\*):
    [Link](https://www.google.com/url?q=http://pratyaksh-gsoc2015.blogspot.in/feeds/posts/default?alt%3Drss&sa=D&usg=AFQjCNEuVq2jvTdw5QrCqMndR1rFdpmK6Q)
-   Resume:
    [Link](https://www.google.com/url?q=https://www.dropbox.com/s/zxd4fib36pgy4f0/resume.pdf?dl%3D0&sa=D&usg=AFQjCNHKDrrw9ra7k84KI7ruGSyK3PEbuw)
-   Primary Language: English

University Information
======================

-   University(\*): Indian Institute of Technology, Bombay
-   Major(\*): Computer Science and Engineering
-   Current Year and Expected Graduation date(\*): Currently in 3rd
    year, expected to graduate in Aug 2016.
-   Degree(\*) (e.g. BSc, PhD): B.Tech.

Project Proposal Information
============================

-   *Proposal Title*(\*): pgmpy: Implementation of sampling algorithms for
    approximate inference in probabilistic graphical models
-   *Proposal Abstract* (\*): 
    - Currently pgmpy supports algorithms like Variable Elimination and Belief Propagation for exact inference. In large graphs (particularly those having large treewidth), exact inference becomes computationally intractable.
    - Thus, there's a need for approximate algorithms which answer the inference query with a lower time complexity.
    - In this project I will implement the two most popular algorithms which fall under the more general class of  Markov Chain Monte Carlo methods

        - Gibbs Sampling. My implementation will follow closely the discussion in section 12.3.1-12.3.3 of [Koller]^[[1]](#ftnt1)^
        - Metropolis–Hastings algorithm. Refer section 12.3.4 of [Koller]1
    - Will implement a general framework which will allow easy installation of more MCMC algorithms.
    - Basically, there are a variety of MCMC sampling methods. If time permits, I shall implement
        - Blocking Gibbs sampler
        - Collapsed Gibbs sampler
        - Rao-Blackwellisation
        - AND/OR importance sampling
        - Hamiltonian MCMC (becoming increasingly popular in recent times)

References:

1.  Chapter 12. Koller, Daphne, and Nir Friedman. Probabilistic
    graphical models: principles and techniques. MIT press, 2009.
2.  B. Bidyuk, V. Gogate, R. Dechter: Tutorial on Sampling Techniques
    for Probabilistic and Deterministic Graphical models (AAAI-2010).
    [Link](https://www.google.com/url?q=https://www.ics.uci.edu/~dechter/talks/tutorial-aaai-2010.pdf&sa=D&usg=AFQjCNHLTeGOgjbfC2hG5RZpUEJ4T0GPMQ)

        

Detailed description of algorithms
==================================

-   Sampling based estimation:

    -    Given a process to sample from a probability distribution
    ![](images/image00.png), we sample ![](images/image01.png). The
    ![](images/image02.png)’s are sampled independently and identically
    from ![](images/image00.png).
    -   To estimate any function ![](images/image03.png) of
    ![](images/image00.png), we could use the result:

                ![](images/image04.png)
    
-   Monte Carlo algorithms are based on the fact that while it may not be feasible to compute expectations under ![](images/image05.png), it may be possible to obtain samples from ![](images/image05.png),
    or from a closely related distribution  such that marginals and other expectations can be approximated using sample-based averages.

-   Gibbs sampling is an example of a Markov chain Monte Carlo (MCMC)
    algorithm. In an MCMC algorithm, samples are obtained via a Markov
    chain whose stationary distribution is the desired
    ![](images/image05.png). The state of the Markov chain is a set of
    assignments of values to each of the variables, and, after a
    suitable “burn-in” period so that the chain approaches its
    stationary distribution, these states are used as samples
-   The Markov chain for the Gibbs sampler is constructed in a
    straightforward way:

    -   at each step one of the variables ![](images/image06.png) is
    selected (at random or according to some fixed sequence),
    -   the conditional distribution ![](images/image07.png) is computed,
    -   a value ![](images/image08.png)is chosen from this distribution, and
    -   the sample ![](images/image08.png)replaces the previous value of the
    ith variable.

-   The implementation of Gibbs sampling thus reduces to the computation
    of the conditional distributions of individual variables given all
    of the other variables. For graphical models, these conditionals
    take the following form:

                

        where ![](images/image09.png)denotes the set of cliques that
contain index ![](images/image10.png). This set is often much smaller
than the set ![](images/image11.png)of all cliques, and in such cases
each step of the Gibbs sampler can be implemented efficiently.

-   When the computation of the above equation is overly complex, the Metropolis-Hastings algorithm can provide an effective alternative. Metropolis-Hastings is an MCMC algorithm that is not based on
    conditional probabilities, and thus does not require normalization.

-   Given the current state ![](images/image12.png) of the algorithm, Metropolis-Hastings chooses a new state ![](images/image13.png) from a “proposal distribution,” which often simply involves picking a
    variable ![](images/image14.png) at random and choosing a new value for that variable, again at random. The algorithm then computes the “acceptance probability”:

        ![](images/image15.png)        

-   With probability ![](images/image16.png) the algorithm accepts the proposal and moves to ![](images/image13.png), and with probability ![](images/image17.png) the algorithm remains in state ![](images/image12.png). For graphical models, this computation also turns out to often take the form of a simple message-passing algorithm.


Timeline
========

        The following is merely a modest sketch. It is possible that if
the allocated work for a week completes earlier than time, I shall start
the next week’s tasks. On the contrary, a week’s tasks may spill over to
the next. This timeline is quite a lenient one for me. I believe I will
end up exceeding my promises

-   Week 1:

    -   Implement Forward Sampling (FS), Rejection Sampling (FS)
    -   Tune parameters such as:
        -   Number of samples required to estimate a distribution.
    -   Deliverables: A method which takes as arguments a Bayesian Network
        and an evidence set and returns the distribution P(Y | E=e), where Y
        is the set of unobserved variables and E is the evidence set.

-   Week 2:

    -   Implement Importance Sampling (IS)
    -   Write tests+documentation for FS, RS and IS

-   Week 3:

    -   Implement a general purpose Markov Chain Monte Carlo class which has
        methods that take as input a Markov Chain (with corresponding
        transition probability matrix) and simulates a run of the same.
    -   Write tests+documentation

-   Week 4:

    -   Write functions to compute various statistics  which compares
        probabilities across different initializations and across different
        windows in the same run.
    -   Tune parameters (window size, various thresholds) for deciding if
        the distribution has converged to a stationary one.
    -   Deliverables: An MCMC class with methods to sample from it and
        report various statistics to decide mixing.
    -   Write tests+documentation

-   Week 5:

    -   Implement plots/charts etc. for visualizing the statistics computed
        in week 4.

    -   This will help the user decide if the distribution has converged.

    -   Write tests+documentation

-   Week 6:

    -   Within the MCMC class, write functions to generate the Gibbs chain,
        given a Bayesian Network or Markov Network.
    -   Implementing the transition model.
    -   Write tests+documentation

-   Week 7:

    -   With the Gibbs chain, write a function to sample a target Gibbs
        distribution
    -   Deliverables: A method to estimate the Gibbs distribution of a
        bayesian network or a markov network.

-   Week 8:

    -   Write tests for inference using Gibbs sampling.
    -   Analyse performance

    -   Compare (time/space efficiency+accuracy) with exact algorithms
    -   Find performance bottlenecks (a compact representation of states is
        absolutely necessary).

-   Week 9:

    -   Implement the framework for Metropolis-Hastings algorithm
    -   Write methods to initialize the proposal distribution and acceptance
        distribution
    -   Write an interface for inference which supports the various
        algorithms in pgmpy for both undirected and directed models.
    -   Deliverables: Methods supporting various inference (approximate)
        queries on graphical models.

-   Week 10:

    -   Tests+debugging+documentation for Metropolis-Hastings
    -   Do a performance analysis + look for improvements
    -   Buffer time

-   Week 11:

    -   Write an interface for inference which supports the various
        algorithms in pgmpy for both undirected and directed models.
    -   Deliverables: Methods supporting various inference (approximate)
        queries on graphical models.
    -   Write documentation+tests

-   Week 12:

    -   Complete the integration
    -   Complete documentation
    -   Test edge cases
    -   Buffer time

The documentation for each week’s work shall be done by the end of that
week only. In any case, any code shall not stay undocumented for more
than 1-2 weeks.

The documentation shall also contain ipython notebook(s) which will form
part of the tutorial.

Link to a patch/code sample
===========================

-    I submitted two pull requests, both of which have been merged.

    -   Fixed a bug, which was causing issues with the latest version of
        networkx (1.9.1)
        [https://github.com/pgmpy/pgmpy/pull/346](https://www.google.com/url?q=https://github.com/pgmpy/pgmpy/pull/346&sa=D&usg=AFQjCNHcanfLKaasd2rD4FLwUawZLK37cw)
    -   Added functionality to compute induced graph
        [https://github.com/pgmpy/pgmpy/pull/349](https://www.google.com/url?q=https://github.com/pgmpy/pgmpy/pull/349&sa=D&usg=AFQjCNGYNrWdn5SeUs3lJHKmemQzMJA0vA)

Time Commitment
===============

        Approximately 40 hours per week or the amount of time required
to finished the tasks allocated for the week (whichever higher).

Background
==========

I was introduced to graphical models during my second year, from the
coursera course on the same. During May-July 2014, I worked at the
[Graphical Model
Algorithms](https://www.google.com/url?q=http://graphmod.ics.uci.edu/group&sa=D&usg=AFQjCNEhDa78y8P1qyApkIfVamVK6-hRHw) group
at UC Irvine, under Prof. Rina Dechter. Rina (and her group) has been at
the forefront of research in PGMs. The winning solver at [Pascal
approximate inference competition (at UAI
2012)](https://www.google.com/url?q=http://www.auai.org/uai2012/pascal.shtml&sa=D&usg=AFQjCNFEwz3HwZQ11egcZDZU_JIGKqpTNQ) was
developed at Rina’s group. I worked on weighted best-first search
algorithms for anytime approximate inference in PGMs. My contribution
was to implement the algorithm and compare its performance with the
branch and bound methods (which is the state of the art). The [paper we
wrote](https://www.google.com/url?q=http://www.ics.uci.edu/~dechter/publications/r216.pdf&sa=D&usg=AFQjCNF_R3H5S6GfmIX15a1Ok9r6Rw3Enw) was
accepted at [PlanSOpt workshop at
AAAI’15](https://www.google.com/url?q=http://org.nicta.com.au/plansopt-15-aaai-workshop-planning-search-optimization/&sa=D&usg=AFQjCNGB4GBRUWXEwOfTTr0wJjwOMN8ZBQ).
I also participated in the [PASCAL approximate inference challenge at
UAI
2014](https://www.google.com/url?q=http://www.hlt.utdallas.edu/~vgogate/uai14-competition/leaders.html&sa=D&usg=AFQjCNE1zWiGhxK7VPmqESeIT0WsFfABMg),
submitting the solver that we developed.

*Why pgmpy?*

During my time at UC Irvine, I strongly felt the need of a robust
library for PGMs. The

existing codebase that they used was poorly documented and it took me a
lot of time just to get a hang of it. Around December 2014, I stumbled
upon pgmpy. I found that the organisation participates in GSoC. The
codebase, though quite limited, seemed decently documented. The fact
that the whole project is written in python made it easier for me to
understand (the code at UC Irvine was written in C++). Basically, I feel
a PGM library was desperately needed and I think I’ll have fun expanding
it.

* * * * *

[[1]](#ftnt_ref1) Koller, Daphne, and Nir Friedman. Probabilistic
graphical models: principles and techniques. MIT press, 2009.
