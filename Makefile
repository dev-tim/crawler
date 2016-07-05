PROJECT_ROOT:=.

PIP_REQUIREMENTS_DIR=$(PROJECT_ROOT)/requirements
PIP_REQUIREMENTS_BASE:=$(PIP_REQUIREMENTS_DIR)/base.txt
PIP_REQUIREMENTS_DEV:=$(PIP_REQUIREMENTS_DIR)/dev.txt
PIP_REQUIREMENTS_TRAVIS:=$(PIP_REQUIREMENTS_DIR)/travis.txt
PIP_REQUIREMENTS_PRODUCTION:=$(PIP_REQUIREMENTS_DIR)/prod.txt
PIP_REQUIREMENTS_ALL:=$(PIP_REQUIREMENTS_BASE) $(PIP_REQUIREMENTS_DEV) $(PIP_REQUIREMENTS_TRAVIS) $(PIP_REQUIREMENTS_PRODUCTION)

requirements: $(PIP_REQUIREMENTS_ALL)
requirements_rebuild:
	$(RM) $(PIP_REQUIREMENTS_ALL)
	$(MAKE) requirements PIP_COMPILE_ARGS=--rebuild

$(PIP_REQUIREMENTS_DIR)/%.txt: PIP_COMPILE_ARGS?=
$(PIP_REQUIREMENTS_DIR)/%.txt: $(PIP_REQUIREMENTS_DIR)/%.in
	pip-compile --no-header $(PIP_COMPILE_ARGS) --output-file "$@.tmp" "$<" >/tmp/pip-compile.out.tmp || { \
	  ret=$$?; echo "pip-compile failed:" >&2; cat /tmp/pip-compile.out.tmp >&2; \
	  $(RM) "$@.tmp" /tmp/pip-compile.out.tmp; \
	  exit $$ret; }
	@sed -n '1,10 s/# Depends on/-r/; s/\.in/.txt/p' "$<" > "$@"
	@cat "$@.tmp" >> "$@"
	@$(RM) "$@.tmp" /tmp/pip-compile.out.tmp

.PHONY: requirements requirements_rebuild

check_pylama:
	pylama crawler

PYTEST_ARGS?=
PYTEST=py.test $(PYTEST_ARGS)
test:
	$(PYTEST) crawler

sys_requirements:
	for pk in $$(cat system-requirements.txt); do sudo apt-get install -yq "$$pk"; done
