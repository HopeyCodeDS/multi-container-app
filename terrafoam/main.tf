resource "google_compute_instance" "web" {
  name         = "web-server-instance"
  machine_type = "f1-micro"
  zone         = var.zone

  tags = ["http-server", "https-server"]

  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-9"
    }
  }

  network_interface {
    network = "default"

    access_config {
      // Ephemeral IP
    }
  }

  metadata_startup_script = <<-EOF
    #! /bin/bash
    sudo apt-get update
    sudo apt-get install -y docker.io
    sudo systemctl start docker
    sudo docker run -d -p 8080:8080 opeyemimomodu/enterprise-web-app
    EOF

  service_account {
    scopes = ["cloud-platform"]
  }
}

resource "google_compute_instance" "db" {
  name         = "db-server-instance"
  machine_type = "f1-micro"
  zone         = var.zone

  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-9"
    }
  }

  network_interface {
    network = "default"

    access_config {
      // Ephemeral IP
    }
  }

  metadata_startup_script = <<-EOF
    #! /bin/bash
    sudo apt-get update
    sudo apt-get install -y docker.io
    sudo systemctl start docker
    sudo docker run -d -e POSTGRES_DB=Enterprise -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=Student_1234 -p 5432:5432 postgres:13
    EOF

  service_account {
    scopes = ["cloud-platform"]
  }
}
