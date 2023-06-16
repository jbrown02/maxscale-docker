# MariaDB MaxScale Docker image

This Docker image runs the latest 2.4 version of MariaDB MaxScale.

## Introduction
This project will enable the user to access a sharded MySQL database of zipcodes and perform SQL queries to interact with their data. It utilizes an instance of MaxScale Docker to run the servers, and MariaDB to interact with the databases. In addition, the main.py script included in the maxscale-docker/maxscale directory will output the information required of this project upon running.

## Installation
You can run the following command to install MaxScale on your VM:

```
curl -LsS https://r.mariadb.com/downloads/mariadb_repo_setup | sudo bash
```

This assumes that you already have curl and ca-certificates packages installed on the system. The install commands for these packages are:

```
sudo apt-get install curl
sudo apt-get install ca-certificates -y
```

When this is done, you should be able to start configuring your MaxScale container.

## MaxScale Docker Compose Setup
To properly set up MaxScale Docker Compose, first navigate to the proper directory or create a new one (ensure that you have full rights to modify the directory). Next, clone the Git repository containing all of the needed files and file associations with the command:

```
git clone https://github.com/jbrown02/maxscale-docker/
```

This should enable you to accurately recreate the appropriate MaxScale environment on your device.

### Configuration

The [default configuration](maxscale/maxscale.cnf) for the container is minimal
and only enables the REST API.

The REST API by default listens on port 8989. Accessing it from the docker host requires a port mapping specified on container startup. The example below shows general information via curl:

```
sudo docker run -d -p 8989:8989 --name mxs mariadb/maxscale:latest
sudo curl -u admin:mariadb http://localhost:8989/v1/maxscale
```

See [MaxScale documentation](https://github.com/mariadb-corporation/MaxScale/blob/2.4/Documentation/REST-API/API.md) for more information about the REST API.

## Configuration
The MariaDB MaxScale Docker image can be configured by editing the maxscale.cnf.d/example.cnf file:

1. Locate the maxscale.cnf.d/example.cnf file. It will be in the directory that you cloned the main Git repository to.
2. Open the file in the Nano text editor with:
   
   ```
   sudo nano example.cnf
   ```
   
3. Modify the configuration options as needed. Refer to the MaxScale documentation for help, as it describes how to configure MariaDB MaxScale and presents some possible usage scenarios. Make sure your server names and types match those designated in the docker-compose.yml file also located in the maxscale-docker/maxscale directory.

## Running
[The MaxScale docker-compose setup](./maxscale/docker-compose.yml) contains MaxScale configured with two primary nodes. To start it, make sure you're in the maxscale-docker/maxscale directory and run the following command:

```
sudo docker-compose up -d
```

After the process finishes and, your servers should be up and running after being given a few moments to connect. You can check their status with the command:

```
sudo docker-compose exec maxscale maxctrl list servers
```

The output should look like this:

```
┌─────────┬──────────┬──────┬─────────────┬─────────────────┬──────┬─────────────────┐                                                                    
│ Server  │ Address  │ Port │ Connections │ State           │ GTID │ Monitor         │                                                                    
├─────────┼──────────┼──────┼─────────────┼─────────────────┼──────┼─────────────────┤                                                                    
│ server1 │ primary1 │ 3306 │ 0           │ Master, Running │      │ MariaDB-Monitor │
├─────────┼──────────┼──────┼─────────────┼─────────────────┼──────┼─────────────────┤                                                                    
│ server2 │ primary2 │ 3306 │ 0           │ Running         │      │ MariaDB-Monitor │
└─────────┴──────────┴──────┴─────────────┴─────────────────┴──────┴─────────────────┘  
```

The database can be accessed with the following credentials:

Username: maxuser

Password: maxpwd

Below is the command that includes these credentials and the resulting terminal output:

```
sudo mysql -umaxuser -pmaxpwd -h 127.0.0.1 -P 4000
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 4
Server version: 11.0.2-MariaDB-1:11.0.2+maria~ubu2204 mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]>
```

You can now enter SQL queries in the terminal to interact with the database. To exit the database, simply type "exit".

### Running the Script
The main.py script executes a series of 4 SQL queries:

1. The largest zipcode in zipcodes_one
2. All zipcodes where state = KY (Kentucky)
3. All zipcodes between 40000 and 41000 
4. The TotalWages column where state = PA (Pennsylvania)

You can run the script with the command:

```
sudo python3 main.py
```

The output should look like this:

```
The largest zipcode in zipcodes_one:
(47750,)
All zipcodes where state = KY:
40003 40022
40004 40023
40006 40025
40007 40026
40008 40027
40009 40031
40010 40032
40011 40033
40012 40036
40013 40037
(etc.)
All zipcodes between 40000 and 41000:
40003 40022
40004 40023
40006 40025
40007 40026
40008 40027
40009 40031
40010 40032
40011 40033
40012 40036
40013 40037
(etc.)
The TotalWages column where state = PA:
330884386 
33137755 
331848277 
332596067 
33272489 
33341723 
333541869 
333547254 
333739234 
33407100 
(etc.)
```

Once complete, to remove the cluster and MaxScale containers:

```
sudo docker-compose down -v
```

### Troubleshooting
If you run main.py and the process hangs, kill it and confirm the IP address of the MaxScale instance with the command:

```
sudo docker inspect maxscale-maxscale-1
```

The Docker instance gets assigned a new IP address on startup, and so the process will hang if the IP address in the Python file doesn't match the Docker instance IP. Take the IP provided and insert it into the main.py file. The script should run properly after this.
