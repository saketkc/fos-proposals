## Table of Contents

* [Basic Information](#basic-information)
* [Personal Background](#personal-background)
* [The Project](#the-project)
* [Prototype](#prototype)
* [Timeline (Tentative)](#timelinetentative)
* [Notes](#notes)
* [References](#references)

---
# About Me   

## Basic Information

**Name:** Himanshu Mishra<br/>
**University:** [Indian Institute of Technology, Kharagpur](http://en.wikipedia.org/wiki/Indian_Institute_of_Technology_Kharagpur)<br/>
**Major:** Mathematics and Computing<br/>
**Email:** himanshu2014iit@gmail.com<br/>
**IRC:** orkohunter<br/>
**Github:** [OrkoHunter](https://www.github.com/orkohunter)<br/>
**Blog:** http://blog.himanshumishra.in<br/>
**Blog RSS Feed:** http://blog.himanshumishra.in/feeds/posts/default/-/networkx<br/>
**Timezone:** IST (UTC +5:30)<br/>

## Background work and Programming Skills

I am a first year student of IIT Kharagpur, India. I'm pursuing a degree in Mathematics and Computing. I work on Linux Mint 17 LTS. I use Sublime Text for development and vim for SSH sessions. I am proficient in C and Python. 

Python easily lets me convert my ideas into code. I like it mainly because it is an interpreted language which gives you freedom to do so much things dynamically. Prototyping anything in Python is very easy and requires less man-work than any other programming language. I like IPython a lot. I have very great experience reading tutorials on IPython notebooks specially the ones for numpy.

Since I started programming as a web developer, I used django all the time which made me familiar with Python in the beginning.

I like `itertools` because of its magical functions which are written to handle iteration based algorithms. They are fast and use memory efficiently.

I know how to use Git and Github. If I am stuck, I go to Google and always come back with a solution.

#The Project   
##The Problem and Motivation   

NetworkX being a pure python library provides a swift way for people to use it because python doesn't need a compiler, so everything goes smoothly on the python interpreter. In spite of that, it is realized that there also exists other graph packages written in other programming languages. While they being written in compiled languages, they offer rich functionalities whose reimplementation in Python is an important task. Some of the common fuctionalities between networkx and other packages have greater performance in them due to their use of compiled languages. This motivates us strongly to integrate them with NetworkX and make it more awesome.

Related to the add-ons, in [#1325](https://www.github.com/networkx/networkx/issues/1325) it was suggested to remove the drawing package out of the NetworkX core package. The thought is that graph drawing should be more interesting for developing purposes for those developers who are interested in visual elements, external graphics packages rather than algorithms and data structures. Keeping it under NetworkX umbrella as `networkx-matplotlib` would make it more easier to develop and maintain.

##The Plan   

Integration doesn't seem to have a single and best way. There are mixed ideas discussed in [#1167](https://github.com/networkx/networkx/issues/1167) to choose the way of implementation.
As I sum up, there are mainly two ways to do this.

1. Handling every add-on package in `networkx.external`. All of their necessary modules would reside in the respective sub-directory of the package in `networkx.external`. Then writing code to NetworkX that interfaces between NetworkX objects and bare lists/arrays expected by the add-on package. Decorators and namespaces can be handled in `networkx.utils`. And lastly, changing `setup.py` to handle installation related issues, the way Cython works. When Cython is not available, it would skip the installation part of the add-on and everything would work as if there is no add-on system for NetworkX.
But this will lead to complication as all those code in NetworkX for the add-on packages and their modules itself would still remain there, unused and counterproductive. That's why we should go on for the other way.

2. Having add-ons as "optional components" under NetworkX umbrella. First of all NetworkX proper should not take those add-ons for granted that they would reliably exist. If so, then they should become an integral part of NetworkX alike NumPy and SciPy. Further, adding more add-ons should be as smooth as appending a list of add-ons. So, the idea is that `setup.py` should inspect and load configurations from `networkx.external.addons` and let the add-ons decide whether they can be installed or not.

My work can be divided into three phases.

####Phase 1: Designing the approach for add-on implementation

A separate repository under NetworkX umbrella on Github will be hosted as `networkx-<addon>` containing the add-on source files, tests and code files written for Cython. The python wrapper, however will be present in the NetworkX proper package. For example, a module named `partition` will be created in `networkx.addons.<add-on>` to provide the partitioning functionality for NetworkX.

Regarding `setup.py`, it will not be edited for each and every add-on to avoid the condition which will quickly inflate the file. Rather it will inspect `networkx.external.addons`, so the add-ons which are present, will be installed leaving no conflictions with those which are not present but are mentioned in `networkx.addons`.

####Phase 2: Working with two graph libraries and hosting the add-ons on Github

I will have to show that the implemented add-on system works. For this I'll have to implement two officially sanctioned add-ons and host them on github. For this I choose the following two libraries-

1. METIS is a set of serial programs written in C, used for partitioning graphs, partitioning finite element meshes, and producing fill reducing orderings for sparse matrices. It is a truly amazing software. Some of its key features are High Quality Partitions, Extraordinary speed and production of efficient low fill orderings.

2. LEMON is graph library written in the C++ language which provides implementations of common data structures and algorithms with focus on combinatorial optimization tasks connected mainly with graphs and networks. LEMON is an abbreviation of Library for Efficient Modeling and Optimization in Networks. LEMON employs generecity in C++ by using [templates](http://en.wikipedia.org/wiki/Template_%28C%2B%2B%29).

Both these add-ons will be hosted on Github under NetworkX umbrella. I plan to work on the respective forks. By the end of every week or two, there will be something to merge.

####Phase 3: Working with graph drawing package of NetworkX

In this period, I will use the implemented add-on system to have the drawing package out of networkx main repository and be implemented as an add-on being hosted as a separate sub-repository under NetworkX umbrella as `networkx-matplotlib`. This will not be similar to implementing a C/C++ add-on as it will not require any wrapper or Cython. This will be a straight forward implementation of a python module as an add-on.

Additionally I'll be writing tests side by side. Solving all the bugs in the last is really a bad idea as compared to not letting them emerge. However, if any hiccups still persists, I'll try to solve them before merging the final work.

##Prototype

One of the prime issues of this project is how the NetworkX API is going to be used while interaction with the add-ons. How the implementation of add-ons are going to change the original NetworkX core package. Such things got discussed in [#1429](https://github.com/networkx/networkx/issues/1429). 

There should be clear distinction between the results obtained by using the NetworkX algorithms and their equivalent ones in the add-on. For instance, say I want to use `some_func()` over some_graph `G`. The prototype looks like this

    >>> import networkx as nx
    >>> from networkx.external.addons import lemon
    
    >>> G = nx.build_some_graph()
    >>> #Result using networkx
    >>> result_nx = nx.some_func(G, *args, **kwargs)
    >>> #Result using lemon
    >>> result_lemon = lemon.some_func(G, *args, **kwargs)

In this way, any algorithm of any add-on need not to interfere with original algorithms of networkx. However, there arises a situation when someone is using networkx over their own code base which is pretty large. To them, it would be more handy to replace all the instances of networkx with algorithms of the add-on library. To meet this need, there can be something like `use_addon(addon.some_func)` in the local namespace.

    >>> import networkx as nx
    >>> from networkx.external.addons import lemon
    
    >>> G = nx.build_some_graph()
    >>> #Result using networkx
    >>> result_nx = nx.some_func(G, *args, **kwargs)
   
    >>> #Result using lemon
    >>> result_lemon = lemon.some_func(G, *args, **kwargs)

    >>> nx.use_addon(lemon.some_func)
    >>> #Now nx.some_func will use lemon.
    >>> result = nx.some_func(G, *args, **kwargs)

Facilitating an add-on should be with more open options for the user. That's why both the APIs are favorable.

While doing

    >>> from networkx.external.addons import lemon
This does not indicate that all the add-on functions will reside in that `networkx.external.addons` namespace. Those will be provided along with the bindings in the separately hosted addon package, like `networkx-lemon` in this case. So, to use its functions, we need to import them into the local namespace. So, the `lemon.py` in `networkx.external.addons` would be looking like this:

```
try:
    from networkx-lemon import *
except ImportError:
    print("Please install networkx-lemon to use this add-on")  # Or maybe raise an exception?
```    

##Timeline(Tentative)   

**Community Bonding Period (27 April - 25 May)**

**Goal**: Community Bonding

* The principle focus in this period would be studying in detail, the functionalities of NetworkX, making notes, so as to compare them with that of the add-ons.

* I'll ask guidance from my mentor upon the functioning of the add-on because that is the most crucial part of my project.

* If possible, I would also start coding in this phase only, so that I get a head-start

**Week 1 - Week 2 (25 May - 9 June)**

**Goal**: Creating the add-on system

* I'll create the general add-on system skeletal. I'll finish when NetworkX will be ready to be implemented with add-ons.

* I'll also draw the skeletal of the sub-repositories. By this week, the first `networkx-<add-on>` will be hosted on Github.

**Week 3 - Week 4 (10 June - 26 June)**

**Goal**: Implementing METIS

* I'll start first with implementing METIS. I'll take [ysitu's](https://www.github.com/ysitu) [work](https://github.com/ysitu/networkx/commit/bd0cf745e327e8410290f5b8f21f98e1d836b59a) as my starting point.

* In this period, I'll be writing Python wrappers of METIS graph partitioning functions.

* I'll also be writing tests along with it

**Mid term Evaluation**

* Having fully functioning add-on sytem with one nontrivial add-on working properly.

* Fix bugs if any

**Week 5 - Week 7 (27 June - 17 July)**

**Goal**: Modifying Lemon Graph Library for use

* Lemon Graph Library has more varied functionalities. This period will be dedicated to studying and modifying the functions to be used.

* As soon as I'll finish modifying the Lemon graph packages, I'll head forward to write code to NetworkX.

**Week 8 - Week 10 (18 July - 7 August)**

**Goal**: Writing code to NetworkX, Writing tests

* In this period I'll be writing Python wrappers of Lemon Graph library functions

* Finishing the add-on after writing tests

**Week 11 - Week 12 (8 August - 21 August)**

**Goal**: Working with NetworkX-Matplotlib

* Remove NetworkX drawing package out of the proper package and implement it as a add-on for NetworkX while it being hosted on github under the umbrella of NetworkX.

* Finishing/fixing bugs for existing add-ons so far.

**Future Work -** Continue working over the add-on system forever. I'll love to see future implementations on it.

I'll be writing my notes through out the progress. Later on I'll write IPython notebook tutorials for the work I'll have done.

I would be able to devote 40 - 50 hours a week during the project, since I have no other big project devoted for the summer. My summer vacations start by 29 April and I'll not be engaged in vacations. My academic year would begin by July 17, but for the first month I would still be able to devote around 40 hours, since there would be no tests/exams.

---


### Notes

* I have no commitment during summer which means I'm free to work completely on my project.

* I am very enthusiastic about my work being beneficial to other people in the open source community. I'll keep on seeing the work done by me and fixing issues if they emerge in future.

---

### References

* Overview of graph libraries
http://lemon.cs.elte.hu/trac/lemon;
http://glaros.dtc.umn.edu/gkhome/metis/metis/overview
* Source codes http://people.sc.fsu.edu/~jburkardt/c_src/metis/metis.html;
http://lemon.cs.elte.hu/trac/lemon/wiki/Downloads
* Related issues https://github.com/networkx/networkx/issues/1167;
https://github.com/networkx/networkx/issues/1325
