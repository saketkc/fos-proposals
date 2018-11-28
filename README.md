# FOS Proposals
## Express your love for Open Source!

This repository serves as an archive of *F*ree and *O*pen *S*ource proposals.
Since [GSoC](https://developers.google.com/open-source/soc/?csw=1) is the only such 
program where I participated myself, the dump is organized as such.
If you have proposals from GSoC/KDE-Soc/any, feel free to send a PR.


## Proposals

- [GSoC-2012](GSoC-2012)
	- [Accepted](GSoC-2012/Accepted)
		- [Connexions-SaketChoudhary-OERPub-API](GSoC-2012/Accepted/Connexions-SaketChoudhary-OERPub-API/Connexions-SaketChoudhary-OERPub-API.md)
- [GSoC-2013](GSoC-2013)
	- [Accepted](GSoC-2013/Accepted)
		- [Genome-Informatics-SaketChoudhary-eQTL-Pipeline](GSoC-2013/Accepted/Genome-Informatics-SaketChoudhary-eQTL-Pipeline/Genome-Informatics-SaketChoudhary-eQTL-Pipeline.md)
- [GSoC-2014](GSoC-2014)
	- [Accepted](GSoC-2014/Accepted)
		- [Mozilla-ManishG-Servo](GSoC-2014/Accepted/Mozilla-ManishG-Servo/Mozilla-ManishG-Servo.md)
		- [KDE-AnujPahuja-KDE-Games-to-KF5](GSoC-2014/Accepted/KDE-AnujPahuja-KDE-Games-to-KF5/GSoC-KDE.md)
		- [BioJS-SaketChoudhary-HumanGV](GSoC-2014/Accepted/BioJS-SaketChoudhary-HumanGV/BioJS-SaketChoudhary-HumanGV.md)
		- [Sympy-HarshGupta-Solvers](GSoC-2014/Accepted/Sympy-HarshGupta-Solvers/Sympy-HarshGupta-Solvers.md)

- [GSoC-2015](GSoC-2015)
	- [Accepted](GSoC-2015/Accepted)
		- [HimanshuMishra-PSF-Implementing-Add-On-System-For-NetworkX](GSoC-2015/Accepted/HimanshuMishra-PSF-Implementing-Add-On-System-For-NetworkX/GSoC-2015-Application-Himanshu-Mishra-Add-on-System-for-NetworkX.md)
		- [Sumith1896-PSF-Implementing-Polynomial-module-in-CSymPy](GSoC-2015/Accepted/Sumith1896-PSF-Implementing-Polynomial-module-in-CSymPy/GSoC-2015-Application-Sumith-Implementing-polynomial-module-in-CSymPy.md)
		- [Pratyaksh-PSF-Sampling-Algorithms-in-pgmpy](GSoC-2015/Accepted/Pratyaksh-PSF-Sampling-Algorithms-in-pgmpy/Pratyaksh-PSF-Sampling-Algorithms-in-pgmpy.md)
		- [SaketC-statsmodels-MixedModels](GSoC-2015/Accepted/SaketC-statsmodels-MixedModels/SaketC-statsmodels-MixedModels.md)
		- [The-Eclipse-Foundation-AnujPahuja-Cloud-Removal](GSoC-2015/Accepted/The-Eclipse-Foundation-AnujPahuja-Cloud-Removal/GSoC-GeoTrellis.md)
		- [ASF-ODE-Process-Instance-Visualization-For-Monitoring-Console](GSoC-2015/Accepted/kamdjouduplex-ASF-ODE-Process-Instance-Visualization-For-Monitoring-Console/kamdjouduplex-ASF-ODE-Process-Instance-Visualization-For-Monitoring-Console.md)
	- [Proposed](GSoC-2015/Proposed)
		- [Mozilla-ManishG-FormSupportServo](GSoC-2015/Proposed/Mozilla-ManishG-FormSupportServo/Mozilla-ManishG-FormSupportServo.md)
- [GSoC-2016](GSoC-2016)
	- [Accepted](GSoC-2016/Accepted)
		- [PSF-MeetPragneshShah-RISCV-myHDL](GSoC-2016/Accepted/PSF-MeetPragneshShah-RISCV-myHDL/PSF-MeetPragneshShah-RISCV-myhdl.md)
		- [PSF-Kivy-udiboy1209-Tiled-Integration-With-KivEnt](GSoC-2016/Accepted/PSF-Kivy-udiboy1209-Tiled-Integration-With-KivEnt/PSF-Kivy-udiboy1209-Tiled-Integration-With-KivEnt.md)
		- [MovingBlocks-rzats-Visual-NUI-Editor](GSoC-2016/Accepted/MovingBlocks-rzats-Visual-NUI-Editor/MovingBlocks-rzats-Visual-NUI-Editor.md)
		- [Mozilla-KalpeshKrishna-Schedule-TaskCluster-Jobs](GSoC-2016/Accepted/Mozilla-KalpeshKrishna-Schedule-TaskCluster-Jobs/Mozilla-KalpeshKrishna-Schedule-TaskCluster-Jobs.md)
		- [lowRISC-omasanori-Porting-musl-libc-to-RISC-V](GSoC-2016/Accepted/lowRISC-omasanori-Porting-musl-libc-to-RISC-V/lowRISC-omasanori-Porting-musl-libc-to-RISC-V.md)
        - [OBF-VivekRai-Linking_Phenotypes_with_SNP](GSoC-2016/Accepted/OBF-VivekRai-Linking_Phenotypes_with_SNP/OBF-VivekRai-Linking_Phenotypes_with_SNP.md)
- [GSoC-2018](GSoC-2018)
	- [Accepted](GSoC-2018/Accepted)
		- [CCExtractor-ShivamKumarJha-ProjectNephos](GSoC-2018/Accepted/CCExtractor-ShivamKumarJha-ProjectNephos/CCExtractor-ShivamKumarJha-ProjectNephos.md)

`Proposed` is euphemistic.
*Love can often be one-sided.*

## Adding your proposal?

Opening a pull request with links to a Google Doc should suffice.
In case you want to help more, read on.


All proposals need to be in Github flavored markdown format.
If you have a Google Doc, conversion should be pretty straightforward
using [pandoc](http://johnmacfarlane.net/pandoc/README.html)



```
git clone git@github.com:username/fos-proposals.git
git checkout -b username-year
cd GSoC-year
mkdir Organisation-YourName-Title
cd Organisation-yourname-title && mkdir media
```

All images should go to `media`, and be relatively linked in your markdown.
To port a `doc/docx` proposal:

```
cd Organisation-YourName-Title
pandoc -r  docx infile.docx -w markdown_github -o Organisation-YourName-Title.md --extract-media=media
rm infile.docx
git add .
git commit -am “GSoC-Year: Proposal Title”
git push origin username-year
```

Alternatively, you can use [gdocs2md](https://github.com/mangini/gdocs2md)
which in my experience so far gives superior output to `pandoc`.
Suggestions are always welcome.


# Similar Projects

- [SDSLabs GSoC](https://blog.sdslabs.co/gsoc/)
- [GSoC-2017-Accepted-Proposals](https://github.com/saurabhshri/GSoC-2017-Accepted-Proposals)

# FAQs

- [GSoC-FAQs](https://github.com/OrkoHunter/gsoc-FAQs)
