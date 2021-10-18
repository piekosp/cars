# cars
It's a simple REST API application - a basic car makes and models database interacting with an external API (https://vpic.nhtsa.dot.gov/api/) checking if given car exisits.

## preview 
App is deployed on Heroku. You can check how it works here: https://cars-pawel.herokuapp.com/. If website doesn't load please wait and reload site.

## instalation 
1. clone the repository
2. run docker-compose build
3. run docker-compose up
4. app is exposed on http://127.0.0.1:8000/

## endpoints
- **POST /cars/**

    *App check if car with given data exists. If yes, it adds it to database*

    ```python
    {
        "make" : "Volkswagen",
        "model" : "Golf",
    }
    ```

- **DELETE /cars/{id}/**

    *Delete the car with the given id from database If the car doesn't exist in database - returns an error*

- **POST /rate/**

    *Add a rat for a car from 1 to 5*

    ```python
    {
        "car_id" : 1,
        "rating" : 5,
    }
    ```

- **GET /cars/**

    *Fetches a list of all cars already present in application database with their current average rate*

    Response:

    ```python
    [
        {
        "id" : 1,
        "make" : "Volkswagen",
        "model" : "Golf",
        "avg_rating" : 5.0,
        },
        {
        "id" : 2,
        "make" : "Volkswagen",
        "model" : "Passat",
        "avg_rating" : 4.7,
        }
    ]
    ```

- **GET /popular/**

    *Returns top cars already present in the database ranking based on a number of rates*


    Response:

    ```python
    [
        {
        "id" : 1,
        "make" : "Volkswagen",
        "model" : "Golf",
        "rates_number" : 100,
        },
        {
        "id" : 2,
        "make" : "Volkswagen",
        "model" : "Passat",
        "rates_number" : 31,
        }
    ]
    ```




