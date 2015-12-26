## texify.sh to simplify running LaTex
## author: Ulrike Hager

#!/bin/bash
fname=$1
f2name=${fname%tex}"ps"
f3name=${fname%tex}"pdf"
bib=0
pdf=0
lsc=0
ini=$(pwd)"/"
fol="./"

check_file(){
find . $fname -maxdepth 0
if test $? -ne 0
then
exit
fi
}
run_latex(){
latex -halt-on-error $fname
if test $? -ne 0
then
exit 
fi
}
run_bibtex(){
bibtex ${fname/.tex/}
if test $? -ne 0
then
exit 
fi
}
OPTIND=2
while getopts bpf: opt;
do
    case "$opt" in
    b) bib=1;;
    p) pdf=1;;
    f) fol=$OPTARG;;    
    [?]) echo "options are: b for bibtex, p for pdf, l for landscape"
    exit 1
    ;;
    esac
done
cd $fol
run_latex
if [ $bib -eq 1 ]
then 
    run_bibtex 
    run_latex
fi
run_latex
 dvips ${fname/.tex/} -R0 -Ppdf -o $f2name
if [ $pdf -eq 1 ]
then
#  ps2pdf -dPDFSETTINGS=/prepress $f2name 
  ps2pdf $f2name 
  atril $f3name  &
 else
  atril $f2name  &
fi
cd $ini
