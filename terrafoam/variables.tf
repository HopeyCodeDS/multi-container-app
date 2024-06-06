variable "project_id" {
  description = "The ID of the project in which to provision resources."
  default     = "myinfra3-project"
}

variable "region" {
  description = "The region in which to provision resources."
  default     = "europe-west1"
}

variable "zone" {
  description = "The zone in which to provision resources."
  default     = "europe-west1-b"
}
