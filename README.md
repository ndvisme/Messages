# Run app using Docker Compose:

1. Build images
   using the following CLI command:

   ```
   docker compose build
   ```

2. Run containers:
   run the following command:

   ```
   docker compose up
   ```

   Checks:

   - That containers are running:

     Enter command:

     ```
     docker ps -a
     ```

     alternetvly, go to Docker Desktop app & check if containers are running.

   - Postgres DB is running:

     1. Install 'Tableplus' app.

     2. Open and connect to running DB container using credentials from `docker-compose.yml` file.

# Run tests:

1. Start project containers

2. Enter 'messages_api' container using intercative shell:
   command:

   ```
   docker exec -it messages_api bash
   ```

3.1 To run all the tests in the project run 'messages_api' shell run the following command:

```
python -m pytest
```

3.2 To run one tests file run 'messages_api' shell run the following command:

```
python -m pytest tests/<test_file_name>
```

3.3 To run one test from a file run 'messages_api' shell run the following command:

```
python -m pytest tests/<test_file_name> -k <test_name>
```
