**statsmodels - Python Software Foundation Google Summer of Code 2015**

**Improvements to Mixed Effects Models**

 

 

## **Sub-organization:** statsmodels 

##  Student Information

* **Name**:					Saket Choudhary

* **Email**: 					[saketkc@gmail.com](mailto:saketkc@gmail.com)

* **Telephone**: 					+1-213-477-3770

* **Time zone**:					GMT -0800 Pacific Time Zone

* **IRC handle**: 					[saketkc@irc.freenode.net](mailto:saketkc@ircfreenode.net)

* **Source control usernames**:

    * **Github**: 				[https://github.com/saketkc/](https://github.com/saketkc/)

    * **Bitbucket**:				[https://bitbucket.org/saketkc](https://bitbucket.org/saketkc)

* **IM**: 						[saketkc@gmail.com](mailto:saketkc@gmail.com)

* **Twitter**: 					[https://twitter.com/saketkc](https://twitter.com/saketkc)

* **Home Page**:					[http://saket-choudhary.me](http://saket-choudhary.me)

* **Blog**: 

    * [http://statsmodels-mlm-gsoc2015.blogspot.com/](http://statsmodels-mlm-gsoc2015.blogspot.com/)

* **GSoC Blog RSS feed**:

    * [http://statsmodels-mlm-gsoc2015.blogspot.com/feeds/posts/default?alt=rss](http://statsmodels-mlm-gsoc2015.blogspot.com/feeds/posts/default?alt=rss)

* **Other personal information you think we would find relevant**:

    * I was part of GSoC’12 and worked on improving the Slideshow publishing API for OERPub with [Connexions](http://cnx.org/) a Rice University project: [[Proposal](http://www.google-melange.com/gsoc/proposal/public/google/gsoc2012/saketkc/5662278724616192)]

    * As part of GSoC’13, I worked for [Galaxy Project](https://wiki.galaxyproject.org/FrontPage), working on python codebase for implementing changes to the workflow system. A major part of my code didn’t make it to the codebase, I however still contribute to the project. We had a [preprint](http://biorxiv.org/content/early/2014/10/19/010538) submitted for part of our work too. [[Proposal](https://docs.google.com/document/d/1CT7cEArKg2VOY3EPFcNiMNjzMxyKZ1WmgOSMb_wnLPI/edit)]

    * I also participated in GSoC’14 with [BioJS](http://biojs.net/) and implemented a [Human Genetic Variation Viewer](http://biojs.io/d/biojs-vis-hgv) , a manuscript is under submission. [[Proposal](https://docs.google.com/document/d/1CT7cEArKg2VOY3EPFcNiMNjzMxyKZ1WmgOSMb_wnLPI/edit?usp=sharing)]

    * I also contribute occasionally to scipy, pgmpy, homebrew-science  

## University Information

* **University**: 				University Of Southern California	

* **Major**: 				Computational Biology & Bioinformatics

* **Current Year**: 			1st

* Expected Graduation date:	2019

* Degree: 				Ph.D

 

## Project Proposal Information

* **Proposal Title**: 			Improvements to Mixed Effects Model

* **Proposal Abstract**:

    * statsmodels.regression.mixed_linear module is relatively new. Mixed effects models are used to often model experiments where a study has been repeated on an individual multiple times in order incorporate fixed-effect parameters and the unobserved random effects. Applications of LMM involve modeling longitudinal data in order to model random effects such as modeling response times for individuals under the influence of different types of drugs.

	

    *  From a user point of view the main features that have been lacking include:

        * **Variance Component models**: Though distinct random effects can be constrained to be independent, the variances are not constrained to be equal

        * **Heteroscedastic Residual errors: **Related issue(tangentially): [https://github.com/statsmodels/statsmodels/issues/1948](https://github.com/statsmodels/statsmodels/issues/1948)

        * **Crossed Random Effects/Nested Random Effects**: The current model of mixed_linear module allows to model only random effect arising out of single factor. Cross-classified data where several factors are expected to have random effects, thus can’t be modeled. Examples of such studies will include gene expression studies where certain set of genes from different individuals are put under certain categories of stress and their expression level is measured. Patients constitute a random sample of the population and so does the level making such studies more cross-design suitable. Nested random effects can be then taken care of implicitly, where each ‘sample’ might be ‘nested’ with other covariates.  This should also implicitly support for uncorrelated random effects.    Related issue: [https://github.com/statsmodels/statsmodels/issues/1946](https://github.com/statsmodels/statsmodels/issues/1946)

	

	Few discussions demanding these features are at: [https://github.com/statsmodels/statsmodels/issues/646](https://github.com/statsmodels/statsmodels/issues/646)

and [https://groups.google.com/forum/#!topic/pystatsmodels/CrHCZkIWj4w](https://groups.google.com/forum/#!topic/pystatsmodels/CrHCZkIWj4w)

* **Deliverables/End Goals & Challenges**

    * **Support for crossed random effects:** This would probably be the most challenging part. The plan is to implement a non-cholmod based way to compute the cholesky decomposition of the error covariance matrix D. Two known  approaches are documented in references [1] and [2].  This will also require significant benchmarking against lme4 methods. General methodology is detailed in [12]

    * **Support for variance component models, heteroscedastic residuals**: nlme supports heteroscedasticity[6]. The implementation details are in [3]. This will also possibly require using sparse methods and hence would depend on the above. A non sparse and slower implementation, is however independent from the above.

    * **Support for other MLE and REML estimation methods**: `lmm` package in R[11] implements several methods for rapid MLE and REML convergence.  Two methods that could likely be ported to statsmodels include: `fastml` and `fastmode` and `fastrml`

    * **Support for nonlinear mixed effect models**: This would be an optional goal, given nonlinear mixed models have too specific use cases[4]

* **Proposal Detailed Description/Timeline**:

<table>
  <tr>
    <td>Week</td>
    <td>Tasks</td>
  </tr>
  <tr>
    <td>
Community Bonding Period

27 April - 24 May</td>
    <td>
--  Chalk out all possible non-cholmod ways of handling sparse cases. This would require understanding the discussions in [1] and [2], taking mentors and statsmodels community’s input.</td>
  </tr>
  <tr>
    <td>
Week 1 

May 25 - May 31
</td>
    <td>
-- Support for heteroscedastic residual errors 
-- Documentation and Unit tests</td>
  </tr>
  <tr>
    <td>
Week 2 and Week 3

June 1- June 7, 
June 8 - June 14
</td>
    <td>
-- Implement generic class for performing  non-cholmod based cholesky decompositions

-- Documentation and Unit tests</td>
  </tr>
  <tr>
    <td>
Week 4, Week 5

June 15 - June 21, 
June 22 - June 28</td>
    <td>
--  Implementation of crossed random effects support using non-cholmod support

-- Tests and documentation
</td>
  </tr>
  <tr>
    <td>
Week 6
June 29 - July 5
</td>
    <td>
-- Implement support for variance components models for constrained random effects

-- Tests and Documentation</td>
  </tr>
  <tr>
    <td>Midterm Deliverables</td>
    <td>
--  A generic non cholmod for sparse calculations

--  Support  for crossed random effects

--  Support for specifying variance component models
</td>
  </tr>
  <tr>
    <td>
Week 7 

July 6 - July 12, 
</td>
    <td>
--  Port `fastml` methods from `lmm`

-- Tests and documentation</td>
  </tr>
  <tr>
    <td>
 Week 8

July 13 - July 19
</td>
    <td>
--  Port `fastml` methods from `lmm`

-- Tests and documentation</td>
  </tr>
  <tr>
    <td>
Week 9

July 20 - July 26 </td>
    <td>
-- Port ‘fastmode` from lmm R package

-- Tests and documentation
</td>
  </tr>
  <tr>
    <td>
Week 10 and Week 11

July 27 - August 2</td>
    <td>
-- Support for nonlinear models

-- Tests and documentation</td>
  </tr>
  <tr>
    <td>
Week 12

August 3 - August 9</td>
    <td>-- Code Profiling

-- iPython Notebook demos

-- Tests and documentation
</td>
  </tr>
  <tr>
    <td>Week 13

August 10 - August 17
August 18 - August 24</td>
    <td>-- Code Profiling
-- iPython Notebook demos
-- Tests and documentation
</td>
  </tr>
  <tr>
    <td>Term end Deliverables</td>
    <td>-- Support for non-linear mixed effects
 
-- IPython notebooks with examples benchmarking/comparing methods against methods from `lme4`, `lmm` and `nlme`(wherever applicable)
</td>
  </tr>
</table>


I have deliberately kept the last two weeks as buffer periods in order to accommodate any pending/overdue tasks from previous weeks.

**References**:

1. Parameter Estimation in High Dimensional Gaussian Distributions [http://www.math.ntnu.no/preprint/statistics/2012/S5-2012.pdf](http://www.math.ntnu.no/preprint/statistics/2012/S5-2012.pdf)

2. FaST linear mixed models for genome-wide association studies(See supplement): [http://www.nature.com/nmeth/journal/v8/n10/abs/nmeth.1681.html](http://www.nature.com/nmeth/journal/v8/n10/abs/nmeth.1681.html)

3. Pinheiro, J.C. and Bates, D.M. (2000). *Mixed-Effects Models in S and S-Plus*. Springer

4. Nonlinear Mixed Effects Models [http://www4.stat.ncsu.edu/~davidian/nlmmtalk.pdf](http://www4.stat.ncsu.edu/~davidian/nlmmtalk.pdf)

5. Fasta algorithms for ML and RML esitmation in linear models: [http://raptor1.bizlab.mtsu.edu/s-drive/TEFF/Rlib/library/lmm/doc/improve.pdf](http://raptor1.bizlab.mtsu.edu/s-drive/TEFF/Rlib/library/lmm/doc/improve.pdf)

6. lme4 heteroscedasticity: [https://stat.ethz.ch/pipermail/r-sig-mixed-models/2014q4/022753.html](https://stat.ethz.ch/pipermail/r-sig-mixed-models/2014q4/022753.html)

7. Current status of Mixed Linear models in statsmodes: [http://statsmodels.sourceforge.net/devel/mixed_linear.html](http://statsmodels.sourceforge.net/devel/mixed_linear.html)

8. lme4 book: [http://lme4.r-forge.r-project.org/book/](http://lme4.r-forge.r-project.org/book/)

9. lme4 implementation: [http://econ.ucsb.edu/~doug/245a/Papers/Mixed%20Effects%20Implement.pdf](http://econ.ucsb.edu/~doug/245a/Papers/Mixed%20Effects%20Implement.pdf) and MJ Lindstrom, DM Bates (1988). "Newton Raphson and EM algorithms for linear mixed effects models for repeated measures data"

10. Julia implementation: [https://github.com/dmbates/MixedModels.jl](https://github.com/dmbates/MixedModels.jl)

11. lmm in r: [http://cran.r-project.org/web/packages/lmm/lmm.pdf](http://cran.r-project.org/web/packages/lmm/lmm.pdf)

12. Mixed-effects modeling with crossed random effects for subjects and items**: **[http://www.sciencedirect.com/science/article/pii/S0749596X07001398](http://www.sciencedirect.com/science/article/pii/S0749596X07001398)

* **Patches contributed to statsmodels**:

    * On Hold

        * Fix trendorder for trend only models in VAR: [https://github.com/statsmodels/statsmodels/pull/2327](https://github.com/statsmodels/statsmodels/pull/2327)

        * Doc fix for hazard_regression: https://github.com/statsmodels/statsmodels/pull/2236

    * Accepted and Merged

        * Check internet availability before running tests: [https://github.com/statsmodels/statsmodels/pull/2247](https://github.com/statsmodels/statsmodels/pull/2247)

        * Raise exception on incorrect trend type: [https://github.com/statsmodels/statsmodels/pull/2329](https://github.com/statsmodels/statsmodels/pull/2329)

        * Doc fixes for MixedLinear: https://github.com/statsmodels/statsmodels/pull/2333

## Other Schedule Information

I will probably be taking a course during summer 2015. Besides this, I do not have any other commitments during the coding period.

 

