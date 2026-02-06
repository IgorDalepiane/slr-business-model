# Build IEEE journal article PDF (pdflatex + bibtex for citations)
.PHONY: pdf clean

pdf:
	pdflatex -interaction=nonstopmode main.tex
	bibtex main
	pdflatex -interaction=nonstopmode main.tex
	pdflatex -interaction=nonstopmode main.tex

clean:
	rm -f main.aux main.bbl main.blg main.log main.out main.toc main.run.xml main.fls main.fdb_latexmk main.synctex.gz
