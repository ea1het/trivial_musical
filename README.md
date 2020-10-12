# Trivial Musical
Trivial Musical for educational purposes (see license)

### Contact
If you need to know more about this repo, its licensing posibilities or any other aspect, please, 
get in touch with  [Marcial Ruiz Escudero](mailto:#@#)

## Database model
![](docs/ER.png)

## Dot-env (.env) example file
In order to rule out the application behavior you need to use environment variables. In devel time
you can use a '.env' file locally. In run time, if you are using containers, you need to use
environment variables injected upon container instantiation. 

```
export SECRET_KEY = 'Qs----------------------------------------------4azm'

export DB_TYPE = 'postgres'
export DB_HOST = 'localhost'
export DB_PORT = 5432
export DB_USER = 'DB_user'
export DB_PASSWORD = 'DB_pass'
export DB_DATABASE = 'DB_name'

export ENV = 'development'
export DEBUG = True
export TESTING = false

```
