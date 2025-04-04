terraform {
  required_providers {
    kubernetes = {
      source  = "hashicorp/kubernetes"
      version = "~> 2.0"
    }
    helm = {
      source  = "hashicorp/helm"
      version = "~> 2.0"
    }
  }
}

provider "kubernetes" {
  config_path = "~/.kube/config"
}

provider "helm" {
  kubernetes {
    config_path = "~/.kube/config"
  }
}

# Namespace
resource "kubernetes_namespace" "marketing_ai" {
  metadata {
    name = "marketing-ai"
  }
}

# MinIO
resource "helm_release" "minio" {
  name       = "minio"
  repository = "https://charts.min.io/"
  chart      = "minio"
  namespace  = kubernetes_namespace.marketing_ai.metadata[0].name

  set {
    name  = "accessKey"
    value = var.minio_access_key
  }

  set {
    name  = "secretKey"
    value = var.minio_secret_key
  }

  set {
    name  = "persistence.size"
    value = "10Gi"
  }
}

# MLflow
resource "helm_release" "mlflow" {
  name       = "mlflow"
  repository = "https://community-charts.github.io/helm-charts"
  chart      = "mlflow"
  namespace  = kubernetes_namespace.marketing_ai.metadata[0].name

  set {
    name  = "backendStore.uri"
    value = "postgresql://${var.postgres_user}:${var.postgres_password}@postgres:5432/mlflow"
  }

  set {
    name  = "artifactRoot"
    value = "s3://mlflow"
  }
}

# Nessie
resource "helm_release" "nessie" {
  name       = "nessie"
  repository = "https://charts.projectnessie.org"
  chart      = "nessie"
  namespace  = kubernetes_namespace.marketing_ai.metadata[0].name

  set {
    name  = "persistence.enabled"
    value = "true"
  }

  set {
    name  = "persistence.size"
    value = "10Gi"
  }
}

# PostgreSQL
resource "helm_release" "postgres" {
  name       = "postgres"
  repository = "https://charts.bitnami.com/bitnami"
  chart      = "postgresql"
  namespace  = kubernetes_namespace.marketing_ai.metadata[0].name

  set {
    name  = "postgresqlUsername"
    value = var.postgres_user
  }

  set {
    name  = "postgresqlPassword"
    value = var.postgres_password
  }

  set {
    name  = "postgresqlDatabase"
    value = "mlflow"
  }

  set {
    name  = "persistence.size"
    value = "10Gi"
  }
}

# Variáveis
variable "minio_access_key" {
  type = string
}

variable "minio_secret_key" {
  type = string
}

variable "postgres_user" {
  type = string
}

variable "postgres_password" {
  type = string
} 