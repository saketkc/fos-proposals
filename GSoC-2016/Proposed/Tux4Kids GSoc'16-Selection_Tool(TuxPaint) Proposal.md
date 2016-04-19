Tux4Kids

Google Summer of Code 2016 

Selection Tool Feature(TuxPaint) Proposal

* Dishant Khanna

<table>
  <tr>
    <td>Basic Information
Background work and Programming Skills
The Project (Selection Tool)
The Plan
Timeline
Why Me?</td>
  </tr>
</table>


## **Basic Information**

**Name:** Dishant Khanna	

**University:** [Bharati Vidyapeeth's College of Engineering, New Delhi](https://en.wikipedia.org/wiki/Bharati_Vidyapeeth%27s_College_of_Engineering)

**Major:** Computer Science

**Email:** dishant.khanna1807@gmail.com

**Github:****[DishantK180**7](https://github.com/DishantK1807) 

**LinkedIn: ****[https://in.linkedin.com/in/dishant-khanna-14797bb**1](https://in.linkedin.com/in/dishant-khanna-14797bb1)

**Timezone:** IST (UTC +5:30)* * *


## **Background work and Programming Skills**

I am a Third year student of Bharati Vidyapeeth’s College of Engineering, New Delhi, India. I'm pursuing a degree in Computer Science Engineering. I work on Manjaro XFCE and Windows operating system . I use Sublime Text for development and vim for SSH sessions. I am proficient in **C, C++, Java and Python**. I have done my first year summer training in Advance C- programming and have a strong grasp of the fundamentals of C and C++. 

Python easily lets me convert my ideas into code. I like it mainly because it is an interpreted language which gives you freedom to do so much things dynamically. Prototyping anything in Python is very easy and requires less man-work than any other programming language. I like IPython a lot. I have very great experience reading tutorials on IPython notebooks specially the ones for numpy.

Since I started programming as beginner in C and C++ , I used Code::Blocks, DevC++ and eclipse( for java ) most of the time and later on I made myself familiar with Python.

I know how to use Git and Github. When I am stuck, I go to Google and always return back with a solution.

## **The Project**

## **The Problem and Motivation **(Selection Tool)

Tux Paint is a free and basic drawing program designed for young children (kids ages 3 and up) for their entertainment. It has a simple, easy-to-use interface, fun sound effects, and an encouraging cartoon mascot who helps guide children as they use the program. It provides a blank canvas and a variety of drawing tools to help kids be creative and draw their creative ideas on the canvas.

It is a free and open source software and provides various tools for editing like:

* Paint Brush

* Rubber Stamp 

* Line Tool

* Shape Tool

* Text and Label Tool

* ‘Magic’ Tool

* Eraser

Now, the feature that it lacks is the selection tool. That allows the user to select a particular part of the drawing and implement operations like cut/copy, etc. on it.

**The Plan**

The plan is to create a selection tool for TUX Paint. As I sum up, there are different ways to create a selection tool do this.

1. **Rectangle Selection: **This tool will be used to define a rectangular or square selections on the canvas.

2. **Ellipse Selection 	: **This tool will be used to create elliptical or circular selections on the canvas.

### The third type of selection that can be implemented can be done through **Lasso Select tool. **This tool will be used to create a freeform selection. The edge of the selected region will follow the mouse cursor as it is dragged around the canvas.  The shape will automatically be closed with a straight line from the current cursor location back to the start point.

### **Making Selections**

The basic use of these tools will be straightforward: click and drag the mouse cursor to create a selection shape. Releasing the mouse button relinquishes editing mode and fixes the selection.

Once a selection will be created, editing operations (Cut/Copy, Move, Add to selection/rest, etc.) will be confined to the active selection.  This can be used to limit drawing to a specific area of the layer.

To edit an area *outside* the current selection it will be necessary to either **add** the new area to the selection or to **deselect** the active selection.

Other features that could be added to the selected area are mentioned below:

* Once created, selections may be moved, resized, and rotated.

* We could **Add (Union) **i.e A new selection can be **added** to any previous selection(s), allowing multiple areas to be selected at once, using different selection tools. For eg: The following type of  selection could be made by drawing a circle selection using the **Ellipse Select tool**(as proposed), followed by the creation of a square selection using the **Rectangle Select tool**(as proposed):

                ![image alt text](image_0.png)

* We could **Subtract** i.e In this mode, any newly defined areas could be **removed** from previously created selection(s).  This mode will allow a selection to be modified or reduced in ways not possible by making a single selection.  Any other selection tool can be used to make subsequent removals.For example, if a circular selection is made with the Ellipse Select tool, Subtract mode allows the center to be easily removed by creating another circle inside it:               ![image alt text](image_1.png) 	

* We could **INVERT** i.e This would act like **Add** mode except that overlapping regions are *removed* from the total selection.This mode will allow the creation of complex selections like this one, made using a combination of the Ellipse Select and Rectangle Select tools:

                                   		![image alt text](image_2.png)

When a selection will be active it will be surrounded by a dashed moving outline to indicate the area (known as the "dancing ants").  If one of the selection tools will be active, a blue highlight will also be applied to the selected area to aid identification.  This highlighting will be removed when another tool is chosen to improve color accuracy.

#### **Phase 1: Designing the approach for creating a selection tool.**

A separate repository under TUX paint umbrella on Github will be hosted as selection-<addon> containing the add-on source files, tests and code files written for Tux paint. 

#### **Phase 2: Working on the defining the add-on operations for the selection tools created and hosting the add-ons on Github**

I will have to show that the implemented add-on selection operation works. For this I'll have to implement standard C  graphic libraries (SDL2) for defining the desired operations for the different selection tools described. 

#### **Phase 3: Working with the selection tools and try to implement extra features **

#### In this period, I will use the implemented add-on system to have the selection package, and try to implement the proposed features to resize, rotate the selected area and implement **UNION, **allowing the selection of multiple areas.  

## **Timeline(Tentative)**

**Community Bonding Period (22 April - 22 May)**

**Goal**: Community Bonding

* The principle focus in this period would be studying in detail, the functionalities of TUX paint, making notes, so as to compare them with that of the add-ons.

* I'll ask guidance from my mentor upon the functioning of the add-on because that is the most crucial part of my project.

* If possible, I would also start coding in this phase only, so that I get a head-start.

**Week 1 - Week 4 (23 May - 19 June)**

**Goal**: Creating the selection tool(s)

* I'll create the general selection tools. 

* The selection tools would be able to select area of different shape and sizes on the canvas.

* All the 3 types of selection tools will be created during this period.

* I’ll also be writing tests along with it.

**Week 5 ( 20 June - 26 June)**

* Ask guidance from the mentor for any other add-on

* Start working on the different operations to be implemented on the selection.

**Mid term Evaluation**

* Having fully functioning add-on selection system with all the selection tool add-ons working properly.

* Fix bugs if any

**Week 6 - Week 7 (27 June - 10 July)**

**Goal**: Defining different operations to be implemented on the selection. 

* Defining cut/copy operation 

* Defining  Add to Selection/Rest operation 

* Ask guidance from the mentor for any add-on operation

* Fix bugs if any.

**Week 8 - Week 11 (11 July - 31 July)**

**Goal**: Writing code to implement other features( rotate, Add(union),Subtract)

* In this period I'll be writing codes to implement extra features like rotate selection and implemented Add and subtract selection, to select multiple areas.

* Finishing the add-on after writing tests

* Fix bugs if any.

**Week 11 - Week 12 (1 August - 14 August)**

**Goal**: Completing the Add-on for final submission.

* Adding the move operation feature to the selection.

* Ask the mentor for guidance to add any other feature.

* Complete the writing and testing of codes for final submissions.

* Fix bugs if any.

**Future Work -** Continue working over the add-on system forever. I'll love to see future implementations on it.

I'll be writing my notes throughout the progress. Later on I'll write document and provide tutorials for the work l would have done. I expect to be in touch with my mentor every 2-3 days to share the progress on the project. I currently have no blog posts of my own, but would like to post on the community blog to let others know about the progress on the project.

I have reviewed the GSoC 2016 Timeline and I am agreeing that I will be fully available without any constraints during the time mentioned there.I would be able to devote 40 - 50 hours a week during the project, since I have no other big project devoted for the summer. My summer vacations start by 20th May and I'll not be engaged in vacations. My academic year would begin by 1st August, but for the first month I would still be able to devote around 40 hours, since there would be no tests/exams.  I have a good internet connection and have no plans to make a trip to anywhere that I might have spotty connection.  

## **Why am I the right person to take this project ?**

I am passionate about open source technologies and i have used other open source technologies for my personal and class projects. I believe in the open source culture of sharing and will like to give back to the Open source community by my participation in this year's GSOC 2016.

### **Notes**

* I have no commitment during summer which means I'm free to work completely on my project.

* I am very enthusiastic about my work being beneficial to other people in the open source community. I'll keep on seeing the work done by me and fixing issues if they emerge in future.

* * *


### **References**

* Some previous work on "Selection" made by Reilly Watson : [https://github.com/reillywatson/tuxpaint-selection](https://github.com/reillywatson/tuxpaint-selection)

* [http://www.tuxpaint.org/](http://www.tuxpaint.org/)

