![Python application test with Github Actions](https://github.com/chegeapollo11/apollo-udacity-ci-cd-pipeline/actions/workflows/main.yml/badge.svg)
[![Build Status](https://dev.azure.com/chegeapollo11/apollo-udacity-ci-cd-pipeline/_apis/build/status/chegeapollo11.apollo-udacity-ci-cd-pipeline?branchName=master)](https://dev.azure.com/chegeapollo11/apollo-udacity-ci-cd-pipeline/_build/latest?definitionId=1&branchName=master)


# Overview

This is a python flask based machining learning application that demostrates DevOps based practices. For this project, a spreadsheet and a trello board have been used to define the project plan and track progress respectively. The project also implements Continuous Integration via Github Actions while Continuous Delivery is achieved using Azure DevOps Pipelines. Finally, the project is fully documented with instuctions on how to run the application in the README file.

## Project Plan

* [Trello Board](https://trello.com/b/oKu23n7d/udacity-ci-cd-project)
* [Project Plan Spreadsheet](project-plan.xlsx)

## Instructions

### Architecture Diagram
![Architecture Diagram](ArchitectureDiagram.png?raw=true "Architecture Diagram")

### Running The Project:
Follow the steps below to get started and run the project:

1.  Connect to **Azure Cloud Shell** from **Azure Portal**.

2.  Clone the project in **Azure Cloud Shell** using this command as illustrated below: `git clone git@github.com:chegeapollo11/apollo-udacity-ci-cd-pipeline.git`
![Azure Cloud Shell Cloned Repository](screenshots/1.%20azure-cloud-shell-cloned-repo.png?raw=true "Azure Cloud Shell Cloned Repository")
3.  Navigate to the newly cloned project using this command: `cd apollo-udacity-ci-cd-pipeline`
4.  Create a local working branch from **Azure Cloud Shell** using this command: `git checkout -b feature/project-demo`
5.  Publish the local working branch to **Github** using this command: `git push -u origin feature/project-demo`
6.  Next, create a python virtual environment from **Azure Cloud Shell** using this command: `python -m venv venv`
7.  Activate the python virtual environment using this command: `source venv/bin/activate`
8.  Make required changes to the project then run tests locally using the following command: `make all`
9.  Observe the following output from **Azure Cloud Shell** if the command runs successfully:
![Azure Cloud Shell Make All](screenshots/2.2.%20azure-cloud-shell-make-all-ml-app.png?raw=true "Azure Cloud Shell Make All")
10. Commit and push your changes to **Github** using the following command: `git add . && git commit -m "Test continuous integration" && git push`
11. Observe that the **Github Actions CI Job** is triggered and executes successfully as illustrated below:
![Github Actions Continuous Integration](screenshots/3.%20github-actions-continuous-integration.png?raw=true "Github Actions Continuous Integration")
12. From **Github**, create a pull request for your working branch with the ***master*** branch as the target branch.
13. Merge and complete the pull request to automatically trigger the **Azure DevOps CD Job**.
14. Nagivate to https://dev.azure.com/{organization}/{project} and confirm a successful run of the **Azure DevOps CD Job** from the pipeline execution logs as illustrated below:
![Azure DevOps Continuous Delivery](screenshots/4.%20azure-devops-pipelines-continuous-delivery.png?raw=true "Azure DevOps Continuous Delivery")
15. Navigate to **Azure Portal** and confirm from the **Azure App Service Deployment Center** that the application was deployed successfully as illustrated below:
![Azure App Service Deployment](screenshots/5.1.%20azure-app-service-deployment.png?raw=true "Azure App Service Deployment")
16. Navigate to the [App Url](https://{app-url}.azurewebsites.net/) and confirm that the application is up and running after deployment as illustrated below:
![Azure App Service Running Application](screenshots/5.2.%20azure-app-service-running-application.png?raw=true "Azure App Service Running Application")
17. From **Azure Cloud Shell**, grant execute permissions to the prediction script by running the following command: `chmod +x make_predict_azure_app.sh`
18. From **Azure Cloud Shell**, verify a prediction from the deployed application in azure by running the following command: `./make_predict_azure_app.sh`
19. Observe the following output from a successful prediction as illustrated below:
![Azure Cloud Shell Make Prediction](screenshots/2.3.%20azure-cloud-shell-make-prediction.png?raw=true "Azure Cloud Shell Make Prediction")

## Enhancements

This project implements DevOps best practices on Azure and so far is a great start but can do with the following improvements:
- Add unit tests for the ***scale*** and ***predict*** methods and ensure the tests run during continuous integration via **Github Actions**.
- Use a single platform for source code management, continuous integration and continuous delivery i.e. either **Github Actions** or **Azure DevOps Pipelines** to simplify maintenance.
- Enable health checks in **Azure App Service** that minitor the health of the application.
- Add monitoring in Azure on the availability of the application and configure alerts that send email notifications when the application is unavailable.
- Add a front end application with that a user interface that users can interact with to make predictions instead of doing it from the terminal.

## Demo 

<TODO: Add link Screencast on YouTube>


