provider "aws" {
  access_key     = "${var.access_key}"
  secret_key     = "${var.secret_key}"
  region     = "${var.region}"
}

resource "aws_instance" "example" {
  ami           = "${lookup(var.amis, var.region)}"
  instance_type = "t2.micro"
  # depends_on = ["example_bucket"]

  provisioner "local-exec" {
    command = "echo ${aws_instance.example.public_ip} > ip_address.txt"
  }
}

resource "aws_eip" "ip" {
  instance = "${aws_instance.example.id}"
}

# resource "aws_s3_bucket" "example_bucket" {
  # bucket = "lambdude-terraform-getting-started-guide01"
  # acl    = "private"
# }

resource "aws_instance" "another" {
  ami           = "ami-b374d5a5"
  instance_type = "t2.micro"
}
