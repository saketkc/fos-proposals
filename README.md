# FOS Proposals
## Express your love for Open Source!

This repository serves as an archive of *F*ree and *O*pen *S*ource proposals.
Since [GSoC](https://developers.google.com/open-source/soc/?csw=1) is the only such 
program where I participated myself, the dump is organized as such.
If you have proposals from GSoC/KDE-Soc/any, feel free to send a PR.


## Adding your proposal?

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

Alternatively, you can leverage on [gdocs2md](https://github.com/mangini/gdocs2md)
which in my experience so far gives superior output to `pandoc`.
Suggestions are always welcome.


## Organisation

```
fos-proposals/
├── GSoC-Year
│   └── Accepted
        └──Organisation-YourName-Title
            └──Organisation-YourName-Title.md
            └──media
                └──image_01.png
    └── Proposed
        └──Organisation-YourName-Title
            └──Organisation-YourName-Title.md
            └──media
                └──image_01.png
```

_`Proposed` is euphemistic. 
Love can often one-direction$al. _



