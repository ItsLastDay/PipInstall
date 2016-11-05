BUILD_DIR = work.dir
OPTIONS = -shell-escape -file-line-error \
		-halt-on-error -output-directory $(BUILD_DIR)
SRC = report.tex
TARGET = $(SRC:.tex=.pdf)

Makefile: ;

.DEFAULT_GOAL := $(TARGET)

all: view

$(TARGET): $(SRC)
	mkdir -p $(BUILD_DIR)
	pdflatex $(OPTIONS) $^
	pdflatex $(OPTIONS) $^
	@mv -v $(BUILD_DIR)/$@ .

.PHONY: clean
clean:
	rm -rf $(BUILD_DIR) $(wildcard *converted-to-pdf.pdf)
	rm -f $(TARGET)

.PHONY: view
view: $(TARGET)
	zathura $(TARGET)
