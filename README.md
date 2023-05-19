# Animal Shelter API

This is the API documentation for the Animal Shelter application, which allows managing data related to animals in the
shelter. The API is built using the Flask-RESTful framework and provides HTTP methods GET, POST, PATCH, and DELETE for
interacting with animal resources.
 # Getting Started #
## Clone the repository:
```
git clone https://github.com/KamilWardyla/shelter-api
```
## Install the required dependencies:

```
pip install requests
```

### Resources ####

#### Get List of Animals ####

Method: GET

Path: /animals

Returns a list of all animals in the shelter.

Sample Response:

```json
  [{
  "name": "Rex",
  "type": "Pies",
  "race": "German Shepherd",
  "age": 5
  },  
  {
  "name": "Luna",
  "type": "Pies",
  "race": "White swiss Shepherd",
  "age": 3
}]
```
#### Get Animal ###
Method: GET
Path: /animal/{id}

Get a specific animal based on its ID.


#### Add a New Animal #####
Method: POST
Path: /animal

Adds a new animal to the shelter.

Request Parameters:

name (string, required) - The name of the animal.

type (string, required) - The type of the animal.

race (string, required) - The race of the animal.

age (integer, required) - The age of the animal.

Sample Response:
```json
{
  "id": 3,
  "name": "Rex",
  "type": "Dog",
  "race": "German Shepherd",
  "age": 5
}
```
#### Update Animal Information ####
Method: PATCH
Path: /animal/{id}

Updates the information of a specific animal based on its ID.

Request Parameters:

name (string) - The new name of the animal.

type (string) - The new type of the animal.

race (string) - The new race of the animal.

age (integer) - The new age of the animal.


#### Delete an Animal ###
Method: DELETE
Path: /animal/{id}

Deletes a specific animal based on its ID.

### Notes ###
All parameters (name, type, race, and age) are required and must be provided in POST requests.
The age parameter should be an integer representing the age of the animal in years.
In case of missing or invalid data in the requests, the API returns appropriate error messages along with the corresponding HTTP response code.
