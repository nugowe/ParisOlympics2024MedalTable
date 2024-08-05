
![Screenshot from 2024-08-04 18-08-09](https://github.com/user-attachments/assets/c50e5f48-ea0d-4b3f-9064-788f19bc74f2)

## Docker run command:
docker run -it -p 4444:4444 nosaugowe/paris_olympicgames_medaltable

## This repo contains a Django Application that is used to query the medal table of the various Nations participating in the Paris Olympic games.

## TECHNICAL BREAKDOWN

This Django application uses Django Filter to query the database from a HTML form where the resulting output is rendered on to the webpage. 

HTMX is used to make AJAX calls to end points where the html data is directly added to the dom. HTMX is used to refresh the webpage and provide the Tournament count down clock.

### BASIC USAGE:

## WITHOUT THE CONTAINER  | VIA MAKEFILE

## DEPLOY THE SQUADLIST APP VIA DJANGO DIRECTLY....

Simply run the command:

make DEPLOY-MEDALTABLE-LOCALLY

## DEPLOY THE SQUADLIST APP ON TO A KUBERNETES CLUSTER (MICROK8S IN MY CASE)

Simply run the command:

make DEPLOY-MEDALTABLE-K8s


## PORT-FORWARD THE EPLSQUADLIST APP TO A WEB BROWSER (TO BE USED WHEN DEPLOY IN A KUBERNETES CLUSTER)

Simply run this command:

make PORT-FORWARD-MEDALTABLE-K8s
