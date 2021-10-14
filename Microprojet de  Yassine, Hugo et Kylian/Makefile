FICHIERS_UI    = $(shell ls *.ui)
FICHIERS_RC    = $(shell ls *.rc)
FICHIERS_UI_PY = $(patsubst %.ui, ui_%.py, $(FICHIERS_UI))
FICHIERS_RC_PY = $(patsubst %.rc, rc_%.py, $(FICHIERS_RC))

all: $(FICHIERS_UI_PY) $(FICHIERS_RC_PY)

clean:
	rm -f $(FICHIERS_UI_PY) $(FICHIERS_RC_PY) *~
	rm -rf __pycache__

archive: clean
	zip ../microprojet.zip *

ui_%.py: %.ui
	pyuic5 $< -o $@

rc_%.py: %.rc
	pyrcc5 $< -o $@

.PHONY: all clean archive

