terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 2.70"
    }
  }
}

provider "aws" {
  profile = "default"
  region  = "us-east-1"
}

# NOTE: Create a SSH key for terraform to use in this dir.
resource "aws_key_pair" "sneakbike_key_pair" {
  key_name   = "sneakbike_key_pair"
  public_key = file("~/.ssh/terraform.pub")
}

resource "aws_security_group" "sg_allow_rtmp" {
  name        = "allow_rtmp"
  description = "Allow RTMP inbound traffic"

  ingress {
    description = "RTMP"
    from_port   = 1935
    to_port     = 1935
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    description = "SSH"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "allow_rtmp"
  }
}

# Old instances: 
#   ami             = "ami-0bcc094591f354be2"
#   instance_type   = "t3a.micro"
resource "aws_instance" "sneakbike_instance" {
  key_name        = aws_key_pair.sneakbike_key_pair.key_name
  ami             = "ami-04c7777d0979422a2"
  instance_type   = "t4g.micro"
  security_groups = [aws_security_group.sg_allow_rtmp.name]

  connection {
    type        = "ssh"
    user        = "ubuntu"
    private_key = file("~/.ssh/terraform")
    host        = self.public_ip
  }

  provisioner "remote-exec" {
    inline = [<<EOF
      sleep 1 && \
      sudo add-apt-repository -y ppa:nginx/stable && \
      sleep 1 && \
      sudo apt-get update && \
      sleep 1 && \
      sudo apt-get install -y libnginx-mod-rtmp && \
      sleep 1 && \
      sudo echo "rtmp { server { listen 1935; chunk_size 4096; max_streams 512; application live { live on; record off; } } }" | sudo tee -a /etc/nginx/nginx.conf

      sudo systemctl restart nginx
    EOF
    ]

  }

  provisioner "local-exec" {
    command = "echo ${aws_instance.sneakbike_instance.public_ip}"
  }
}
