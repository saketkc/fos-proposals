> **Sub Org Info**
>
> [***coala***](http://coala-analyzer.org/)
>
> **Student Info**
>
> **Name:** Karan Sharma
>
> **Alternate names:** mr-karan
>
> **Email:** karansharma1295@gmail.com **Telephone:** +91 9650 31 8721
>
> **GSoC Blog RSS Feed URL:** http://gsoc2016mr-karan.blogspot.com/feeds/posts/default **Timezone:** IST (UTC +5:30)
>
> **CV:** [*Link to CV*](https://www.dropbox.com/s/pbwvpvcmxbyvy1l/KaranSharma-CV.pdf?dl=0) **Github:** [*mr-karan*](https://github.com/mr-karan)
>
> **Code Sample**

-   [*coala*](https://github.com/coala-analyzer/coala/commits/master?author=mr-karan)

-   [*coala-bears*](https://github.com/coala-analyzer/coala-bears/commits/master?author=mr-karan)

> Prominent PR's from the above:

1.  [*SCSSLinterBear*](https://github.com/coala-analyzer/coala-bears/pull/142)

2.  [*BootLintBear*](https://github.com/coala-analyzer/coala-bears/pull/152)

3.  [*formatRLintBear*](https://github.com/coala-analyzer/coala-bears/pull/179)

4.  [*RuboCopBear*](https://github.com/coala-analyzer/coala-bears/pull/205)

5.  [*AutoPrefixBear*](https://github.com/coala-analyzer/coala-bears/pull/281)

6.  [*GoTypeBear*](https://github.com/coala-analyzer/coala-bears/pull/276)

> **Project Title: Extend linter integration**
>
> **Proposal Abstract**
>
> The aim of the project is to ease the process of creating a new Lint Bear, address the issue of linting files having embedded source code and provide command line interface improvements to existing coala application.
>
> **Possible Mentors : @sils1297, @AbdealiJK, @Makman2**
>
> **Languages used : Python**

**The Problem and Motivation**

> **(A) coala-bears --create command**
>
> The current process of creating a new bear is quite repetitive and mundane. Each bear which has been added to coala has to go through these 2 steps:

-   Manually add dependencies to package.json/requirements.txt/Gemfile if it’s based on either Node/ Python/ Ruby.

-   Create files in directories Bears and Tests.

> This motivates me strongly to integrate this command with coala and make the process of creating a new bear easier.I've also filed an issue regarding the same [*here*](https://github.com/coala-analyzer/coala-bears/issues/154).
>
> **(B) Multi Syntax Lint Bear**
>
> Another current problem which is presented in [*issue \#1690 *](https://github.com/coala-analyzer/coala/issues/1690)is, handling source code files having embedded syntax. Elaborating more on it, currently the user has to run language specific linters for files which can be quite a cumbersome process if the directory has files of different programming language syntaxes. Another problem is that the linters don’t check for the extension of the file they are linting. Case in point, the following screenshot shows Bootstrap and Ruby Lint Bears linting a python file.

<img src="media/media/image1.jpeg" width="680" height="320" />

> **(C) Navigation of errors**
>
> Another feature that can be implemented in the ConsoleInteraction is the ability to navigate the errors/warnings shown by the bear to the user. Currently if the user chooses to go over the next warning, he/she cannot come back to the previous error. While the error/warning is still displayed on the screen but if the lint has an option for auto correct and the user mistakenly chose to go over the next error then he/she has to run the bear again to correct that line.
>
> **(D) Multiline regex support**

Currently there’s a workaround for the linter executable which outputs multiline message, i.e. by

using regex hacks. A new Lint class variable should be introduced to provide a cleaner solution.

**(E) Improving the UI of coala**

Since coala is a CLI application, I have looked at various modules and found [*python prompt toolkit*](http://python-prompt-toolkit.readthedocs.org/) to be a versatile library which can help in improving command line interface.

**(F) A Web application for listing out all Bears (optional)**

An optional feature (if time permits) that i would like to add in my proposal is the creation of a small web application which will host details of all the bears developed till now. This project will complement the Decentralizing Bear project. Since every bear is going to be split into it’s own python package and Github repositories, I think having a central place for details about all Bears developed till now with their help guides/documentation will be a good idea. Inspiration of this project is from [*Atom linter list *](http://atomlinter.github.io/)website and [*postcss*](http://postcss.parts/).

**Implementation**

**Phase 1: Designing the approach for coala-bears --create command**

A separate repository will be created for coala-bears --create executable. The user will be greeted with a small set of questionnaire in the CLI which will initiate the bears and tests folders and also add external linter executable dependencies. An example template and a questionnaire will be created in JSON file.

<img src="media/media/image2.jpeg" width="680" height="265" />

The approach of this command will be to work like how git --interactive works or [*pelican*](http://docs.getpelican.com/en/3.6.3/install.html#kickstart-your-site) [*-quickstart* ](http://docs.getpelican.com/en/3.6.3/install.html#kickstart-your-site)works. The questionnaire will have the following design:

<img src="media/media/image3.jpeg" width="680" height="147" />

Generated files from this command will have basic syntax which is required for bear to run:

ExampleLintBear.py

<img src="media/media/image4.jpeg" width="680" height="393" />

> import re
>
> from coalib.bearlib.abstractions.Lint import Lint from coalib.bears.LocalBear import LocalBear
>
> from coalib.results.RESULT\_SEVERITY import RESULT\_SEVERITY
>
> class ExampleBear(LocalBear, Lint): executable = 'user\_input\_binary' output\_regex = re.compile(r'') severity\_map = {
>
> "": RESULT\_SEVERITY.NORMAL,
>
> "": RESULT\_SEVERITY.MAJOR,
>
> "": RESULT\_SEVERITY.INFO
>
> }
>
> def run(self, filename, file):
>
> '''
>
> Checks the code with \`\`user\_input\_binary\`\` on each file separately.
>
> '''
>
> return self.lint(filename)

ExampleLintBearTest.py

<img src="media/media/image5.jpeg" width="680" height="237" />

> from bears.examplebeardir.ExampleLintBear import ExampleLintBear from tests.LocalBearTestHelper import verify\_local\_bear
>
> good\_file = """
>
> """.splitlines(keepends=True)
>
> bad\_file = """
>
> """.splitlines(keepends=True)
>
> ExampleLintBearTest = verify\_local\_bear(ExampleLintBear, valid\_files=(good\_file,), invalid\_files=(bad\_file,))

Progress on this work during Application period can be seen at: *https://github.com/coala-analyzer/coala-bears/issues/154\#issuecomment-192676559*

> **Phase 2: Working with Lint Class**
>
> In this phase, I will be working on adding a few Lint class methods and variables. I’ll start by working on implementing a Multi Syntax Lint Bear and will be adding can\_lint() method which will assert whether the bear is meant to lint that syntax or not. If can\_lint() returns True, program execution will follow normal routine but if it returns False then it will find the list of Bears which can lint that syntax. If the source code has embedded source code in it (like HTML files may have
>
> .php, .css syntax in it as well) a new Lint class variable syntax is introduced for this purpose. The language syntax will be mapped to the portion of code which is separate from original syntax which can be extracted using Regex. An example of this is linting a HTML file which has JS and CSS code embedded in it.

<img src="media/media/image6.jpeg" width="680" height="116" />

> embedded\_syntax = (‘css’,'js’) embedded\_syntax\_regex = {‘css’:
>
> \#regex for detecting css code in &lt;style&gt;&lt;/style&gt; tags in html; ‘Js’: \# regex for detecting js code in &lt;script&gt;&lt;/script&gt; tags
>
> }
>
> So, the code extracted from these variables will be linted using appropriate bears. The user can define which bear to run in .coafile or we can display all the bears present for that syntax to the user and the user can choose during run time.
>
> Also, a new multiline Lint class variable will be introduced which will use re.finditer module to iterate over regex output for lint executables using multiline output messages. For navigation of results, two methods get\_next() and get\_previous() will be implemented in ConsoleInteraction class to navigate the results shown to the user.
>
> **Phase 3: Working on improving the command line interface**
>
> For improving the current command line interface, I will be implementing the following features from Python Prompt Toolkit Library:

1.  [*Pygment syntax highligitng*](http://python-prompt-toolkit.readthedocs.org/en/latest/pages/building_prompts.html#syntax-highlighting)

2.  [*Autocompletion*](http://python-prompt-toolkit.readthedocs.org/en/latest/pages/building_prompts.html#autocompletion)

3.  [*Status Bar*](http://python-prompt-toolkit.readthedocs.org/en/latest/pages/building_prompts.html#adding-a-bottom-toolbar)

> For syntax-highlighting, I've filed an issue at [*coala*](https://github.com/coala-analyzer/coala/issues/1925)
>
> **Phase 4: Web application for listing out all Bears (Optional)**
>
> I will begin my work by creating a small web application in Flask. I will write a small program which will parse the list of bears like coala -A command does and will plug in them to the website. If the bears have a small documentation written in Markdown files, I will add them to the details page of each bear. A script can also be written which will write the details of each bear to a JSON file. The fields of JSON can be This will make the task of creating a web application very easy process by just plugging in the values to the template.
>
> <img src="media/media/image7.jpeg" width="680" height="151" />
>
> name:” ”,
>
> Asciinema:” ” \# asciinema url of working of bear, Short-description: “ ”,
>
> Long-description:” ”:
>
> Author Twitter/Github handle:” ”,
>
> }
>
> The front end of website can be done in any lightweight framework like Polymer.
>
> **Timeline(Tentative)**
>
> **Community Bonding Period (22 April - 22 May)**
>
> **Goal**: Community Bonding

-   The principal focus in this period will be studying in depth about coala, diving deep in the codebase, the functionalities of coala, making notes as I go along.

-   I'll ask guidance from my mentor upon the functioning of the Multi Syntax Bear because that is the most crucial part of my project.

-   If possible, I plan to start coding in this period only, so that I get a head-start.

> **Week 1 (23 May - 30 May)**
>
> **Goal**: Creating the coala-bears --create helper functions

-   I’ll start with making a questionnaire in JSON format.

-   I’ll write helper functions for generating files based on user input.

-   I’ll write helper function for appending linter executable in external dependency files.

> **Week 2 (30 May - 6 June)**
>
> **Goal**: Completing coala-bears command

-   I’ll integrate the helper functions in coala-bears module.

-   I’ll write test cases for coala-bears --create command covering boundary conditions and handling unexpected user behavior.

-   By the end of Week 2, coala-bears --create will be completed.

> **Week 3 (6 June - 13 June)**
>
> **Goal**: Implementing multi syntax Lint bear

-   I'll start first with implementing can\_lint method in Lint class. I'll take code base of [*Sublime Linter*](http://www.sublimelinter.com/en/latest/linter_methods.html#can-lint-syntax) [*Plugin* ](http://www.sublimelinter.com/en/latest/linter_methods.html#can-lint-syntax)as my starting point.

-   I’ll be working on linting the bear to work on only the files it’s supposed to lint using can\_lint() method and displaying appropriate error/ other Lint Bear choices to the user.

> **Week 4 (13 June-20 June)**
>
> **Goal**: Implementing embedded source code checking

-   I’ll be working on handling the Lint method for embedded source code.

-   I’ll be writing test cases for handling embedded source code.

> **Week 5 (20 June - 27 June)**
>
> **Goal**: **Mid term Evaluation**

-   Have a fully functional coala-bears --create command and implemented Multi Syntax Lint Bear.

-   Take feedback from mentors and improve upon it.

-   Fix bugs if found any/reported.

> **Week 6 - 7 (27 June - 11 July)**
>
> **Goal**: Working on multiline regex and navigation of results

-   I will be working on multiline regex support.

-   I will be working on Navigation of Results.

-   I will be writing test cases for get\_next and get\_previous and will test multiline with Linter such as [*write-good* ](https://github.com/btford/write-good)which outputs multiline message.

> **Week 8 - Week 9 (11 July - 25 July)**
>
> **Goal**: Modifying interface of coala CLI application

-   I will be working on [*Issue \#1925*](https://github.com/coala-analyzer/coala/issues/1925).

-   I will be adding the rest of features mentioned above from Python Prompt Toolkit Library to coala CLI.

> **Week 10 (25 July - 1st August)**
>
> **Goal**: Buffer Week

-   In this period I'll pause the current development of my project and will be be doing bug fixing, working on mentor’s feedback and finish incomplete tasks if the above mentioned schedule didn’t work out due to unforeseen circumstances.

> **Week 11 - Week 12 (1st August - 15 August)**
>
> **Goal**: Working with web application.

-   Create a web application using Flask which will have a list of all bears present with a searchable catalog.

-   I will be hosting this web application on coala-html repository.

> **Week 13 (15 August - 23 August))**
>
> **Goal**: Buffer Week; Finishing all pending tasks

-   I will be documenting all the changes.

-   I will be tidying up the code and refactoring if deemed necessary.

-   I will do additional testing and bug fixing of all the changes done till now.

> **Future Work**:

-   I would love to maintain coala-bears --create command for further improvements and also the coala bears website.

-   I will be writing blog posts regularly about working on coala project and will share whatever I learn from this project in my blog.

-   I will be encouraging new comers on helping how to create a new Lint Bear.

> **Other Commitments**

-   Do you have any other commitments during the main GSoC time period, May 23rd to August 23rd? <sup>❍</sup> None, I’ll be having my summer break in this period.

-   Do you have exams or classes that overlap with this period?

> <sup>❍</sup> I don’t have any exams though my college will start from August 1 but since it will be a new semester there won’t be any work load or exams coming up till August 23.

-   Do you plan to have any other jobs or internships during this period? <sup>❍</sup> No I’ll be working full time for GSoC project.

-   Do you have any other short term commitments during this period? <sup>❍</sup> None

-   Have you applied with any other organizations? If so, do you have a preferred project/org? (This will help us in the event that more than one organization decides they wish to accept your proposal.)

> <sup>❍</sup> No. coala is my first and only preference.
>
> **extra information**

-   Will you be able to join us for a conference such as EuroPython or GUADEC and present your work if at least partial sponsorship will be provided? (See https://github.com/coala-analyzer/coala/wiki/Conferences-Upcoming)

> <sup>❍</sup> Yes, in fact I have registered for EuroPython already and wish to give a poster presentation over there. I have also applied for giving a workshop at PyCon India. [*Here's *](https://in.pycon.org/cfp/2016/proposals/creating-lint-bears-with-coala/)my proposal for the same.

-   We love having twitter handles so we can tell people publicly about your great project and successes at https://twitter.com/coala\_analyzer! (Not required but recommended.

> <sup>❍</sup> A) [*karansharma1295*](https://twitter.com/karansharma1295)
