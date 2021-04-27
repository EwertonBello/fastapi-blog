FROM mysql:latest


#create folder
RUN mkdir -p /opt/code
RUN mkdir -p /opt/code/api

WORKDIR /opt/code/api

# Expose the default port
EXPOSE 3306
