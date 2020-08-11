# Container's default name (bwell_challenge)
NAME=bwell_challenge
# Docker image default name (glmeece/bwell_challenge)
IMAGE=glmeece/$(NAME)
# Base directory
BASE=/opt/bwell
# Mount localfile system
LOCAL_OPTS=-v $(shell pwd):$(BASE)

# Start container
.PHONY: start
start:
	@echo "--> Starting $(NAME)"
	docker start $(NAME)

# Stop container
.PHONY: stop
stop:
	@echo "--> Stopping $(NAME)"
	docker kill $(NAME) || true

# Remove container
.PHONY: rm
rm:
	@echo "--> Removing container $(NAME)"
	docker rm $(NAME) || true

# Build image
.PHONY: build
build:
	@echo "--> Building $(NAME)"
	docker build -t $(IMAGE) .

# Run container and provide a Shell terminal for debugging
.PHONY: local
local:
	@echo "--> Starting $(NAME)"
	docker run $(LOCAL_OPTS) --name $(NAME) -it $(IMAGE) /bin/bash

# Local development
.PHONY: dev
dev: stop rm build local

# Runs tests
.PHONY: run
run:
	@echo "--> Running tests..."
	pytest

# Verify Chrome & Chromedriver are installed correctly and Selenium works
.PHONY: seltest
seltest:
	@echo "--> Testing Selenium, Chromedriver, and Chrome"
	./check_chromedriver.py

# Tail container logs
.PHONY: logs
logs:
	docker logs -f $(NAME)
