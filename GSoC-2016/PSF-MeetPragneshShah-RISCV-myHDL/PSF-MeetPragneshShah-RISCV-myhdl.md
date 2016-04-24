MyHDL: RISC-V Implementation
----------------------------

Student Info
------------

-   Name : Meet Pragnesh Shah
-   City : Mumbai, India
-   Skype : meetshah1995
-   Email : meetshah1995@gmail.com
-   Alternate Email : meetshah1995@ee.iitb.ac.in
-   Github : [https://github.com/meetshah1995/](https://www.google.com/url?q=https://github.com/meetshah1995/&sa=D&ust=1461475401415000&usg=AFQjCNHdoqY63LlFnCvv3EO-JX6wv4V5pA)
-   GSoC Blog Feed URL : [http://myhdl-meetshah1995.blogspot.com/feeds/posts/default](https://www.google.com/url?q=http://myhdl-meetshah1995.blogspot.com/feeds/posts/default&sa=D&ust=1461475401416000&usg=AFQjCNHgtMl1WSROu7xHjZRlqel52_FKcQ)
-   Telephone : \<placeholder\>
-   IRC nick : meetshah1995
-   Primary Language : English
-   Time zone : GMT +5:30
-   Website : [http://meetshah1995.github.io](https://www.google.com/url?q=http://meetshah1995.github.io/&sa=D&ust=1461475401418000&usg=AFQjCNGaCSM2poUKLWMwq7XdO5QobftNyg)
-   Resume : \<placeholder\>

### Education

-   University: Indian Institute of Technology Bombay (IIT-Bombay)
-   Degree: B.Tech & M.Tech (Dual Degree) in Electrical Engineering
-   Current Year: 3rd (Junior)
-   Graduation Year: 2018
-   Minors: Computer Science and Operations Research
-   Master's Specialization: Communications and Signal Processing

Patches Submitted
-----------------

-   Make the resync parameterizable sync\_reset(clock, reset\_in, reset\_out, synclen=2) and fifo\_syncers cleanup.

-   [https://github.com/cfelton/rhea/pull/8](https://www.google.com/url?q=https://github.com/cfelton/rhea/pull/8&sa=D&ust=1461475401423000&usg=AFQjCNFAjYfBqaqjMOBL8Pricj2crZvegw)

-   Currently working on increasing the test coverage for enum and always\_seq blocks.

-   [https://github.com/meetshah1995/myhdl](https://www.google.com/url?q=https://github.com/meetshah1995/myhdl&sa=D&ust=1461475401424000&usg=AFQjCNF5WfBI0x8cerMDCMeX3bk-CASeaw)

Project Info
------------

### Proposal Title

-   Title : RISC-V CPU and CPU design tools implementation in myHDL

### Proposal Abstract

RISC-V is an open ISA freely available for all types of use. The RISC-V ISA has been designed with small, fast, and low-power real-world implementations in mind, but without "over-architecting" for a particular microarchitecture style.

The RISC-V being a base ISA  is carefully restricted to a minimal set of instructions sufficient to  provide a reasonable target for compilers,  assemblers,  linkers,  and  operating  systems  (with additional supervisor level operations),  and so provides a convenient ISA and software toolchain skeleton around which more customized processor ISAs can be built.

This project thus aims to leverage and demonstrate the advantages of myHDL and python in general in the field of CPU design by implementing a RISC-V CPU (in myHDL) and other CPU design utilities. Since RISC-V is a base ISA, having a myHDL based implementation becomes a essential and would enable a lot of Computer Architecture researchers to design and test RISC-V based derivatives using myHDL and python based utilities.

 

### Features and Deliverable Specifications

The module features would be as follows on a very high level:

-   A robust, correct, rigorously tested implementation of a simple 32-bit CPU based on the RISC-V ISA in myHDL.
-   The modules (and corresponding tests) that shall be delivered by me would be :

-   RISC-V ISA decoder in pure python and myHDL..
-   A simple 32-bit non-pipelined RISC-V based CPU.
-   A 3 stage pipelined design based on RISC-V.
-   Full 6 stage pipelined design based on RISC-V.
-   Utility tools for CPU design.    

-   QA tests for developed for RISC-V module to check correctness & performance.
-   Tutorials and Documentation for the module and tools.

### Project Timeline

This is merely a modest sketch. I have tried to be as lenient as possible in assigning the weekly tasks. The last 1-2 days of a Week will usually be reserved for code review and documentation or buffers to complete work which has not been completed in the allotted time. Though I intend to keep in touch with the mentor throughout the week and ensure that I am going in the right direction, I have tried to maintain a feasible feedback mechanism in the schedule so as to ensure that my mentor gives feedback on a reviewable quantity of code at appropriate intervals.

Documentation : The documentation for each week's work shall be done by the end of that week only. In any case, any code shall not stay undocumented for more than 1-2 weeks.

Tests : The tests for individual modules shall be developed using a working RISC-V core [3] and using intermediate outputs as stimulus to respective blocks and comparing the output with ground truth. The testing also will be done over a chain of blocks using respective ground truths and stimulus to test sequential correctness. The tests will also be carried out on FPGAs (Altera DE0) to test synthesizability.

CPU Design Utilities : The present RISC-V repository provides a lot of CPU design utilities in shell [5] .As the project goes through, key utilities from the repository will be identified and implemented to support our implementation of the RISC-V CPU. A few other important utilities (like calculating CPI at variable workloads) will also be implemented. This is a non-exhaustive list and I will be implementing them as and when time permits, after GSoC as well.

-   Community Bonding period:

-   Read and brush up the relevant theory (RISC-V Instruction Set Architecture) needed to implement the module.
-   Get working knowledge of the of processor variants [3], modifications of which will be reused in implementing the RISC-V module.

-   Week 1 (6th May - 13th May):

-   Start with the decoder (both the python and myHDL) implementation.
-   Define the interface needed for the ISA decoding and simulation.
-   Writing the pseudocode for decoder module, laying out the classes and methods to be used which will help during implementation.
-   Write tests for the decoder module.
-   QA testing of the the decoder module

-   Week 2 (13th May - 20th May):

-   Begin implementation of the non-pipelined CPU.
-   Use existing datapath from a Verilog design and identify key modules.
-   Define the interface, classes and methods needed for the different modules [Register file, ALU, IR, encoders etc]  of the design taking help from existing designs.
-   Write the tests for individual processor modules.

-   Week 3 (20th May - 27th May):

-   Continue with the CPU implementation.
-   QA testing of the CPU.

-   Week 4 (27th May - 3rd June):

-   Begin implementation of the 3 staged pipelined CPU.
-   Use existing pipelined datapath from a Verilog design and identify key modules.
-   Define the interface, pipeline stages, classes and methods needed for the different modules [fetch, decode, execute etc.] of the design taking help from existing designs.
-   Identify the hazards and implement a Hazard Detection Unit [HDU].
-   Write the tests for the individual processor modules

.

-   Week 5 (3rd June - 10th June):

-   QA testing of the entire 3 staged processor.
-   Bug-squashing for errors in the processor implementation.
-   FPGA based testing of the processor.

-   Week 6 (10th June - 17th June):

-   Begin implementation of the 6 stage in-order pipelined CPU similar to the Rocket core [4].
-   Use existing pipelined datapath from a design and identify key modules.
-   Define the interface, pipeline stages, classes and methods needed for the different modules of the design taking help from existing designs.
-   Write the tests for the individual processor modules

-   Week 7 (17th June - 24th June):

-   Generate tests for individual processor modules.
-   Continue the implementation and side by side unit testing.

-   Week 8 (24th June - 1st July):

-   QA testing of the entire processor module.
-   Exhaustive chat with mentors regarding mid-term evaluation and some parts of code that I might need to improve upon.

-   Week 9 (1st July - 8th July):

-   Testing the entire processor synthesized on a FPGA.
-   Identification of utilities to be implemented and discussion with mentor to finalize a list of them.

-   Week 10 (8th July - 15th July):

-   Implementing the CPU design utilities in python and myHDL.
-   Identifying and running comparisons tests to find the plus points of using myHDL and python over conventional CPU design tools.
-   Writing the tests for the utilities.
-   Exhaustive documentation and tutorial writing begins.

-   Week 11 (15th July - 22th July):

-   Documentation and Buffer to complete any remaining parts.
-   Try to port the entire RISC-V utils repo and experiment with out-of order and other architectural intricacies if things finish early.

-   Week 12 (22th July - 29th July):

-   Write tutorials explaining how to use the module and other utilities.
-   Ideally a week to complete any remaining documentation of the code.
-   Buffer week for analyzing the suggestions by the myhdl community and talking to the mentor regarding implementing the same.
-   Implementing the suggestions.
-   Final evaluation exhaustive chat with mentors and a feedback for the change in the code needed.

Summer Availability
-------------------

-   Classes End Date: 15/04/2016 (dd-mm-yyyy)
-   Exams End Date: 05/05/2016
-   Work Hours per week: Approximately 42 hours per week or the amount of time required to finished the tasks allocated for the week (whichever is higher).

Extra Information
-----------------

###     Background

Being a electrical engineering student and interested in High Level Synthesis and VLSI, I think this is a very good opportunity for me to get hands on development experience in this field. I am definitely prepared to learn more about it in the summers and explore this interesting field. I think given my interests, I would like to add more functionalities to my-hdl post GSoC as and when time permits me.

I designed two RISC Multi-cycle ([code](https://www.google.com/url?q=https://github.com/yashbhalgat/Multicycle-RISC-Processor&sa=D&ust=1461475401450000&usg=AFQjCNEpEyWvhnwTnHm4UXF8F2X-zLb_jg)) [[report](https://www.google.com/url?q=https://github.com/yashbhalgat/Multicycle-RISC-Processor/blob/master/report/Final_%2520Report_Meet_Navjot_Yash.pdf&sa=D&ust=1461475401451000&usg=AFQjCNG2EVfDVQtu_R7HzVKt0he5422kNQ)] and Pipelined processors ([code](https://www.google.com/url?q=https://github.com/navisngh11/Pipelined-RISC15-Processor&sa=D&ust=1461475401452000&usg=AFQjCNEKzav6ArrxwtX9IJmwRpRyIYGwBA)) [[report](https://www.google.com/url?q=https://github.com/navisngh11/Pipelined-RISC15-Processor/blob/master/Report/Pipelined_RISC_Report.pdf&sa=D&ust=1461475401453000&usg=AFQjCNHqjmSsTl0aLU4ASehca2HvegzRIw)] as a part of my EE309 Microprocessors course and have been through rigorous verilog exercises as a part of my EE224 Digital Systems Lab. I also interned at Computation Acceleration team at University of Illinois at Urbana-Champaign's Advanced Digital Sciences Center where in I developed an synthesizable arbitrary precision fixed and floating point library for their High Level Synthesis tool which also works with Vivado and Calypto.I thus feel that I have experience with the concepts and skills needed to complete this project.

Coding Preferences

I have been interested in Open Source programming since my freshman year at college. I was a part of the Autonomous Underwater Vehicle ([AUV-IITB](https://www.google.com/url?q=http://www.auv-iitb.org/Web/&sa=D&ust=1461475401455000&usg=AFQjCNE7R-aflCowrJ5pAi9srl4jIGMlIA)) team as a Software engineer where we developed the entire stack for our AUV Matsya (which reached the semi-finals at RoboSub in 2013, 2014 and 2015). I have also done a bunch of other parallel computing, computer vision and image processing like chess playing robot and written a lot of utility software including Django servers and Android apps.

I code on my Ubuntu Desktop using vim as I think the availability of a large number of plugins for vim makes its customizable to suit my needs. I am comfortable with a lot of programming languages but I specifically like Python because of its intuitive interface and very broad spectrum of usage from simple scripting to web applications and scientific uses. One specific feature I like about Python is decorators :).  

MyHDL Example Code

I have ported a few modules to myHDL from my earlier processor design in verilog and will be porting other modules soon. If time permits I will implement the entire RISC processor in myHDL.  

[https://github.com/meetshah1995/myhdl-examples](https://www.google.com/url?q=https://github.com/meetshah1995/myhdl-examples&sa=D&ust=1461475401458000&usg=AFQjCNEbX1xKSp2uEPwzTx7r6YNYX28Yqw)

References
----------

[1](https://www.google.com/url?q=http://riscv.org/specifications/&sa=D&ust=1461475401458000&usg=AFQjCNGMApxZ5ri0-H8rthF8D-ErlJgNFQ) : RISC-V ISA, http://riscv.org/specifications/

[2](https://www.google.com/url?q=https://github.com/riscv&sa=D&ust=1461475401459000&usg=AFQjCNEBo1T8dD4ZIYm32HWw7g0RfX2C1g) : RISC-V Github organization and codebase,  https://github.com/riscv

[3](https://www.google.com/url?q=https://bitbucket.org/casl/shakti_public&sa=D&ust=1461475401460000&usg=AFQjCNHbhwyxru6Mhp7T6d7Cs4vihU69YQ) : RISC-V based processors variants, https://bitbucket.org/casl/shakti\_public   

[4](https://www.google.com/url?q=https://github.com/ucb-bar/rocket&sa=D&ust=1461475401461000&usg=AFQjCNHRcQBPxnDWYL5Ys94O3pGb8kTAmw) : Rocket core, https://github.com/ucb-bar/rocket

[5](https://www.google.com/url?q=https://github.com/riscv/riscv-tools&sa=D&ust=1461475401462000&usg=AFQjCNFDJVWge-zUbH7PqzgZkFk3uNUE_w) : RISC-V tools and utils, https://github.com/riscv/riscv-tools


