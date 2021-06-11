#!/usr/bin/env bash

# Variables
resourceGroup="nd082-c2-project"
location="westus"
planName="apollo-udacity-app-service-plan"
webAppName="apollo-udacity-webapp"

# Create resource group
echo "Creating resource group $resourceGroup..."

az group create \
--name $resourceGroup \
--location $location

# Create app service plan
echo "Creating app service plan $planName..."

az appservice plan create \
--resource-group $resourceGroup \
--location $location \
--name $planName \
--is-linux \
--sku F1

# Create web app
echo "Creating web app $webAppName..."

az webapp up \
--resource-group $resourceGroup \
--location $location \
--plan $planName \
--name $webAppName \
--runtime "python|3.6"
