## pdftexify.sh to simplify running pdflatex
## author: Ulrike Hager

#!/bin/bash
fname=$1
pdfname=${fname%tex}"pdf"
bib=0
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
pdflatex -halt-on-error $fname
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
while getopts bf: opt;
do
    case "$opt" in
    b) bib=1;;
    f) fol=$OPTARG;;    
    [?]) echo "options are: b for bibtex, f for folder"
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
xdg-open $pdfname  &
cd $ini
