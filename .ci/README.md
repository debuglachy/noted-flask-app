# Jenkins CI pipeline

`.ci/Jenkinsfile` contains mostly the same functionality as its Github counterpart [`.github/workflows/ci.yaml`](../.github/workflows/ci.yaml).

> [!IMPORTANT]
> This is one of two independent pipelines that were built while developing the app.
> Only 1 pipeline is used at a time. 

The pipeline file is compatible with the [automated Jenkins deployment](https://github.com/debuglachy/ops/tree/main/lab/kustomize/jenkins/base) where triggers are added to poll Github.

## Continuous Integration

When a change is committed on Github, this file is called and instructs Jenkins to:
- Deploy agents to Kubernetes that package the application and publish its container image to Docker
- Modify the [application yaml](https://github.com/debuglachy/noted-flask-app/blob/main/noted-flask-app.yaml) and commit it into the main branch on Github

## Continuous deployment

Argo watches the yaml file specifically and automatically deploys the new application version to Kubernetes.

## Development history

History of the separate commit and package files continues from the [previous CI workspace](https://github.com/debuglachy/ops/tree/fbf4ecea1ff740be9f1fca318d32d299e0bdacb2/lab/scripts/prototypes/noted-flask-app/ci) before transfer to standalone repo.
