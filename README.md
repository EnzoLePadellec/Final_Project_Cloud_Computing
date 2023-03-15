> ## Final Project - Cloud Computing

This application is a web-based platform that displays information about various species of eagles. It retrieves data from a MongoDB database and presents it in a formatted text format on the homepage. Users can browse through the list of eagles and view their descriptions. Additionally, the application provides a link to an acknowledgements page, which displays a list of contributors to the project. The application runs as a Docker container, using the Flask framework for the web interface and MongoDB as the database management system. The application is designed to be scalable and efficient, with the use of containerization technology and network configuration to facilitate communication between different services.


> ## 👷 Prerequisites

1. Have a Github account properly setup with your local Git
   > You should use ssh authentication between your local git and
   Github. **[How to set it up](https://help.github.com/articles/connecting-to-github-with-ssh)**

2. **Fork** the repository

   ![fork button](img/fork.png)

3. **Clone** your fork locally
    ```shell
    cd /path/to/workspace 
    git clone git@github.com:YOUR_USERNAME/Final_Project_Cloud_Computing.git
    ```

4. Have Docker installed on your computer.

5. Execute the command line 'docker-compose up'
    ```shell
    docker-compose up
    ```
6. Check the result, `🚀 It Works!`


> ## Docker Hub

Project link : https://hub.docker.com/layers/enzolp/final_project-app/latest/images/sha256:0ad53d352475eaedc8340bc9a1fb25ae2fb2e4f00ae6bfafc461c06607f66c83