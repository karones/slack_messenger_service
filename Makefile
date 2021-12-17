NAME := название сервиса
VERSION := $(shell git tag -l | sort -V | tail -n 1)
MAJOR := $(shell cut -d '.' -f1 <<< $(VERSION))
MINOR := $(shell cut -d '.' -f2 <<< $(VERSION))
PATCH := $(shell cut -d '.' -f3 <<< $(VERSION))
$(shell git config --global credential.helper 'cache --timeout=600')

.PHONY: change-version tag

version:
	@echo "VERSION: $(VERSION)"

change-version:
ifeq ($(release), major)
	$(eval VERSION := $(shell expr $(MAJOR) + 1).0.0)
else ifeq ($(release), minor)
	$(eval VERSION := $(MAJOR).$(shell expr $(MINOR) + 1).0)
else ifeq ($(release), patch)
	$(eval VERSION := $(MAJOR).$(MINOR).$(shell expr $(PATCH) + 1))
else
	@echo "Error change version"
endif

tag: change-version
	@echo "New version: $(VERSION)"
	@git tag $(VERSION)
	@git push --tags

restart:
	docker-compose down && docker-compose up --build -d
