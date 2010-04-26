all:
	./bin/build . ./_build

css:
	pygmentize -S trac -f html > ./bin/static/hilite.css

styles:
	python -c 'from pygments.styles import get_all_styles; print "\n".join(get_all_styles())'
