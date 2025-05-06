# AWS AI Agent Delivery System
You can refer to https://github.com/lihuiniu/ai-agent-delivery-system for Azure based project. Current project will leverage the AWS technology.

This project provides a scalable system to deliver AI agents within an existing application using AWS infrastructure and OpenAI APIs. It includes:

- **Chat API** with streamed LLM responses
- **Agent configuration service** to control prompts, tools, and base models
- **Authentication and secure action handling**
- **Evaluation framework** (online and offline) for prompt/code changes
- **Infrastructure-as-code with Terraform and Helm**
- **CI/CD via GitHub Actions and Azure DevOps (stubbed)**

## Components

### App (FastAPI)
- `/api/v1/chat.py`: Chat endpoint with streamed response
- `/services/`: Agent config & OpenAI interface logic
- `/models/`: Pydantic schemas and user model
- `/core/`: Security (JWT-based) and config

### Helm Chart
- `deployment.yaml`: App deployment manifest
- `hpa.yaml`: Horizontal Pod Autoscaler
- `service.yaml`: LoadBalancer service
- `values.yaml`: Configurable Helm values

### Terraform
- `eks.tf`: EKS Cluster setup
- `rds.tf`: PostgreSQL database (optional)
- `redis.tf`: ElastiCache Redis 8.0
- `outputs.tf`: Outputs for integration
- `main.tf`, `variables.tf`: Root config and variables

### GitHub Actions
- `.github/workflows/ci.yml`: Docker build and push, Helm upgrade

## Usage

```bash
# Deploy infrastructure
cd terraform
terraform init && terraform apply

# Build and deploy app
cd ..
docker build -t agent-api .
helm upgrade --install agent-api ./helm -f helm/values.yaml
```

## Authentication
JWT-based auth with bearer tokens and role-based access.

## OpenAI Features
- ChatCompletion API with streamed responses
- Prompt templates and dynamic tool use
- Model configuration via agent profiles

## Deployment Lifecycle
1. Agent config PR triggers eval workflows
2. Canary or dev deployment via GitHub Actions
3. Metrics observed before rolling to prod
4. Rollback supported via Helm/infra versions

## Evaluation Framework
- Offline: Evaluate prompt accuracy on test queries
- Online: Score real user interactions
- Versioning allows bisecting regressions in code or prompt config

## License
MIT

## Authors
Hui.

