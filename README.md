# Kubernetes Multi Service Web App Deployment

This project deploys a simple FastAPI backend that writes to a PostgreSQL database in a local Kubernetes cluster (minikube). This is intended as a learning exercise to practice Kubernetes concepts such as Deployment, Service, ConfigMaps etc. Everything can be deployed locally.

## Prerequisites

The following software should be installed beforehand (assume macOS):
- Docker Desktop
- minikube
- kubectl 

You should also have a Docker Hub account

## Installation

Build the image and tag it with your Docker Hub username

```bash
docker build --tag {your-docker-hub-username}/k8s-multi-service-app:latest .
```

Push the image to Docker Hub

```bash
docker push {your-docker-hub-username}/k8s-multi-service-app:latest
```

Set up a local Kubernetes cluster with 3 nodes via minikube

```bash
minikube start --nodes 3 --profile k8s-multi-service-app --cni=kindnet
```

Replace the following line in `k8s/kustomization.yaml` with your Docker Hub username

```yaml
newName: your-docker-hub-username/k8s-multi-service-app
```

Deploy onto the local Kubernetes cluster

```bash
kubectl apply -k k8s/ --validate=false
```

## Usage

Open up a tunnel to the Kubernetes cluster so that you can access it via localhost

```bash
minikube tunnel -p k8s-multi-service-app
```

curl the healthcheck endpoint to ensure that you can reach the backend FastAPI

You should receive a HTTP 200 OK in your reponse

```bash
curl -i http://127.0.0.1:8080/healthcheck
```

curl the root endpoint which will write some request information to the database

You should receive a HTTP 200 OK as well as a response indicating the path, host, port and time of the request

```bash
curl -i http://127.0.0.1:8080
```

## Contributing

Feel free to use this repo for your own learning purposes