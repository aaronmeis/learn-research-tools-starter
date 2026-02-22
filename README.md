# learn-research-tools-starter
> **GitHub Description:** Standardized boilerplate and scaffolding for building AI Observability research tools with pre-configured CI/CD and OTel integration.

Standardized template and scaffolding for AI Observability research and tools.

## Purpose
Template architecture for API + worker + DB + UI + observability.

## Infographic Prompt
> **Prompt:** Generate a professional infographic for 'Research Tools Starter', a standardized template for AI Observability repositories. Visualize the repository structure: API + Worker + DB + UI. Show the CI/CD pipeline: lint -> test -> build -> scan -> publish. Highlight the one-click deployment to a dev environment.

## MVP Scope
- **Must-have:** Standardized folder structure, CI/CD pipeline config (GitHub Actions), Docker base images.
- **Nice-to-have:** Pre-integrated LiteLLM, monitoring sidecars (Prometheus/Grafana).

## Quickstart
```bash
./scripts/init-repo.sh my-new-tool
cd my-new-tool && docker compose up -d
```
