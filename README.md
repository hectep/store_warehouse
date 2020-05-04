# store_warehouse
Both projects use same poetry, but are in separate docker containers

To start up each project:

- store
```
docker-compose -f docker-compose-store.yml build
docker-compose -f docker-compose-store.yml up
```

and in different terminal:
- warehouse
```
docker-compose -f docker-compose-warehouse.yml build
docker-compose -f docker-compose-warehouse.yml up
```

For easier testing env variables are prepopulated and superusers are created for both projects via migrations:
- store: 
```store_admin:store_admin```
- warehouse: 
```warehouse_admin:warehouse_admin```

So to test functionality you need to add a link in each project to each other.
So, in warehouse project in admin you need to create a store instance 
(ip address can be found with ```docker inspect id_here  | grep IPAddress```) so it would look like this:

![test test](https://i.imgur.com/35UpCj2.png)

The name ```test_store``` is prepopulated in env variables.
