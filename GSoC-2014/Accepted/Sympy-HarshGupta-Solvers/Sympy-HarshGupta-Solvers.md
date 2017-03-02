## About Me

### Username and Contact Information

**Name**            :   Harsh Gupta

**University**      :   [Indian Institute of Technology, Kharagpur](http://iitkgp.ac.in)

**email**           :   gupta.harsh96@gmail.com

**IRC Handle**      :   hargup at freenode.net

**github username** :   [hargup](https://github.com/hargup)


### Personal Background

Hello, I am Harsh Gupta a second year undergraduate student at IIT
Kharagpur, India. I'm pursuing a degree in Mathematics and Computing.
I work on Ubuntu 12.04 LTS with vim as my primary text editor. I love vim it for it's power and flexibility.
I'm proficient in C and Python. I like Python because it easily lets me convert
my ideas into code.


## Contributions to Sympy

I first tried to contribute in February 2013 and started working on Issue 
[#6322](https://github.com/sympy/sympy/issues/6322)
at [#1793](https://github.com/sympy/sympy/pull/1793) but abandoned the work
primarily due to lack of confidence and some other reasons.

Then I started working again on Sympy in October-November 2013 and here is a list
of all the merged and unmerged contributions in chronological order:

* (**Merged**) `Integrals.transforms: Fix for issue 2486` [#2498](https://github.com/sympy/sympy/pull/2498)
Caught and raised an `IntegralTransformError` in case `hyperexpand` raised
a `NotImplementedError` in evaluation of Inverse Laplace Transform.

* (**Rejected**) `Evaluating limits when substituting an expression with infinity.`
[#2599](https://github.com/sympy/sympy/pull/2599)
this PR was unnecessary and was a result of misunderstanding of `subs` on my part,
but this PR lead to further fixes #2611 and #2649.

* (**Merged**) `Return infinity for factorial(infinity)` [#2611](https://github.com/sympy/sympy/pull/2611)

* (**Merged**) `Better docs for Subs.` [#2649](https://github.com/sympy/sympy/pull/2649)

* (**Rejected**) `Return NaN for tan and cot at infinity` [#2667](https://github.com/sympy/sympy/pull/2667)
`tan(oo)` and `cot(oo)` returns an evaluated object which sometimes leads to
wrong results like evaluating `limit(tan(x)/x, x, oo)` returns zero. So I proposed
that we return NaN for `cot(oo)` and `tan(oo)` but a wrong fix should not be
an answer to wrong result.

* (**Closed**) `Implemented interval arithmetic.` [#2682](https://github.com/sympy/sympy/pull/2682)
The motivation was basically to provide infrastructure so that we can return `[-1, 1]` for things like
`sin(oo)`.
The work was almost complete but then we decided that general set
expressions will be more useful. [Matthew Rocklin](https://github.com/mrocklin)
is working on Set Expressions at [#2721](https://github.com/sympy/sympy/pull/2721)

* (**Merged**) `Fixed imageset for Interval` [#2723](https://github.com/sympy/sympy/pull/2723)
The evaluation of imageset was correct only for the cases when the function was
monotonic in both positive and negative reals. This PR fixed it.
It was my longest running PR and it lead to a lot of discussion on finding singularities,
completeness of algorithms and on the robustness of solvers. The function `sympy.calculus.singularities` was also added in this PR.

* (**Merged**) `Implemented inequation solver for continuous functions with finite number of solutions` [#2736](https://github.com/sympy/sympy/pull/2736)

* (**Merged**) `Add reference of module solvers.inequalities in documentation.` [#2746](https://github.com/sympy/sympy/pull/2746)

* (**Closed**) `Implemented function to find the points of discontinuities of an univariate real function.` [#2753](https://github.com/sympy/sympy/pull/2753)
This was moved to PR 2723

* (**Merged**) `bool, relational: added as_set method ` [#2781](https://github.com/sympy/sympy/pull/2781)

* (**Merged**) `Piecewise: added as_expr_set_pair property` [#2859](https://github.com/sympy/sympy/pull/2859)

* (**Closed**) `Simplifications for LambertW` [#2870](https://github.com/sympy/sympy/pull/2870) Closed for the need of better patch

* (**Unmerged**) `Added method for intersection for ImageSet` [#2904](https://github.com/sympy/pull/2904)

# The Project

## The Problem and Motivations

Solving equations and system of equations is a crucial feature of Computer
Algebra Systems.
As mentioned in the ideas page we have reasonably powerful but messy equations solvers.
It is a high priority issue in our bug tracker with a milestone for 8.0 release,
so the project the import for long term growth of sympy.


We have following major problems with solve:

1. We don't have a consistent output for various types of solutions

   We need to return a lot of types of solutions consistently:
   * single solution : ` x == 1`
   * Multiple solutions: `x**2 == 1`
   * No Solution: `x**2 + 1 == 0; x is real`
   * Interval of solution: `floor(x) == 0`
   * Infinitely many solutions: `sin(x) == 0`
   * Multivariate functions with point solutions `x**2 + y**2 == 0`
   * Multivariate functions with non point solution `x**2 + y**2 == 1`
   * System of equations `x + y == 1` and `x - y == 0`
   * Relational `x > 0`
   * And the most important case "We don't Know"


2. The input API is also a mess, there are a lot of parameter. Many of them
   are not needed and they makes it hard for the user and the developers to
   work on solvers.

   Thanks to Aaron here is the list of current parameters
   `solve(f, *symbols, dict=False, set=False, exclude=(), check=True,
   numerical=True, minimal=False, warning=False, simplify=True,
   force=False, rational=True, manual=False, implicit=False,
   minimal=False, quick=False)`
   We have to simplify input API.


3. The current solve is not reliable enough, it cannot guarantee that it has
   found all the solutions. This can especially problematic in cases like
   evaluating imageset where missing out solutions can lead to wrong results.
   Moreover solve itself can output wrong result in tricky case like solving `y**w = z` for `y`.
   The answer isn't simply `y = z**(1/w)`. See the Professor Fateman's paper 
   [Why Computer Algebra Systems Can't Solve Simple Equations](http://www.cs.berkeley.edu/~fateman/papers/y=z2w.pdf) 
   for more information.

## The Plan


1. For the first issue I propose to return Set in cases we know the answer and
   an unevaluated Solve object in case solvers fail to get an answer or
   cannot guarantee that it has found all the solutions.

   Though there was some disagreement in past regarding returning set as a result of solve,
   there were no objection in the resent discussions.
   The reasons for set to be appropriate output for solve are:

   * Mathematically solving an equation means returning the set where the equation
     is true.
   * Sets are most generic and can consistently represent all type of solutions.
   * Our set theoretic modules are maturing, the imageset module can be easily used
     to represent both countably and uncountably infinite solutions.

   Set Theoretic capabilities we need to have
   - We don't have any complex sets yet. We need to implement them.
   - We have almost no capability of dealing with multidimensional sets, they
     need to implemented.
   - Sets need to get more powerful to deal with countable infinite sets. For
     example `imageset(x, x*pi, S.Intergers).intersect(Interval(0, 10))` needs to
     work. Some of these techniques are discussed in this draft by Richard Fateman
     http://www.cs.berkeley.edu/~fateman/papers/sets.pdf. After the implementation sympy should be able to:

       * tell about the equality of set {2*n | n in ℕ}, {2*m| m in ℕ}
         and {2*k + 4| k in ℤ ∩ [1, ∞)}

       * tell that {2n + 1| n in ℕ} ∪ {2n | n in ℕ} is same as ℕ

       * {2n + 1| n in ℕ} ∩ {2n | n in ℕ} is ∅

       * Finite sets can result from intersection of infinite sets.

   - Things like S.Intergers - S.Naturals also needs to work. We will have to
     define a Set Difference class.
   - Better imageset evaluator, that will need a more reliable solve.
   - More general set to native type converters, they include Bool to Set and Set to Bool conversion
     for multidimentional sets and bools.


2. Here is the list of all the parameters and my comments on them

   `dict`=True (default is False)
           return list (perhaps empty) of solution mappings

   `set`=True (default is False)
       return list of symbols and set of tuple(s) of solution(s)

   Not needed, sets as output will take care of it.

   `implicit=True (default is False)`
       allows solve to return a solution for a pattern in terms of
       other functions that contain that pattern; this is only
       needed if the pattern is inside of some invertible function
       like cos, exp, ....

   We won't be able to support such output with our new output API

   `force=True (default is False)`
       make positive all symbols without assumptions regarding sign.

   The user can define this in the input_set parameter.

   `rational=True (default)`
       recast Floats as Rational; if this option is not used, the
       system containing floats may fail to solve because of issues
       with polys. If rational=None, Floats will be recast as
       rationals but the answer will be recast as Floats. If the
       flag is False then nothing will be done to the Floats.

   I don't know if people use it. If such flag is not popular we will use
   it. Anyway sympy solvers are mainly for "exact" symbolic coefficient so floating point
   coefficients doesn't really fit in.

   `exclude=[] (default)`
       don't try to solve for any of the free symbols in exclude;
       if expressions are given, the free symbols in them will
       be extracted automatically.

   The new API makes is mandatory to enter the variable as an argument so all symbols
   not given in the variables list is excluded.

   `particular=True (default is False)`
       instructs solve to try to find a particular solution to a linear
       system with as many zeros as possible; this is very expensive

   I'm not sure about this one.

   `check=True (default)`
       If False, don't do any testing of solutions. This can be
       useful if one wants to include solutions that make any
       denominator zero.

   `numerical=True (default)`
       do a fast numerical check if ``f`` has only one symbol.

   `minimal=True (default is False)`
       a very fast, minimal testing.

   `quick=True (default is False)`
       when using particular=True, use a fast heuristic instead to find a
       solution with many zeros (instead of using the very slow method
       guaranteed to find the largest number of zeros possible)


   `warning=True (default is False)`
       show a warning if checksol() could not conclude.


   `simplify=True (default)`
       simplify all but cubic and quartic solutions before
       returning them and (if check is not False) use the
       general simplify function on the solutions and the
       expression obtained when they are substituted into the
       function which should be zero


   `manual=True (default is False)`
       do not use the polys/matrix method to solve a system of
       equations, solve them one at a time as you might "manually".

   All these parameters trade the speed of the solvers with the accuracy. I know there have been issue regarding speed, see https://github.com/sympy/sympy/issues/6611.
   But I still think we should not be using these flags for the reason of maintaining simplicity.
   If a lot of people report that our solvers are too slow then we might reintroduce a few of them.

   It turns out that we might go about not using any of the current parameters and have a clean simple input api as

   `solve(<expression>, <variables>, input_set=<domain of variables>)`


3. To tackle this problem I did an audit of the current solvers at https://github.com/sympy/sympy/wiki/solvers.
   Unfortunately I couldn't complete the whole of it.
   But the audit for univariate equations is complete, and hopefully I understand how
   it works. Here's the summary

   1. If the function is a polynomial, we use various polynomial solving
      algorithms implemented in the polynomials module.
   2. If the function is not a polynomial, we try to reduce it a polynomial with
      suitable generator. e.g., pure trigonometric equations are reduced to
      polynomial of tan.
   3. If the function is of form `f(x)*g(x)` then the overall solution is the
      union of the solution of `f(x)` and `g(x)`.
   4. Then we try to invert the function by various inversion, or try to recognize
      a lambert pattern.
   5. If it fails we force some assumption, to simplify the expression. e.g.,
      `log(f(x)) + log(g(x))` is combined to `log(f(x)*g(x))` assuming both `f(x)`
      and `g(x)` are positive. And the above steps are repeated.


   We have the possibility of loosing a solution:

   - if we get `f(x)*g(x)` in some intermediate stage and the solution of `f(x)` is known but
     the solution of `g(x)` is not know.
   - In simplification process where we force certain assumptions upon the
     expressions and variables. For example while solving `log(f(x)) + log(g(x))` we
     force the assumption that both `f(x)` and `g(x)` are positive and we loose
     solutions in other domain.
   - In case all the function is not injective and all the branches of the inverse
     function are not implemented. Ex: `cos(x) == 0` is inverted to `x == acos(0)`.
     for x in `[0, 2*pi]` and all other branches of inverse of cos are neglected.

   To make sure we don't lose a solution, the code will have to be written in such
   a way that it will be aware of unsafe branches.

## Execution

I plan to execute the project in three phases. After every phase we will have
something that can be directly merged into the code base.

### 1. Building the basic set infrastructure and unevaluated solve class

#### Unevaluated Solve Class

I plan to return set as a solution if and only if it is guaranteed that solve
will return all the solutions for the given function in the given domain. For
every other case an unevaluated solve object will be returned, including the
cases where solve has found some solutions.


```

In[]: soln =  solve((cos(x) - a*x)*sin(x), x, input_set = S.Reals)

In[]: soln
Out[]: Solve((cos(x) - x)*sin(x), Reals())

In[]: soln.expr
Out[]: (cos(x) - a*x)*sin(x)

In[]: soln.know_solutions
Out[]: ImageSet(Lambda(c1, pi*c1), Integers())

In[]: soln.parameters
Out[]: {a}

In[]: soln.ind_vars
Out[]: {x}

In[]: soln.domain
Out[]: ℝ
```

For multivariate solvers
```
In[]: b = var('b', real=True)
In[]: soln =  solve((cos(x*y) - a*y*x)*sin(x*b)*sin(y), (x, y), input_set = S.Reals*S.Reals)

In[]: soln.know_solutions
Out[]: ImageSet(Lambda(c1, pi*c1/b), Integers)*Imageset(Lambda(c1, pi*c2))

In[]: soln.domain
Out[]: 2
      ℝ

In[]: soln.ind_vars
Out[]: {x, y}

In[]: soln.parameters
Out[]: {a, b}
```


#### Set Infrastructure

Building the basic set infrastructure include
- Facilitating basic Set operations
   - Complement and Set Difference
   - Intersections
   - Union

- Other Set Properties
   - Cardinality
   - Equality of Sets

- Usability options
   - Conversion to Relational
   - Conversion to Dictionary
   - Extraction of Parameters and substituting it with some particular value
   - Conversion to lists

**Complement and Set Difference**
```
In[]: s1 = Interval(0, 2)

In[]: s1.complement()
Out[]: (-∞, 0) ∪ (2, ∞)

In[]: s2 = s1.complement(S.Complex)
Out[]: ℂ - (0, 2)

In[]: 1 in s2
Out[]: False

In[]: I in s2
Out[]: True
```


**Intersection**
```
In[]: s1 = imageset(n, 2*n, S.Integers)

In[]: s2 = imageset(m, 2*m + 1, S.Intergers)

In[]: Intersection(s1, s2)
Out[]: ∅

In[]: solve(sin(x), x).intersection(Interval(0, 4))
Out[]: {0, π}

In[]: s = imageset(n, n*pi, S.Intergers)*imageset(m, m*pi, S.Integers)

In[]: s.intersect(Interval(0, 4))
TypeError: Cannot intersect Sets of different dimensionality

In[]: s.intersect(Interval(0, 4)*Interval(0, 4))
Out[]: {(0, 0), (0, π), (π, 0), (π, π)}
```


**Union**
```
In[]: s1 = imageset(n, 2*n, S.Integers)

In[]: s2 = imageset(m, 2*m + 1, S.Intergers)

In[]: Union(s1, s2)
Out[]: ℤ
```


**Cardinality**
```
In[]: S.Natural.cardinality
Out[]: Aleph(0)

In[]: S.Reals.cardinality
Out[]: Aleph(1)

In[]: FiniteSet(1, pi, E).cardinality
Out[]: 3
```


**Equality of Sets**
```
In[]: s1 = imageset((x, y), (cos(x), sin(y)), S.Reals*S.Reals)

In[]: s2 = imageset((x, y), (sin(x), cos(y)), S.Reals*S.Reals)

In[]: Eq(s1, s2)
Out[]: True

In[]: s3 = imageset(n, n**2, S.Integers)

In[]: s4 = imageset(m, m**2 - 2*m + 1, S.Intergers)

In[]: Eq(s3, s4)
Out[]: True


In[]: unit_ring1 = imageset(Lambda((theta), (cos(theta), sin(theta))), Interval(0, 2*pi))

In[]: unit_ring2 = imageset(Lambda((theta), (cos(theta), sin(theta))), S.Reals)

In[]: Eq(unit_ring1, unit_ring2)
Out[]: True
```


**Conversion to dictionaries**
```
In[]: soln = solve(sin(x)*sin(y), (x, y), input_set = Interval(0, 4)*Interval(0, 4))

In[]: soln
Out[]: FiniteSet((0, 0), (0, π), (π, 0), (π, π))

In[]: sol_dict = soln.as_dict(x, y)

In[]: sol_dict
Out[]: [{x: 0, y:0}, {x: 0, y:π}, {x:π, y:0}, {x:π, y:π}]

In[]: (x + y).subs(sol_dict[0])
Out[]: 0
```

**Boolean to set and set to Boolean conversions**

We already have set to Boolean and Boolean to set converters. I plan to extend
them to multidimensional sets.

```
In[]: (x**2 + y**2 < 1).as_set(x, y)
Out[]: {(r⋅cos(θ), r⋅sin(θ)) | r, θ ∊ [0, 1] × [0, 2⋅π]}

In[]: Interval(0, 1)*Interval(0, 3).as_relational(x, y)
Out[]: x ≥ 0 ∧ y ≥ 0 ∧ x ≤ 1 ∧ y ≤ 3

```

**Dealing with parametrised solution**

```
In[]: unit_disk = imageset(Lambda((r, theta), (r * cos(theta), r * sin(theta))), Interval(0, 1) * Interval(0, 2*pi))

In[]: unit_disk.parameters
Out[]: {r, theta}

In[]: unit_disk.subs({r: 1})  # Currently subs doesn't do anything on the imageset
{(cos(θ), sin(θ)) |  θ ∊ [0, 2⋅π]}

```

**Assumptions and Sets**

The assumption system and the set module are closely tied. Assumptions can answer questions like
if `k` is in ℕ, is `k*(k+1)/2` in ℕ ?
This will clearly help in resolving some of the set operations. Likewise
algorithms in Set can be used in assumptions. I will try to
provide a clean interface to go back and forth between set and assumptions.
Unfortunately it is not entirely clear at this point of time how this can be
done. Some of the ideas are discussed here https://github.com/sympy/sympy/pull/2948#issuecomment-35789746 
and on the mailing list https://groups.google.com/forum/#!topic/sympy/Oyz8SkR2fRk.

### 2. Rewriting the current solvers to return set and splitting of various solvers

This is the most important and challenging part of the project.

Both the input API and the output API of current solvers is going to be changed.
The new solvers will have a unified public interface as
`solve(<expressions>, <ordered tuple of variables>, input_set=<domain of variables>)`
with no additional flags or parameter.
The input set defines the domain of variables we using. Because getting all
solutions might not be possible in general, we can restrict our domain to answer
the question "Have we found all solutions?".

Though the input_set parameter doesn't appear to very friendly.
It will allow us to unambiguously represent various types of domains of
the variables. The axis is determined by the order in which variables appear in
the variable list.

Here are some examples from the input API.
```
In[]: solve((x - 2)*(y - 4), (x, y), input_set=Interval(0, 5)*Interval(0, 3))
Out[]: {{2}*Interval(0, 3)}

In[]: solve((x - 2)*(y - 4), (x, y), input_set=Interval(0, 3)*Interval(0, 5))
Out[]: {{2} x [0, 5]} U {[0, 3] x {4}}

In[]: unit_disk = imageset(Lambda((r, theta), (r * cos(theta), r * sin(theta))), Interval(0, 1) * Interval(0, 2*pi))

In[]: solve(f(x, y), (x, y), unit_disk)

```

The output API will be a set of the solution in case we are sure we have found
all the solutions. In case we are not sure it will return an unevaluated solve
object.

Properties of the unevaluated solve object are mentioned above.

We will be breaking up and modularising the solvers horizontally across domains, i.e., Integers,
Reals and Complexes. Then we will be breaking up them vertically across various
types of functions; polynomials, pure trigonometric and hyperbolic equations,
piecewise functions, transcendental equations, misc equations; multivariate polynomials.

While doing this part we will have to be very careful to sure that we know when we
might lose a solution. Also we should be care to not implement any *wrong* algorithm.
Ensuring mathematical correctness can turn out to be a challenge. To help out that
I plan to (other than being careful),
* take regular feedback from the community on the implementation. (it should be
  done anyway)
* present the idea in non code form in wiki and documentation so that people
  not familiar with the code
  can point out the logical fallacies and come up with tricky test cases.
* Whenever possible come up with formal proof of correctness, or existing
  literature to back the implementation.

### 3. Implementing new algorithms

#### Singularities

In some areas it is important that we know what are the critical points of
a functions. For example while evaluating imageset for an interval, the current
algorithm is correct only if the given function is continuous in the given
Interval. Finding singularities is also important in plotting as by that we will
be able to cut the graph it reaches very large values. For example
plotting `1/x` renders to this pretty useless plot.

![Plot 1/x](https://github.com/hargup/sympy/wiki/sing.png)

If we can identify `0` as the point where `1/x` takes infinitely large value we
can avoid plotting till *infinity*.

The current function `sympy.calculus.singularities` is written by me, but it
works only for rational functions. I plan to extend this functionality to more
general functions.

We need solvers to improved to complete this section because we need to know
exactly where we have solutions to not get wrong result.

A reliable singularity finder can help in proving the continuity of function,
that can enable us to implement some new algorithms in solve itself.

```
In[]: singularities(1/x, x)
Out[]: {0}

In[]: singularities(tan(x), x)
Out[]: {π⋅k | k ∊ ℤ}

In[]: singularities(exp(1/x), x)
Out[]: {0}
```

#### Radical Denesting

Using the polynomial formulas for higher degree polynomials returns deeply
nested radicals, which are seldom usable. It is necessary that we simplify them
and reduce the depth of nesting.

Our current denesting code is an implementation of these papers
[http://www.almaden.ibm.com/cs/people/fagin/symb85.pdf](http://www.almaden.ibm.com/cs/people/fagin/symb85.pdf) *excluding the last two sections
[Simplifying Square Roots of Square Roots by Denesting](http://www.cybertester.com/data/denest.pdf)

I propose to implement the remaining sections of the first paper mentioned
above and then
I plan to implement denesting of Ramanujan's Nested Radicals. And if time
permits I'll try to implement root denesting algorithm from the work of R. Zippel
and S. Landau

```
In[]: rootdenest(sqrt(1 + sqrt(3)) + sqrt(3 + 3*sqrt(3)) - sqrt(10 + 6*sqrt(3))
Out[]: 0

In[]: rootdenest((2**(S.One/3) - 1)**(S.One/3))
Out[]:
  3 ___   3 ___    2/3 3 ___
  ╲╱ 6    ╲╱ 3    2   ⋅╲╱ 3
- ───── + ───── + ──────────
    3       3         3

In[]: rootdenest((7*(20)**(S.One/3) - 19)**(S.One/6))
Out[]:
  3 ___  2/3    2/3 3 ___
  ╲╱ 2 ⋅3      3   ⋅╲╱ 5
- ────────── + ──────────
      3            3
```

## Timeline (tentative)

#### Community Bonding period (21st April - 19th May) and Week 1, 2 and 3

My summer vacation will start from 25th of April and I can start coding right
away. As I mentioned in the Execution part I have divided the project into
three parts and after completion of each part we have code that can be merged
and used right away.

* Create an unevaluated solve class
* Create basic set infrastructure

#### Week 4, 5, 6 and 7


Rewriting the current solvers code into various smaller modules
and then making it return a set.


#### Week 8

Since we are changing both the input API and the output API we should expect
to break to a lot of existing code.
It is essential that I fix them before my code
can be merged. Here a list of test failures if solve raises
a `NotImplementedError` for every call https://gist.github.com/hargup/9468786.

#### Week 9, 10 and 11

* Implement general singularity finder
* Implement radical denesting
* Write the test cases from "Review of Symbolic Solvers"

#### Week 12 and 13

* Final brush up. And buffer period.

**Notes**

I have no major plans for summer and I will contribute full time for 40 - 50
hours a week. My college restart in mid July but I will still be able to
contribute full time since there will be no exams or tests.

How do I fit in?
-----------------

I have been working with sympy from quite some time. I'm familiar with
a significant section of the solvers code and I'm well aware of the challenges
of this project. Some of my contributions to sympy are directly relevant to the
completion of this project. For example I'm the author of the
`sympy.solvers.solve_univarite_inequality` and `as_set` method for booleans.
As I mentioned in the singularities sections the current implementation is
authored by me. Also I have contributed the code for imageset evaluation
for intervals.
I am confident that I have the skills and the experience to succesfully
complete the project.

Though there are some loose ends like I don't have a very clear idea of how
multivariate solvers work and I don't claim to have read all the papers
I mentioned in the citation but I can fill these gaps in the pre gsoc period,
and many other details can be worked out during the coding period.

Relevant Issues/ Discussions and References
---------------------------------------------

1. [Action Plan for improving solvers. #2948](https://github.com/sympy/sympy/pull/2948) This contains a lot of discussion on solvers and various other aspects of computer algebra systems. Especially the comments by Professor Richard Fateman are worth reading.
1. https://groups.google.com/forum/#!topic/sympy/OW1ezjt_E5c
1. [GSoC 2014 Solvers](https://groups.google.com/forum/#!topic/sympy/Oyz8SkR2fRk)
1. [#6659](https://github.com/sympy/sympy/issues/6659)  solve is a giant mess
1. [#6766](https://github.com/sympy/sympy/issues/6766)  getting consistent output from solve until a Solution class is available
1. [#4333](https://github.com/sympy/sympy/issues/4333)  solve should give all solutions
1. [#6798](https://github.com/sympy/sympy/issues/6798) solve() should be able to tell you when it knows it's found all the solutions
1. [#4678](https://github.com/sympy/sympy/issues/4678)  Have solve return RootOf when it can't solve equations
1. [#7074](https://github.com/sympy/sympy/issues/7074)  solve(floor (x)-5,x) should not raise NotImplementedError
1. [#5464](https://github.com/sympy/sympy/issues/5464) solve(inequality) should have an option to return a set of intervals
1. [#6547](https://github.com/sympy/sympy/issues/6547)  Cannot solve multivariate inequalities
1. [#5464](https://github.com/sympy/sympy/issues/5464) solve(inequality) should have an option to return a set of intervals
1. [Why Computer Algebra Systems Can't Solve Simple Equations](http://www.cs.berkeley.edu/~fateman/papers/y=z2w.pdf)
1. [syntax for results of solve() and dsolve()](https://groups.google.com/forum/#!topic/sympy/QMr7dds8tSI), it is a very old thread (May 2009) and it mainly compares the output of solve() of Maple and Mathematica.
1. [Add cardinality to sets #2995](https://github.com/sympy/sympy/issues/2995)
1. [Review of Symbolic Solvers](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.44.9444&rep=rep1&type=pdf)
1. [Simplification of Nested Radicals](http://www.computer.org/csdl/proceedings/focs/1989/1982/00/063496.pdf) by Susan Landau
1. [How to tangle with Nested Radicals](http://link.springer.com/article/10.1007%2FBF03024284) by Susan Landau
1. [How to denest Ramanujan's Nested Radicals](http://pdf.aminer.org/001/059/825/simplification_of_nested_radicals.pdf)  by Johannes Blomer
1. [note on “Zippel Denesting” ](http://www.sciencedirect.com/science/article/pii/074771719290004N) by Susan Landau
1. [Simplification of expressions involving radicals ](http://www.sciencedirect.com/science/article/pii/S0747717185800146) by Richard Zippel
1. [Square root denesting #3192](https://github.com/sympy/sympy/issues/3192)
1. [Denesting by Bounded Degree Radicals](http://books.google.com.np/books?id=MUgsCkndkdsC) Page 53
1. [Decreasing the Nesting Depth of Expressions Involving Square Root](http://researcher.watson.ibm.com/researcher/files/us-fagin/symb85.pdf)
1. [Simplifying Square Roots of Square Roots by Denesting](http://www.cybertester.com/data/denest.pdf)
1. [find singularities for any expression #2925](https://github.com/sympy/sympy/pull/2925)
1. [ Comments on Sets in Computer Algebra Systems, especially including Infnite Indexed Sets](http://www.cs.berkeley.edu/~fateman/papers/sets.pdf)
