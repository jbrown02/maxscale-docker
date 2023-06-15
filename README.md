# MariaDB MaxScale Docker image

This Docker image runs the latest 2.4 version of MariaDB MaxScale.

## Configuration
The MariaDB MaxScale Docker image can be configured by editing the maxscale.cnf.d/example.cnf file:

1. Locate the maxscale.cnf.d/example.cnf file. It will be in the directory that you cloned the main Git repository to.
2. Open the file in the nano text editor with:
   
   ```
   sudo nano example.cnf
   ```
   
3. Modify the configuration options as needed. Refer to the MaxScale documentation for help, as it describes how to configure MariaDB MaxScale and presents some possible usage scenarios. Make sure your server names and types match those designated in the docker-compose.yml file

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

The  database can be accessed with the following credentials:

Username: maxuser
Password: maxpwd

Below is the command that includes these credentials and the resulting terminnal output:

```
sudo mysql -umaxuser -pmaxpwd -h 127.0.0.1 -P 4000
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 4
Server version: 11.0.2-MariaDB-1:11.0.2+maria~ubu2204 mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]>
```

You can now enter SQL queries in the terminal to interact with the database. To exit the database, simply "exit". Once complete, to remove the cluster and MaxScale containers:

```
sudo docker-compose down -v
```

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
