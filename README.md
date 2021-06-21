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
