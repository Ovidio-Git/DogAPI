# DOGS API
 Code for build a Api DOGS
 
 
## Description
Proyect made with Docker, Flask, Python and JWT autetication 


## Endpoints

1- `POST /auth`
<br>Description: get JWT token.
- Example:
  <br>[http://127.0.0.1:5000/auth](http://127.0.0.1:5000/auth)

 Request:
   ```json
   {
       "username": "root",
       "password": "t4p1"
   }
  ```
 Response:
   ```json
   {
       "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2MjQyNTAwMTEsImlhdCI6MTYyNDI0OTcxMSwibmJmIjoxNjI0MjQ5NzExLCJpZGVudGl0eSI6MX0.KRp9b5Mf-   L3WPwSzyOiqsmaWGWypXDRth34qvPoV8Co"
   }
  ```
 
<br>
2- `POST /api/dogs/`
<br>Description:Create items for names.
- Example:
  <br>[http://127.0.0.1:5000/api/dogs/](http://127.0.0.1:5000/api/dogs/)

 Request:
   ```json
  {
     "id_dog" : 1, 
     "name":"loky",
     "is_adopted" :false
  }
  ```
 Response:
   ```
    200 OK CREATE
  ```
<br>
3- `GET /api/dogs/`
<br>Description:Read all items.
- Example:
  <br>[http://127.0.0.1:5000/api/dogs/](http://127.0.0.1:5000/api/dogs/)

 Response:
   ```json
[
    {
       "create_date": "Mon, 21 Jun 2021 04:32:22 GMT",
       "id_dog": 1,
       "is_adopted": false,
       "name": "loky",
       "picture": "https://images.dog.ceo/breeds/terrier-australian/n02096294_8557.jpg"
    },
    {
       "create_date": "Mon, 21 Jun 2021 04:36:11 GMT",
       "id_dog": 2,
       "is_adopted": true,
       "name": "shot",
       "picture": "https://images.dog.ceo/breeds/basenji/n02110806_1404.jpg"
    }
]
  ```

