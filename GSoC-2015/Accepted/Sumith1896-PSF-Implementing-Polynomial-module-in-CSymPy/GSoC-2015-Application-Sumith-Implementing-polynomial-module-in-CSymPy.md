##Personal details

**Name**: Sumith<br/>
**University**: [Indian Institute of Technology, Bombay](http://www.iitb.ac.in)<br/>
**Email**: sumith1896@gmail.com<br/>
**Github/IRC**: [Sumith1896](https://github.com/Sumith1896)<br/>
**Blog**: [sumith1896.github.io](http://sumith1896.github.io/)<br/>
**Time-zone**: UTC+5:30

##Personal background

I am a first year undergraduate pursuing B.Tech. in **Computer Science and Engineering** in [Indian Institute of Technology, Bombay](http://www.iitb.ac.in). I have keen interest in Mathematics, Physics and Computer Science and have been following these subjects from quite a lot of time. I have taken following courses in these three subjects in my first year - Introduction to Computer Programming, Object Oriented Programming, Abstractions and Paradigms for programming, Algorithms: Analysis and Design, Calculus, Linear Algebra, Differential equations, Quantum Mechanics and Electricity and Magnetism.

#Programming details

##Platform details

I use Ubuntu 14.04LTS as my primary work machine with Sublime Text 3 with some useful plugins as my primary text editor because of its features, indentation lines and most importantly I am comfortable with it. I am familiar with the concept of version control and have been using git and GitHub since quite some time and have enough knowledge to carry out the project successfully.

##Programming experience

I have been programming in C++ for the past one year and in Python for past 6 months. I started learning programming about a year ago with the C language. I have developed couple of webpages with JavaScript and web apps with Python, PHP along with SQL database support. My favourite language among these is C++ as I am most proficient in C++ as compared to other languages and whenever it comes to speed and competitive coding, I rely on C++.
Developed a complete game of Sudoku using C++ with gtkmm library for GUI.

##Contribution to CSympy
CSymPy is the first open source project I contributed to and with the help of the great community I have contributed in the following ways:

1. [PR 385](https://github.com/sympy/csympy/pull/385): (Merged) Fixed a printing issue where (3/2)^(1/3) was printed as 3/2^(1/3) prior to the fix and added the necessary tests for this.

2. [PR 404](https://github.com/sympy/csympy/pull/404): (Merged) Changed the printing of pow in CSymPy from a^b to 
a**b so as to match SymPy.

3. [Issue 399](https://github.com/sympy/csympy/issues/399): (Discussion) Initiated the discussion on automatic porting script for SymPy to CSymPy as done in projects such as OpenCV.

##Contribution to SymPy
SymPy has a very interesting codebase which I started exploring parallel to that of CSymPy's and this exploration led to:

1. [PR 8993](https://github.com/sympy/sympy/pull/8993): (Merged) Implementing columnspace of a given matrix,a feature previously unimplemented in SymPy. Added the necessary tests and also updated documentation on this.

2. [PR 9067](https://github.com/sympy/sympy/pull/9067): (Merged) Fixed operators in sympy.physics.quantum.operator to give same results for `A*IdentityOperator()` and `IdentityOperator()*A` where A is an operator.

3. [PR 9069](https://github.com/sympy/sympy/pull/9069): (Pending) Fixed multiplicity(n, 0) from hitting endless recursion which also led log(0, n) to endless recursion.

4. [Issue 8996](https://github.com/sympy/sympy/issues/8996): Printing out integral for non-convergent integral.

#The Project
##Overview
CSymPy currently lacks a polynomial module which is very essential in achieving CSymPy's goal of being the fastest CAS ever. Having a polynomial module is a core concern and implementing a fast module also help in achieving a fast series module. We can use [Piranha's](https://github.com/bluescarni/piranha/) polynomial module, but it has complicated code and does not compile with old compilers. My aim is to implement a sparse polynomial module in CSymPy itself.

##Why this project?
Many a time it happens in physics and mathematics that once a problem is solved you get a lot of insights of the problem when it solved generally(symbolically) than when you solve it numerically given the initial data. This is one of the reasons why symbolic computation interests me.<br/>
Mathematics is pretty close to me and that's why it's CSymPy that I choose to work under. The discussion about algorithms, methods, benchmarks, speed, etc. that happen in the community is really engaging and enriching. With this project, introduction of new modules in CSymPy will allow it to explore new possiblities of CAS speeds and also at the same time being compatible as a optional fast SymPy core.

##Summary of discussions[1]
SymPy uses sparse polys, the sparse polys use a tuple of ints to represent the power in monomials. Then you have a dictionary (hashtable) where you simply store the coefficients.<br/>
Example: `7*x*y + 3*z**3` is stored as dict - `{(1, 1, 0): 7, (0, 0, 3):3}`

The exponents however can be packed into one integer using Kronecker substitution currently unimplemented even in SymPy which I plan to implement in both SymPy and CSymPy as you can use upto 64 bit integer(or _int128 of C++) and number of bits that each exponent requires will be decided on the number of variables, hence packing is possible. Then you use that integer as the key in the hashtable/dictionary to speed up things. Also, multiplying two monomials then just becomes adding the ints of exponents, etc.<br/>
But problems can arise when two monomials are multiplied and there is overflow across bits. To overcome this we check before the operation that the result will fit or not. If not we can convert from packed structure to tuple. Another idea was to use a guard bit which gets switched to 1 then an overflow error is raised but this idea was discarded as this reduces the number of bits per variable. 

If the exponents are too large to be packed, then the code should raise an exception, the user then needs to use the tuple representation using either std::vector<int> in C++, though std::array is faster, as std::vector is allocating on heap, or a faster vector implementation that uses static allocation.

The integer arithmetic, the coefficients of the monomials, must be very fast. This can be done using our very own fast machine integers for small integers and then switch to GMP for large integers. This will be applied for all CSymPy integers, which should speed things up considerably.
 
The hashtable should be tailored for this purpose, so we can store the values directly in the array for one value and a linked list for more than one value. Also, there is a trick to use a 1:1 hash function, [Piranha](https://github.com/bluescarni/piranha) uses that. Usage in Piranha, [here](https://github.com/bluescarni/piranha/blob/master/src/hash_set.hpp).
   
Polynomials with rational(or even extensions for symbols) coefficients and probably rational exponents also needs to be thought of.

Sparse representation is chosen for variety of reasons some being, benchmarks show that sparse representation works better with sparse and semi–dense inputs, thus covers most polynomials that can be encountered in real–life problems of symbolic mathematics.

I plan to do a sparse implementation of polynomial module. The following steps were planned:

1. A fast integer implementation.
2. Kronecker packing of the exponents 
3. Faster hashtable and std::vector. 
4. Use faster c++ class instead of `mpzclass` for all CSymPy integers for speed.

SymPy currently does not have exponent packing which also can be implemented to gain speed.

The end implementation of polynomial module for CSymPy should be working atleast as fast as [Piranha polynomial implementation](https://github.com/bluescarni/piranha/blob/master/src/polynomial.hpp) if not faster.
The series expansion should then be implemented using it. That will provide optimal speed.<br/>
In addition to this some other implementations are planned in the CSymPy polynomial module which will form the base and the module can be expanded from there on.

##The Polynomial Manipulation Module

###Basic functionality
The user will be allowed to declare a polynomial and do basic algebra of addition, multiplication and substitution.
```
RCP<const Polynomial> f = Poly(3*x**3 + 2);
RCP<const Polynomial> g = Poly(x**2 + 2);
```
Note: Multiplying the above two polynomials i.e. `f*g` is planned to returned `(3*x**3 + 2)*(x**2 + 2)` 
	  and not `3*x**5 + 6*x**3 + 2*x**2 + 4` by default but there will be a method `expand()` which will return this on 
	  `expand(f*g)`. The `expand(f*g)` will expand and multiply by Kronecker substitution is explained in detail in implementation details [here](https://github.com/sympy/sympy/wiki/GSoC-2015-Application-Sumith-:-Implementing-polynomial-module-in-CSymPy#multiplication). 

###Division
Division between two polynomials f, g gives quotient q and remainder r such that `f = g*q + r` is satisfied with degree of r is less than q. There will be a `division()` function that takes two polynomial arguments and returns a polynomial.
```
RCP<Polynomial> q;
RCP<Polynomial> r;
division(f, g, outArg(q), outArg(r));
```
Here, `q = 3*x` and `r = -6*x + 2` and 

A more generalised division algorithm will be implemented we reduce a polynomial `f` modulo a set of polynomials `G` i.e. given a polynomial `f` and a set of polynomials `G = (g_1, ..., g_n)`, it computes a set of quotients `q = (q_1, ..., q_n)` and the remainder `r` such that `f = q_1*g_1 + ... + q_n*g_n + r`, where `r` vanishes or `r` is a completely reduced polynomial with respect to `G`.
```
std::vector<RCP<const Polynomial>> q;
RCP<Polynomial> r;
reduced(f, G, std::vector<RCP<const Polynomial>> &q, outArg(r));
```
returns the set of quotients `q` remainder polynomial or completely reduced polynomial `r` with respect to `G`.

###Evaluation
Though there is `subs()` is already implemented in CSymPy, a method `eval()` will be added to the `Polynomial` class which will have a well known algorithm Horner's scheme implemented shown in the implementation section [below](https://github.com/sympy/sympy/wiki/GSoC-2015-Application-Sumith-:-Implementing-polynomial-module-in-CSymPy#evaluation-1).<br/>
Comparison in SymPy
```
In [10]: f = Poly(x**15 + 5*x**13 + x**12 + 7*x**7 + 38*x**4 + 2*x**2 + 10)

In [11]: %timeit f.subs(x, 2)
10000 loops, best of 3: 32.7 µs per loop

In [12]: %timeit f.eval(2)
100000 loops, best of 3: 5.54 µs per loop
```

###Derivative and Integrals
Differention of polynomials with respect symbols will be useful and easy to implement feature.
```
RCP<const Polynomial> b = f->diff(x);
RCP<const Polynomial> c = f->diff(y);
```
Here, `b` will be `9*x**2` and `c` will be the zero polynomial.<br/>
Same goes for the integrals.
```
RCP<const Polynomial> d = f->integrate(x);
RCP<const Polynomial> e = f->integrate(y);
```
Here, `d`will be `3*x**4/4 + 2*x` and `e` will be `3*x**3*y + 2*y`.<br/>
Note: Though it is a indefinite integral, constant is not added, the user is expected to know.

###GCD and LCM
With division, GCD and LCM of univariate and multivariate polynomial can be computed. GCD and LCM are useful as standalone algorithms as well as component of other algorithms. <br/>
```
RCP<const Polynomial> i = gcd(Poly(12*x**2), Poly(4*x));
RCP<const Polynomial> j = gcd(Poly((1/3)*x**2), Poly((1/2)*x));
RCP<const Polynomial> k = lcm(Poly(x*y**2 + x**2*y), Poly(x**2*y**2))
```
The point to be noted here is that if the polynomial has integer coefficients then gcd of coefficients is also considered else the polynomial returned is monic i.e. here `i = 4*x` while `j = x`.<br/>
The polynomial `k` will be `x**3*y**2 + x**2*y**3`.

###Square-free decomposition
Given a polynomial f, square–free decomposition(factorization)[[2](http://en.wikipedia.org/wiki/Square-free_polynomial)]  of f gives a list of polynomials (factors) `f_1, f_2... f_n`, such that all pairs of polynomials `(f_i, f_j)`, for i not equal to j, are co–prime, and `f = f_1*f_2^2*...*f_n^n`. Thus each `f_i` has no repeated roots. Note that square–free decomposition does not give a true factorization into irreducibles, although is a very important step in any factorization algorithm.<br/>
There will be an unordered map defined from `Polynomial` to `Integer` which will be returned or the `umap_basic_num` can be used.<br/>
Example: For
```
RCP<const Polynomial> f = Poly(2*x**2 + 5*x**3 + 4*x**4 + x**5);
umap_basic_num d = sqf(f);
cout<<d;
```
the printed otuput will be `{x + 2 : 1, x : 2, x + 1 : 2}`.

##The benchmarks
CSymPy benchmark system can be improved a lot and I plan to implement benchmarks from Wester's article(or from any other source, suggestions welcome)[[3](http://www.math.unm.edu/~wester/cas/book/Wester.pdf)]. The section H of this article has problems related to algebra and selected ones can be added to benchmark the implemented polynomial module. If time permits, the following sections can also be added:
* C. Numbers<br/>
* G. Number theory<br/>
* I. Trigonometry<br/>
* K. Complex Domain so on.<br/>

This will help in testing it against other CAS. Eventually CSymPy aims to be the fastest and good benchmarks will be necessary. Also this vs Pynac, if positive, can be convincing to replace Sage's core[[4](https://groups.google.com/forum/#!topic/sage-gsoc/WbmAJAaGlhs/discussion)].<br/>
Note: If a better source of great benchmark is suggested, then those will be implemented. These can then be implemented as examples.

**If the above are successfully completed and if time permits, a basic implementation of Groebner bases will be done, highlighting the power of the newly implemented polynomial module**<br>

###Groebner bases
The method of Groebner bases[[5](http://en.wikipedia.org/wiki/Gr%C3%B6bner_basis)] is a powerful technique for solving problems in commutative algebra. Groebner bases provide a uniform approach for solving problems that can be expressed in terms of systems of multivariate polynomial equations. It has many practical applications.<br/>
Calculating a Groebner basis is typically a very time-consuming process for large polynomial systems, hence implementation CSymPy will guarantee speed. The algorithm used for computation is Buchberger's algorithm[[6](http://en.wikipedia.org/wiki/Buchberger%27s_algorithm)]<br/>
Buchberger's algorithm can be viewed as a generalization of the Euclidean algorithm for univariate GCD computation and of Gaussian elimination for linear systems.<br/>
The basic implementation is relatively simple to implement.<br/>
```
RCP<const Polynomial> f[2] = {Poly(x**2 + 1), Poly(x**3 + x*y**4)};
RCP<const Polynomial> g[2] = grobner(f);
```
Then `grobner(f)` returns a polynomial array `[Poly(x**2 + 1), Poly(y**4 -1)]`.

###Near future
The polynomial module will grow and eventually many features will be implemented. Some of them are <br/>
* **cancel()**: Cancels common factors from the numerator and the denominator of a rational function. Depends on the GCD algorithm.<br/>
* **apart()**: Decomposes a univariate rational function f with integer coefficients into partial fractions. Algorithm of Manuel Bronstein will be implemented, also better but limited algorithm of Wang.
* **Factorization** along with factoring in terms of cyclotomic polynomials, expanded factorisation including complex numbers.
* **Polynomial roots** with system of polynomials with help of implemented Groebners basis.
and many more.

##Implementation details
###Data Structures
The polynomial class only handles polynomials in an expanded form.The heart of the module will the data structure, the representation for expanded polynomials is already explained above(in summary of discussions).<br/>
Examples such as `x**2*(x**2+1)**2*(x**2+2)**2` are then represented Mul(Add, Add) as usual in CSymPy.<br/>
The `Poly()` method converts an polynomial expression to that of an object in `Polynomial class`
```
RCP<const Polynomial> f = Poly(x**2 + 2*x + 1);
```
The idea of constructing a `Polynomial` from a integer to integer dict is also a possibility.

###Canonicalization
We should be able to determine that a + b and b + a are equivalent. This is one of reasons why it is important for every `Polynomial` to be stored in canonical form i.e. canonical ordering of terms. Everytime a user enters a poly, it is converted to canonical form. The canonical form for univariate is increasing order of exponent. In the multivariate representation, one approach would be to first sort the terms lexicographically and then by degree.<br/>
For example: Input expression `y**2 + z + x*y + x**2*z + y*z + y*z**2` is then stored as `x**2*z + x*y + y**2 + y*z**2 + y*z + z`.<br/>
This way it is easier for us to judge the equality of former and latter expressions in our system and it is an important design construct which will be used in algorithms of Groebner basis,etc.<br/>
The selection of sorting is irrelevant (whether first by lexicographic order and then degree or vice versa) as long as the choice is consistent.<br/>

###Multiplication
The `expand()` will be implemented will work on Mul when either of the parameters are polynomials. It will use Kronecker's substituion trick[[7](http://en.wikipedia.org/wiki/Kronecker_substitution)][[8](http://www.cs.berkeley.edu/~fateman/papers/polysbyGMP.pdf)]. Here polynomials with integer coefficients are encoded as sufficiently large integers and arithmetics are done using long integer arithmetics, and later results are converted back to polynomials. This is possible by using an isomorphism (a reversible transformation) between polynomials and integers. This algorithm will be efficient as we already have a fast integer arithmetics library.<br/>
Example: Finding product of `f` and `g`, `h = f*g`
```
f = 41*x**3 + 49*x**2 + 38*x + 29
g = 19*x**3 + 23*x**2 + 46*x + 21
f(10**4) = 41004900380029
g(10**4) = 19002300460021
```
Here, the cofficients are `packed` together. Then
```
h(10**4) = f(10**4)*g(10**4) = 779187437354540344421320609.
```
Coefficients of `f` and `g` are `< 50`, so coefficients of `h` are `< 4*50**2 = 10**4`.<br/>
We can unpack `h(10**4)` to obtain
```
h = 779*x**6 + 1874*x**5 + 3735*x**4 + 4540*x**3 + 3444*x**2 + 2132*x + 609
```
In practice a power of two will substituted. We can use coefficients to determine a value of x that is a large enough power of two for that the coefficients of the product `f*g` to be read off from the binary representation of the product number.

###Division
####division()
The specialised `division()` function that will be implemented for two polynomials `f` and `g` will be declared as
```
void division(const RCP<const Polynomial> &f,
    const RCP<const Polynomial> &g,
    const Ptr<RCP<const Polynomial>> &q,
    const Ptr<RCP<const Polynomial>> &r);
```
with usage as
```
division(f, g, outArg(q), outArg(r));
```
The algorithm will be polynomial divison algorithm[[10](http://en.wikipedia.org/wiki/Polynomial_long_division)].

####The generalized division algorithm
The implementation will be carried out same as the `reduced()` is implemented in SymPy[[11](https://github.com/sympy/sympy/blob/master/sympy/polys/rings.py#L1322)]<br/>
```
void reduced(const RCP<const Polynomial> &f,   //help change g and q to arrays
    std::vector<RCP<const Polynomial>> &g,
    std::vector<RCP<const Polynomial>> &q,
    const Ptr<RCP<const Polynomial>> &r);
```
with usage as
```
reduced(f, g, outArg(q), outArg(r));
```
The implementation will be carried out on the same lines as that of SymPy's[11].

###Exponentiation
When `expand()` of exponentiation i.e `f**n` where f is a `Polynomial` and n is an integer constant we apply the repeated squaring algorithm that has the complexity `O(log(n))`.

###Evaluation
A well known algorithm for evaluating univariate polynomial is Horner’s scheme[[12](http://en.wikipedia.org/wiki/Horner's_method)], which is implemented in `eval()` method of SymPy's Poly class. This led significant improvement in execution times as compared to `subs()` method. The same algorithm will be implemented as it's an optimized algorithm for its task and it takes advantage over very fast integers.<br/>
Horner scheme is a very general algorithm, which is also used in SymPy for computing compositions and rational transformations of polynomials, and many other, which require some sort of efficient evaluation of polynomials.
Example:
```
P(x) = a_n*x**n + a_(n-1)*x**(n-1) + ... a_1*x + a_0
```
The Horner scheme computes the value P(t) of the polynomial P at x = t as the sequence of steps starting with the leading coefficient a_n
```
b_k = t*b_(k-1) + a_k
```
for k = n-1, n-2,...1, 0 with `b_n = a_n` reaching `b_0 = P(t)`. This follows from the form,
```
P(x) = (...(a_n*x + a_(n-1))*x +...+ a_1)*x + a_0
```
For univariate polynomials, it returns a `Integer`.
```
RCP<const Integer> value = f->eval(integer(3));
```
Then `value` will be `integer(83)`.<br/>
For multivariate polynomials, it returns a `Polynomial`, also the change in the input API
```
RCP<const Polynomial> k = Poly(x*y**2 + y);
RCP<const Polynomial> m = k->eval(y, integer(2));
```
Then the Polynomial `m` will be `4*x + 2`.<br/>
Another design choice that cna be made is that `RCP<const Basic>` is returned in both cases and then is dynamically casted.

###Differentiation and Integration
The definitions of derivative and integrals are themselves algorithmic in nature. <br/>
These implemented will extend the current `diff()` to differentiate the `Polynomial` class and also `integrate()` with respect to the character entered.

###Greatest Common Divisor

####Algorithm
**EEZ–GCD algorithm of Wang**[[13](http://dl.acm.org/citation.cfm?id=1089228)]<br/>
This is a fast algorithm specifically for sparse polynomials and it computes GCDs of sparse multivariate polynomials over integers and rationals. Implementation of EEZ–GCD algorithm will require the variable–by–variable Hensel lifting algorithm. This will be the main algorithm implemented fo GCD.<br/>

Some other algorithms for exploration are<br/>
**Algorithm-heuristic GCD algorithm**[[14](www.eecs.berkeley.edu/~fateman/papers/phil8.ps)]<br/>
This transforms the problem of computing GCD of polynomials to integer GCD problem. This requires a fast kernel hence currently used in Maple only and SymPy also has an implementation<br/>
Although the algorithm is heuristic, the same algorithm is implemented in SymPy and with current parametrization it never failed in SymPy.<br/>
Because sophisticated sparse algorithm are relatively slow on small problems and emerge superior in large problems, this algorithm is chosen. It is faster than most algorithms for low degree polynomials of upto ten variables.<br/>	
It also requires very efficient integer GCD algorithm, hence the fast integer library will come of benefit.

**Using Grobners basis(optional)**<br/>
An addition algorithm[[15](http://ac.els-cdn.com/S0747717108801058/1-s2.0-S0747717108801058-main.pdf?_tid=d6cbe41a-d39f-11e4-a933-00000aab0f02&acdnat=1427364598_1af8d119916e99d960411c7a47e825fc)] can also be implemented that uses Groebner bases for computing GCD of multivariate polynomials which will done only if Groebner basis is implemented.

###Square-free decomposition
The fast algorithm of Yun[[16](http://en.wikipedia.org/wiki/Square-free_polynomial)] for computing square–free decompositions in domains of characteristic zero for multivariate polynomials. The cost of computing square–free decomposition is equivalent to the computation of the greatest common divisor of f and its derivative. This is dependent on the GCD algorithm.<br/>
Working principle
```
a_0 = gcd(f, f');   b_1 = f/a_0;   c_1 = f'/a_0;   d_1 = c_1 - b_1';   i = 1;
iterate until b = 1
a_i = gcd(b_i, d_i);   b_(i+1) = b_i/a_i;   c_(i+1) = d_i/a_i;   i = i + 1;    d_i = c_i - b_(i+1)';
return a_1, a_2, ... ,a_(i-1)
```

###Groebner bases
**Check for Groebner basis**<br/>
Given a set of polynomials G, one can check if G is a Groebner basis in a finite number of steps using the generalized division algorithm implemented.<br/>
Given two polynomials f and g, to test whether they form Grobner basis.
1. Find `s_polynomial`(defined below) of `f` and `g`.
2. Find remainder of `s_polynomial` with respect to `[f, g]` using `reduced()`.<br/>
If zero, then `f` and `g` form groebner basis.<br/>
If not, then `[f, g, s_polynomial(f, g)]` form groebner basis which can be shown by taking `s_polynomial` pairwise and computing its remainder with the extended array and all turn out to be zero.<br/>
This can be extended for larger arrays.

**Algorithm**<br/>
Methods needed for the algorithm:
* `LM()`: Returns the leading monomial.
* `LT()`: Returns the leading term.
* Also needed will be `lcm()` and `expand()`.<br/>
We then define the notion of s_polynomial.
```
Polynomial s_polynomial(const Polynomial a, const Polynomial b){
	return expand(lcm(LM(f), LM(g))*(1/LT(f)*f - 1/LT(g)*g));
}
```
Note the importance of introducing ordering of monomials in computation of s_polynomial.<br/>
Once the above methods are implemented then improved version of Buchberger's algorithm will be done[[16](http://www.maths.qmul.ac.uk/~whitty/LSBU/MathsStudyGroup/Buchberger.pdf)].<br/>
The same is also implemented in `groebner()` of SymPy[[17](https://github.com/sympy/sympy/blob/master/sympy/polys/groebnertools.py#L52)].<br/>

It should be noted that for linear system of polynomials, this reduces to Gauss-algorithm and hence can be applied to solve that system. In SymPy, it is noted that solving using this method is faster that the Gauss-Jordan implemented using `solve()`
```
>>> F = [x + 5*y - 2, -3*x + 6*y - 15]

>>> %timeit groebner(F, x, y)
100 loops, best of 3: 5.15 ms per loop

>>> %timeit solve(F, x, y)
10 loops, best of 3: 22.7 ms per loop
```

##Timeline
I have no other commitments for this summer and I will be able to contribute for full 50 hours a week. All the programming and learning that I will be doing this summers will be through this project .<br/>
My summer vacation starts on 24th April. Hence, I can start working on full time basis from then on.<br/> 
Though my classes start in mid July, it won't be an issue as I won't have any tests or exams till the coding period ends.<br/>
I will also maintain a blog to get feedback from the community and show my progress.

####Pre-GSoC
* Do an audit of [Piranha](https://github.com/bluescarni/piranha). Clear doubts, if any, with author [Francesco Biscani](https://github.com/bluescarni) or [Ondřej](https://github.com/bluescarni).
* Try out Piranha, look into the integer and hashtable implementation. Go through the polynomial implementation.
* Submit a wiki on the possible algorithms for various implementation and their details.

####Community Bonding
* Chalk out all design details of implementation and decide on undecided areas of implementation possible such as implementation of symbolic coefficients/exponents.<br/>

Work with mentor and implement
* Small integer implementation.
* The faster hashtable implementation.<br/>
Enough understanding of implementation should be gained so that tweaking as per needs is possible in the future.

####Week 1
* Implement a basic polynomial structure, which uses GMP working, with Kronecker substitution used as key in hashtable with add and subtract methods.

####Week 2
* Update the polynomial structure which uses the new integer for small coefficients and switches to GMP for large.
* First the implementation and tests can be carried out for monomials. 

####Week 3
* For multiplication of two monomials, check before the operation that the result will fit or not in packed structure.
* When it does not fit, implement a method to convert from packed structure to tuple
* Update the polynomial structure to use this.
* Send in a PR.

####Week 4
* Implement repeated squaring algorithm for exponentiation.
* Implement benchmarks for the polynomial module.
* Test it against various other CAS polynomial like Piranha, Pynac.
* Check out the areas where improvement is possible.

####Week 5
* Experiment with the implementation, possible tweaking of integer/hashtable implementation will be needed.
* Benchmark and get it working atleast as fast as Piranha if not faster.
* Send in a PR.

####Week 6
* Implement `division()` function.
* Send in a PR.
* Start working on the implementation of generalized division algorithm.

####Week 7
* Complete the implementation of generalized division algorithm.
* Send in a PR.

####Week 8
* Implement the Horner's scheme for evalution methods.
* Implement the `diff()` and `integrate()`.
* Send in a PR.

####Week 9
* Finalize on the GCD algorithm, with insights on how things where done in SymPy.
* Start working on the implementation of GCD algorithm.
* Implement the GCD algorithm

####Week 10
* Complete the implemetation of GCD algorithm.
* Get both `gcd()` and `lcm()` methods working.
* Send in a PR.

####Week 11
* Implement the square-free decomposition
* Send in a PR.

####Week 12
* Implement our very own fast integer for all CSymPy for speed.
* Work on the polynomial documentation.
* Send in a PR.

####Week 13
* A buffer week. Try and get the PRs merged. In case there are some unimplemented details/TODO's, try to finish them off this week.

Note: The tests for the methods implemented will be written simultaneously with the methods, this is not specifically mentioned in the timeline. I’ve tried to structure the timeline so that there is no week which is purely for coding or purely for learning.

###Post GSoC
As I am pretty early in my academic career, I can contribute for years to come and there are many interesting stuff to keep me engaged. I wish to do GSoC because the spirit being new comers are given oppurtunity to be permanent part of an open source team. I plan to take GSoC project as a platform to be one of the strong contributors of CSymPy and SymPy in general. Post GSoC, I have the following plans.
* CSymPy is planned to be a optional fast SymPy core. I want to be part of the team when SymPy is supplied with optional CSymPy.
* The polynomial module will not be completed in a summers time, hence all the remaining features, eventually as much as SymPy will be implemented in the coming year.
* CSymPy has also the chances of being a bigger thing than SymPy itself in the CAS competition. For that the documentation has to be expanded and code needs organization into modules.
* I had gone through the extensive reading period for implementation of solvers in CSymPy which I plan to do in future once it is well figured out in SymPy.<br/>
and hopefully many more interesting things.

##References
[1]Gitter discussions with [@certik](https://github.com/certik)<br/>
[2][Square-free decomposition](http://en.wikipedia.org/wiki/Square-free_polynomial)<br/>
[3][A Critique of the Mathematical Abilities of CA System, Michael Wester](http://www.math.unm.edu/~wester/cas/book/Wester.pdf).<br/>
[4][Discussion on Sage's mailing list, [Make Sage use CSymPy as the symbolic engine](https://groups.google.com/forum/#!topic/sage-gsoc/WbmAJAaGlhs/discussion).<br/>
[5][Groebner Basis](http://en.wikipedia.org/wiki/Gr%C3%B6bner_basis)<br/>
[6][Buchberger's algorithm](http://en.wikipedia.org/wiki/Buchberger%27s_algorithm)<br/>
[7][Kronecker substitution](http://en.wikipedia.org/wiki/Kronecker_substitution)<br/>
[8][Can you save time in multiplying polynomials by encoding them as integers? Richard J. Fateman](http://www.cs.berkeley.edu/~fateman/papers/polysbyGMP.pdf)<br/>
[9]A document on [Kronecker substitution](http://web.maths.unsw.edu.au/~davidharvey/talks/kronecker-talk.pdf)<br/>
[10][Polynomial division](http://en.wikipedia.org/wiki/Polynomial_long_division)<br/>
[11]The implementation of division in SymPy[[1](https://github.com/sympy/sympy/blob/master/sympy/polys/rings.py#L1322)],[[2](https://github.com/sympy/sympy/blob/master/sympy/polys/densearith.py#L1459)].<br/>
[12][Horner's method](http://en.wikipedia.org/wiki/Horner's_method)<br/>
[13][THE EEZ-GCD ALGORITHM, Paul S. Wang](http://dl.acm.org/citation.cfm?id=1089228)<br/>
[14][Evaluation of Heuristic Polynomial GCD, Liao, Fateman](www.eecs.berkeley.edu/~fateman/papers/phil8.ps)<br/>
[15][Three New Algorithms for Multivariate Polynomial GCD, TATEAKI SASAKI AND MASAYUKI SUZUKI](http://www.sciencedirect.com/science/article/pii/S0747717108801058#)<br/>
[16][S-Polynomials and Buchberger’s Algorithm, J.M. Selig](http://www.maths.qmul.ac.uk/~whitty/LSBU/MathsStudyGroup/Buchberger.pdf)<br/>
[17]SymPy's implementation of [Buchberger's algorithm](https://github.com/sympy/sympy/blob/master/sympy/polys/groebnertools.py#L52).<br/>
[18]Mateusz Paprocki's [Master's Thesis](https://mattpap.github.io/masters-thesis/html/src/internals.html).<br/>
[19]DAVID COX, JOHN LITTLE, and DONAL O’ SHEA, Ideals, Varieties and Algorithms. An Introduction to Computational Algebraic Geometry and Commutative Algebra, second ed., Undergraduate Texts in Mathematics, Springer-Verlag, New York, 1997.