#This program makes nametags given list in csv of "Full Name, Country".
#It will produce a .tex file, which can be converted to pdf using pdflatex.
#Usage: 
#python nameTagMaker.py nameList.csv out.tex; pdflatex out.tex
#
#To edit style symply edit variable texHeader 

from string import Template
import copy
import sys

texHeader=r"""\documentclass[a4paper,12pt]{article}%{minimal}
%\setlength\arraycolsep{5pt}
%\setlength\tabcolsep{6pt}
\setlength\arrayrulewidth{0.1mm}
%\usepackage{multirow}
\usepackage[a4paper,total={181mm,270mm},left=15mm, top=15mm]{geometry}
\usepackage{array}
\pagestyle{empty}
\usepackage[document]{ragged2e}
\usepackage{graphicx}
%\DeclareGraphicsExtensions{.png}
\usepackage{tabularx}
\graphicspath{ {graphics/} }
\usepackage[most]{tcolorbox}
\usepackage{setspace}

\newcommand{\makeRowThree}[2]{
            \makeCellOne{#1}
            & 
            \makeCellOne{#2} \\ %[49mm]
}

\newcommand{\makeCellOne}[1]{
    \begin{minipage}[t][50mm]{8.5cm}
        \begin{flushright}
        %\hspace*{3cm}\\
        \includegraphics[width=3cm, trim=0 -0.4cm 0 -0.5]{logoForNametags}
        \end{flushright}
        {#1}
    \end{minipage}
}

\newcommand{\makeNames}[2]{
    \begin{center}
        \begin{minipage}[t][21mm]{8.5cm}
            \begin{center}
                \begin{spacing}{1.4} 
                    \textsc{\LARGE{\textbf{#1}}}
                \end{spacing}
            \end{center}
        \end{minipage}\\
        #2
    \end{center}
}

\newcommand{\makeOnePage}[1]{
\begin{minipage}{17cm}
\begin{tabular}{ | p{8.5cm} | p{8.5cm} | }
#1
\end{tabular}
\end{minipage}
\newpage
}

\begin{document}"""

texFooter="\n\\end{document}"

row=Template("""\hline\makeRowThree{
\makeNames{$LName}{$LCountry}
}{
\makeNames{$RName}{$RCountry}
}""")

makeDataRow=lambda pd, i: {"LName":pd[i][0][0], "LCountry":pd[i][0][1], "RName":pd[i][1][0], "RCountry":pd[i][1][1]}
makeDataRows=lambda pd:[makeDataRow(pd,i) for i in range(5)]
makePageTex=lambda pd: "\\makeOnePage{\n"+''.join(row.substitute(x) for (x) in makeDataRows(pd))+"\\hline}"
preprocPageDataList=lambda datalist: [[datalist[::2][i],datalist[1::2][i]] for i in range(len(datalist)//2)]

pageData=[['a','b'],['c','d'],['e','f'],['g','h'],['i','j'],['k','l'],['m','n'],['o','p'],['q','r'],['s','t']]
dt=[[pageData[::2][i],pageData[1::2][i]] for i in range(5)]

import csv
#with open('nameList.csv') as inCSV: #DEBUG
with open(sys.argv[1]) as inCSV:
    dataAll=list(csv.reader(inCSV))

dt=dataAll+[['','']]*(10%(len(dataAll)%10))
dataPages=[dt[i*10:(i+1)*10] for i in range(len(dt)//10)]

#with open('output.tex','w') as out: #DEBUG
with open(sys.argv[2],'w') as out:
    out.write(texHeader)
    out.write('\n\n'.join([makePageTex(preprocPageDataList(dataPage)) for dataPage in dataPages]))
    out.write(texFooter)
