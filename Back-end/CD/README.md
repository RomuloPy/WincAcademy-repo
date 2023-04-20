# CD-Assignment-WincAcademy
This repository was made to submit my WincAcademy CD assignment

[![Python package](https://github.com/RomuloPy/CD-Assignment-WincAcademy/actions/workflows/calculator-flow.yml/badge.svg)](https://github.com/RomuloPy/CD-Assignment-WincAcademy/actions/workflows/calculator-flow.yml)


### 1. Name three components of your solution, explain what they are and how they relate to each other. A 'component' can be anything from GitHub Actions or Bash to Digital Ocean and SSH.

1-	Actions
Actions are a set of code scripts that are designed to automate tasks and integrate with other tools and services. Actions can be used to build, test, deploy, and more. Actions are often packaged as reusable workflows that can be shared with other developers.

2-	SSH keys
SSH keys, short for Secure Shell keys, are a pair of cryptographic keys used to authenticate with remote systems over the Secure Shell (SSH) protocol. The SSH keys consist of a public key and a private key. The private key is kept on the local system and is used to authenticate with remote systems that have the corresponding public key added to the authorized keys file. SSH keys are commonly used for secure communication and remote access to servers and other systems.

3-	Secrets
Secrets are sensitive pieces of data that are used in software development workflows but should not be exposed to the public. Secrets can include passwords, API keys, access tokens, and other sensitive information. Secrets can be stored securely using various tools and services and can be accessed by Actions during a workflow to authenticate with external services or to perform other secure operations.
<br>

***All three of these components can be used together to create secure and efficient software development workflows. For example, an Action may use an SSH key to authenticate with a remote server and then use a secret to access a secure API endpoint. By using these components together, it’s possible to automate the workflows and ensure that sensitive data remains secure.***
<br>


### 2. Discuss three problems that you encountered along the way and how you solved them.


1-	*“Can’t connect without a private SSH key or password”*

- I had to add my Private SSH Key to the repository secrets, otherwise there username and key weren’t known.
	
2-	*"dial tcp :22: connect: connection refused"*
- I had to add my Private SSH Key to the repository secrets, otherwise there wasn’t connection to the server.

3-	*When I close the connection to the server, my flask app doesn’t appear on my browser.*

- The solution was to let the app running on the backgroung with unicorn and set the host to 0.0.0.0 as following on my app.py file : <br>
    `app.run(host="0.0.0.0", debug=True)`
<br>
so now when I commit my project, the changes flow directly to the server because the app is continuously running.
<br>
<br>

### 3. (optional) Anything of note that you want to share about the process of solving this assignment.

The first part of the assignment went quite good and easy, as we had on the previous exercise a similar workflow.

The second part took me a long time to resolve, perhaps because I am not very comfortable with the Linux operating system. In fact, I also had no experience with creating droplets on the server and all related processes.
This exercise meant that I had to do more in-depth research on the Linux operating system and deployment, which made my knowledge about it much richer.