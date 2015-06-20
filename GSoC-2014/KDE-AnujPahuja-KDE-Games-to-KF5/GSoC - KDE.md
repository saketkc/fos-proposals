**Name: **Anuj Pahuja

**Freenode IRC Nick: **alasin

**﻿IM Service and Username: **﻿GTalk - kamikazeanuj@gmail.com

**Location: **Gurgaon, India (GMT + 0530 hrs)

**﻿Project Title: **Porting KDE Games to KDE Frameworks 5

**Motivation for Proposal:**

As a part of the porting process of KDE apps to newly developed KDE Frameworks 5, I would like to port the KDE Games module to KF5. The main motivation behind the project is to keep KDE Games bit rot-free and maintained with respect to the latest libraries. An initial port of libkdegames to KF5 has been made by Albert Astals Cid but needs to be updated and completed. Also being untested, the library requires some games to be ported to KF5. The project aims at completely porting libkdegames to KF5 followed by a KF5 port of three games from different categories.

**Project Goals:**

**List of Deliverables:**

* KDE Games module (libkdegames) completely ported to KDE Frameworks 5.

* KBounce (Arcade), Naval Battle (Board) and KMines(Logic) ported to KF5/Qt5/Qt Quick 2.

   

**Investigative work:**

* Dropping QPainter API in favour of QSceneGraph API for rendering game graphics resulting in some performance benefits.

**Implementation:**

As a part of porting process to KF5/Qt5, it would be a better approach to first port the games to kde4support and then drop kde4support dependencies in favor of other KF5 methods. As a port of libkdegames has already been made by Albert, porting libkdegames would require much less effort. KBounce, Naval Battle and KMines on the other hand would require porting from scratch. The essential steps can be broadly categorized as follows:

* Removal of Qt3Support.

* Making corresponding changes in the build system.

* Modifying the includes and headers.

* Making core macro changes (‘slots -> Q_SLOTS’ etc.) and other platform specific macros (‘Q_WS_*’ -> Q_OS_*’ etc.)

* Removing wrapped macros for Plugin loading and unit tests.

* Changing method signatures.

* Porting all instances of Qt Quick 1 code to Qt Quick 2/QML2.

* Replacing deprecated methods which have been moved to kde4support by native Qt5 methods.

**Tentative Timeline:**

**22 April - 19 May:  (Community Bonding Period)**

* Familiarize myself with the codebase of KDE games and the common libraries.

* Read through the existing documentation of KDE Frameworks 5 and the important changes that have been made since the previous version.

* Discuss the flow of action and finalize a workplan with the mentor and other developers.

**19 May - 2 June: 2 weeks (Porting libkdegames)**

* Make changes in the build system of libkdegames.

* Remove kdelibs dependency by using Cmake modules from ‘extra-cmake-modules- package’.

* Make changes in UI by replacing deprecated kdelibs methods like KDialog and KAction.

**2 June - 25 July:  ~ 7.5 weeks (Porting KBounce,  Naval Battle and KMines)**

* Remove any Qt3 support dependencies.

* Make core functional changes from KStandardDirs, KComponentData etc. to corresponding Qt5 counterparts QStandardPaths, QCoreApplication etc.

* Replace deprecated KDE 4 methods like KConfig, KSaveFile, KConfig etc. by the corresponding Qt5/KF5 methods like QSaveFile, QCoreApplication etc.

* Make UI changes  by modifying how notifications, fonts, pixel mapping etc. work as per the KF5/Qt5 guidelines. This would include changes in KAction, KDialog, KPixmap, KStyle etc.

* Make IO changes which will involve removing deprecated KIO::Job methods including showErrorDialog() and isInteractive() and porting KFileItem API to QMimeType.

* Change KFile, KParts and ItemViews functions.

* Port QML/Qt Quick 1 to QML/Qt Quick 2 wherever needed.

 

Further breakdown of timeline would be:

* Port Kbounce (Arcade) - 2 June - 20 June (~2.5 weeks )

* Port Naval Battle (Board) - 20 June - 7 July (~2.5 weeks)

* Port KMine (Logic) - 7 July - 25 July (~2.5 weeks)

**25 July - 11 August:  ~2.5 weeks (Investigative period)**

* Replace uses of the QPainter API to the QSceneGraph API wherever possible. This would be done if time persists and things go as per the timeline.

* Port another game to KF5.

**11 August - 18 August: (Pencils Down)**

* Final testing of the ported games.

* Writing the necessary documentation and porting notes for future developers.

* Cleaning up the code and removing bugs (if any).

**Other Commitments:**

I have my semester exams from May 3 - May 17, which falls in the community bonding period during which I might not be able to spend much time reading documentation and source codes. I will spend extra time before my exams to compensate for that. During the coding period, I have no other commitments and will be able to work 40-45 hours per week except for the last week. My college will open from August 2, after which I will be able to spend around 30 hours a week. Having successfully participated in the Season of KDE before, I am confident that I will be able to manage my time efficiently and devote as much time as required to complete the project.

**About me:**

I am a third year undergraduate student pursuing my Bachelors in Computer Science from BITS Pilani. Apart from having lots of interest in computing in general, I have been an open source enthusiast from past 2 years, creating awareness in and around our college about FOSS.

I started using KDE just 6 months after my introduction to Ubuntu and haven’t switched to any other distro after that. The range of applications and the great community support encouraged me to contribute to KDE. Consequently, I participated in Season of KDE 2013 and successfully completed my project on implementing new features in KBounce with the help of my mentor Roney Gomes *. During the project, I also went through the sourcecode of other KDE Games to find similar features which helped me understand the generic layout of the KDE Games module.

Being a big fan of KDE Games and having worked on its codebase, I believe I am well-suited for this project and looking forward to work on it. I would start working on porting other games as and when the project gets over.

﻿

**Link to Patches:**

The changes and patches me and Roney made are in the keyboard-integration branch of Kbounce. Here are the links:

[1]https://projects.kde.org/projects/kde/kdegames/kbounce/repository/show?rev=keyboard-integration

[2]https://projects.kde.org/projects/kde/kdegames/kbounce/repository/revisions/keyboard-integration/revisions

