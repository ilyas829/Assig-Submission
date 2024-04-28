# Assig-Submission

<!-- To run the app 
1. git clone the repository "https://github.com/ilyas829/Assig-Submission.git"
2. Change the directory to Assig-Submission
3. run command python -m venv flask-app to create a virtual environment
4. from command-palattet choose python interp to venv python.exe
5. run command   .\flask-app\Scripts\activate  to activate env
6. Run Command python -m pip install -r .\requirements.txt to install dependencies
7. Run python app.py -->

Web Application and CI/CD Pipeline
Introduction
This repository contains a simple web application built using Flask for Python. Additionally, it includes a GitHub Actions CI/CD pipeline for automating testing and deployment to Azure App Service. This README provides detailed instructions on how to run the application locally and an overview of the CI/CD pipeline setup.

Running the Application Locally
To run the web application locally, follow these steps:

Ensure you have Python installed on your system. You can download Python from the official website.
Clone this repository to your local machine:
bash
Copy code
git clone <repository-url>
Navigate to the repository directory:
bash
Copy code
cd <repository-directory>
Install the required Python dependencies:
Copy code
pip install -r requirements.txt
Run the Flask application:
Copy code
python app.py
Open a web browser and visit http://localhost:5000 to view the application.
CI/CD Pipeline Overview
The CI/CD pipeline automates the testing and deployment process using GitHub Actions. Below is an overview of the pipeline:

Pipeline Steps
Test: This job runs on every push to the main branch. It sets up a Python environment, installs dependencies, and runs unit tests using unittest. It sets the FLASK_ENV environment variable to testing to ensure the application runs in testing mode.
Deploy: This job runs after the test job succeeds. It deploys the application to Azure App Service using the Azure Web Apps Deploy GitHub Action. It only runs if the previous job succeeds (if: success()).
Tool Choices
Flask: Chosen for its simplicity and flexibility in building web applications with Python.
unittest: Standard Python unit testing framework for writing and executing tests.
GitHub Actions: Used for CI/CD automation due to its tight integration with GitHub repositories and ease of use.
Azure Web Apps: Chosen as a free-tier cloud service for deploying the web application due to its ease of use and integration with GitHub Actions.
Scaling for Larger Applications
The setup described in this repository can be scaled for larger applications with some modifications:

Infrastructure as Code (IaC): Implement IaC tools like Terraform or ARM templates to manage infrastructure provisioning. This ensures consistency and scalability as your application grows.
Containerization: Containerize your application using Docker. This allows for easier deployment and scaling of services, especially in a microservices architecture.
Integration Tests: Incorporate integration tests into your CI/CD pipeline to validate the interaction between different components of your application.
Deployment Strategies: Explore different deployment strategies like blue-green deployments or canary releases to minimize downtime and risk during deployments.
Conclusion
The provided web application and CI/CD pipeline offer a basic foundation for automating the testing and deployment process. By following the instructions in this README and understanding the CI/CD process, you can efficiently manage and deploy your web applications with confidence..

