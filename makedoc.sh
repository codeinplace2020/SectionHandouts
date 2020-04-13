#!/bin/bash
# Make HTML and PDF documentation in each language and save the build output.
# This script is pretty janky - after using it, it's a good idea to inspect
# the output manually for sanity.

readonly HTML_FOLDER="handouts-html"
readonly PDF_FOLDER="handouts-pdf"
readonly BUILD_FOLDER="_build"

# Make sure we're working from a clean build folder, since many tools (LaTeX
# in particular) leave crumbs behind.
make clean

# Make handouts in English.
make html
mkdir -p "${HTML_FOLDER}/en/"
cp -r "${BUILD_FOLDER}/html/_static" "${HTML_FOLDER}/en/"

make latexpdf
mkdir -p "${PDF_FOLDER}/en/"
find "${BUILD_FOLDER}/latex" -iname "*.pdf" -exec cp {} "${PDF_FOLDER}/en/" \;

make clean

# Make handouts in other languages.
for LANGUAGE in locale/*; do
	LC="${LANGUAGE##*/}"  # Get just the basename.

	# Make HTML documentation.
	make -e SPHINXOPTS="-D language='${LC}'" html
	mkdir -p "${HTML_FOLDER}/${LC}/"
	cp -r "${BUILD_FOLDER}/html" "${HTML_FOLDER}/${LC}/"

	# Make PDF documentation.
	make -e SPHINXOPTS="-D language='${LC}'" latexpdf
	mkdir -p "${PDF_FOLDER}/${LC}/"
	find "${BUILD_FOLDER}/latex" -iname "*.pdf" -exec cp {} "${PDF_FOLDER}/${LC}/" \;

	make clean
done