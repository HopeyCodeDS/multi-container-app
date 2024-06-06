output "web_instance_ip" {
  value = google_compute_instance.web.network_interface[0].access_config[0].nat_ip
}

output "db_instance_ip" {
  value = google_compute_instance.db.network_interface[0].access_config[0].nat_ip
}
