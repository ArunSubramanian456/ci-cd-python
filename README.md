# ci-cd-python - Commands to install Docker on EC2 
- Ensure port 80 is available

Steps
1. update the server with root user privileges
2. install docker with root user privileges
3. start docker with root user privileges
4. check the status of docker with root user privileges
5. add ec2-user to the 'docker' group granting permission to run docker commands w/o sudo
6. activate the new 'docker' group
7. run docker -- version command to see if everything works perfectly
8. login to ecr via aws cli or PowerShell

```
sudo yum update -y
sudo yum install -y docker 
sudo systemctl start docker
sudo service docker status 
sudo usermod -a -G docker ec2-user 
newgrp docker
docker —-version


# Login to ECR via AWS CLI
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin aws_account_id.dkr.ecr.us-east-1.amazonaws.com

# Alternate option via PowerShell using AWS Tools
(Get-ECRLoginCommand).Password | docker login --username AWS --password-stdin aws_account_id.dkr.ecr.us-east-1.amazonaws.com
```