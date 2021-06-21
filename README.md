# DogAPI
 Code for build a Api DOGS
  
## Description
 Proyect made with Docker, Flask, Python and JWT autetication  and MySQL 

## Endpoints

<br>

**1-** `POST /auth`
<br>
<br>Description: Get JWT token.
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
<br>

**2-** `POST /api/dogs/`
<br>
<br>Description: Create items for names.
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
<br>

**3-** `GET /api/dogs/`
<br>
<br>Description: Read all items.
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

<br>
<br>

**4-** `GET /api/dogs/<dname>`
<br>
<br>Description: Read items for names.
- Example:
  <br>[http://127.0.0.1:5000/api/dogs/shot](http://127.0.0.1:5000/api/dogs/shot)

 Response:
   ```json
 {
    "create_date": "Mon, 21 Jun 2021 04:36:11 GMT",
    "id_dog": 2,
    "is_adopted": true,
    "name": "shot",
    "picture": "https://images.dog.ceo/breeds/basenji/n02110806_1404.jpg"
 }
 ```

<br>
<br>

**5-** `GET /api/dogs/is_adopted`
<br>
<br>Description: Read items for is_adopted.
- Example:
  <br>[http://127.0.0.1:5000/api/dogs/is_adopted](http://127.0.0.1:5000/api/dogs/is_adopted)

 Response:
   ```json
[
   {
      "create_date": "Mon, 21 Jun 2021 04:36:11 GMT",
      "id_dog": 2,
      "is_adopted": true,
      "name": "shot",
      "picture": "https://images.dog.ceo/breeds/basenji/n02110806_1404.jpg"
   },
   {
      "create_date": "Mon, 21 Jun 2021 04:40:18 GMT",
      "id_dog": 3,
      "is_adopted": true,
      "name": "bronco",
      "picture": "https://images.dog.ceo/breeds/papillon/n02086910_6305.jpg"
   }
]
 ```

<br>
<br>

**6-** `UPDATE /api/dogs/<dname>`
<br>
<br>Description: Update items for names.
- Example:
  <br>[http://127.0.0.1:5000/api/dogs/bronco](http://127.0.0.1:5000/api/dogs/bronco)

 Request:
   ```json
  {
     "id_dog" : 3, 
     "name":"broncono",
     "is_adopted" :true
 }
 ```
 Response:
 ```
    200 OK UPDATE
 ```


<br>
<br>

**7-** `DELETE /api/dogs/<dname>`
<br>
<br>Description: Delete items for names.
- Example:
  <br>[http://127.0.0.1:5000/api/dogs/broncono](http://127.0.0.1:5000/api/dogs/broncono)

 Response:
  ```
    200 OK DELETE
 ```


