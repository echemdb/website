SOURCE_DIR=../literature

SOURCE_METADATA=$(wildcard $(SOURCE_DIR)/**/*.yaml)
SOURCE_SVG=$(patsubst %.yaml,%.svg,$(SOURCES_METADATA))

TARGET_DIR=generated/digitized

TARGET_CSV=$(patsubst %.yaml,%.csv,$(patsubst ${SOURCE_DIR}/%,${TARGET_DIR}/%,$(wildcard $(SOURCE_DIR)/**/*.yaml)))
TARGET_JSON=$(patsubst %.yaml,%.json,$(patsubst ${SOURCE_DIR}/%,${TARGET_DIR}/%,$(wildcard $(SOURCE_DIR)/**/*.yaml)))
TARGET_BIB=$(patsubst ${SOURCE_DIR}/%,${TARGET_DIR}/%,$(wildcard $(SOURCE_DIR)/**/*.bib))

${TARGET_DIR}/%.csv ${TARGET_DIR)}/%.json : $(SOURCE_DIR)/%.yaml $(SOURCE_DIR)/%.svg
	svgdigitizer cv --sampling-interval .001 --package --metadata $< $(patsubst %.yaml,%.svg,$<) --outdir=$(@D)

${TARGET_DIR}/%.bib: $(SOURCE_DIR)/%.bib
	@mkdir -p $(@D)
	cp $< $@

all: $(TARGET_CSV) $(TARGET_JSON) $(TARGET_BIB)

clean:
	rm -rf data/generated

.PHONY: all clean
