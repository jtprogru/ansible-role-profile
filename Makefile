.DEFAULT_GOAL := help

# All tooling lives in a local .venv managed by uv; the system Ansible is
# never touched. Override the test distro with: make test MOLECULE_DISTRO=debian13
MOLECULE_DISTRO ?= ubuntu2604
export MOLECULE_DISTRO

UV_RUN := uv run

.PHONY: help
help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) \
		| awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-12s\033[0m %s\n", $$1, $$2}'

.PHONY: setup
setup: ## Create .venv and install the toolchain + collections
	uv venv
	uv pip install -r requirements.txt
	$(UV_RUN) ansible-galaxy collection install -r requirements.yml

.PHONY: lint
lint: ## Run yamllint and ansible-lint
	$(UV_RUN) yamllint .
	$(UV_RUN) ansible-lint

.PHONY: test
test: ## Full molecule cycle (create -> converge -> idempotence -> verify -> destroy)
	$(UV_RUN) molecule test

.PHONY: test-all
test-all: ## Run molecule test across all supported distros
	@for distro in ubuntu2604 debian13 rockylinux9; do \
		echo "==> molecule test on $$distro"; \
		MOLECULE_DISTRO=$$distro $(UV_RUN) molecule test || exit 1; \
	done

.PHONY: converge
converge: ## Create the instance and apply the role
	$(UV_RUN) molecule converge

.PHONY: verify
verify: ## Run the testinfra verification suite
	$(UV_RUN) molecule verify

.PHONY: login
login: ## Open a shell in the test instance
	$(UV_RUN) molecule login

.PHONY: destroy
destroy: ## Tear down the test instance
	$(UV_RUN) molecule destroy
