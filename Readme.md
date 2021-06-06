Most of the project settings are configured using [environment variables](https://www.geeksforgeeks.org/environment-variables-in-linux-unix/), a python package is used to read these variables from `.env` file present in the project directory instead.

Run the following command:

```bash
cp .env.example .env
```

The important environment variables that you should be focusing for getting your project running is:

`DATABASE_URL`, it contains the information required to configure the database for the project.

It's syntax is :

```
postgres://db_user:db_password@db_host:db_port/db_name
```

Configure this value in the `.env` file.

Now you need to migrate to apply all the changes to new database, it can be done using following command

```
python manage.py migrate



#Enter data into City Table manually Using django admin:
or
