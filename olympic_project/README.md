## This repo contains a Django Application that is used to query the squad list of the various teams participating in the English Premier League 2023-2024 Season.

### BASIC USAGE:

## WITHOUT THE CONTAINER  | VIA MAKEFILE

## DEPLOY THE SQUADLIST APP VIA DJANGO DIRECTLY....

Simply run the command:

make DEPLOY-SQUADLIST-LOCALLY

## DEPLOY THE SQUADLIST APP ON TO A KUBERNETES CLUSTER (MICROK8S IN MY CASE)

Simply run the command:

make DEPLOY-SQUADLIST-K8s


## PORT-FORWARD THE EPLSQUADLIST APP TO A WEB BROWSER (TO BE USED WHEN DEPLOY IN A KUBERNETES CLUSTER)

Simply run this command:

make PORT-FORWARD-SQUADLIST-K8s