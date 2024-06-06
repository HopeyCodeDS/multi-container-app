provider "google" {
  project = var.project_id
  region  = var.region
}

provider "kubernetes" {
  load_config_file = true
}
