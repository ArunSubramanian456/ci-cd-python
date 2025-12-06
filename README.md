# ci-cd-python
- Ensure port 80 is available

Steps
1. Create ECR repository "my-flask-app" using AWS Console
2. Create a EC2 instance using AWS Console
   a. Create an instance profile with ECRFullAccess permission as part of the EC2 Launch template
3. Log into the EC2 instance using EC2 instance connect via browser
    1. update the server with root user privileges
    2. install docker with root user privileges
    3. start docker with root user privileges
    4. check the status of docker with root user privileges
    5. add ec2-user to the 'docker' group granting permission to run docker commands w/o sudo
    6. activate the new 'docker' group
    7. run docker -- version command to see if everything works perfectly
    8. login to ecr via aws cli or PowerShell
4. Setup GitHub repo with app.py, README.md, tests.py and 
   .github\workflows\actions.yml
     1. sync local and remote
     2. Setup Actions secrets in GitHub repo (will be used by actions.yml)
5. Push updates to the remote repo to trigger the actions workflow.

```
sudo yum update -y
sudo yum install -y docker 
sudo systemctl start docker
sudo service docker status 
sudo usermod -a -G docker ec2-user 
newgrp docker
docker —-version
```