# Docker example for MOOC course

Course name: Devops with Docker.

## Description

A docker image built from Grafana base. Provisions one datasource and one dashboard.
Displays a bar chart of population data. Data originally from Statistics Finland.

Secure access is not configured. Run this locally and do not expose port 3000 to internet.

## Building image

`docker build . --tag ikaluokat`

### Running image

`docker run -d -p 3000:3000 --name ikaluokat-app ikaluokat`

Navigate to `http://localhost:3000`  
Log in as user `docker` and password `moocmooc`.  
View should default to dashboard `Väestö iän mukaan 31.12.2023`
