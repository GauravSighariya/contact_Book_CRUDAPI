# Django_CRUDAPIs-for-a-contact-book-app
A suite of CRUD APIs for a contact book app .

## Functionality
- Authentication of User
- Create Contact       
- Read Contact
- Update Contact
- Delete Contact

## Requirements
- Python 3.6
- Django (2.2.13)
- Django REST Framework (3.9.4)
- Django Rest Auth

## Set Up Guide ..

### Use virtual environment (Suggested)
    
   #### An isolated workspace for the Project and  the requirement is Python 
    
        install virtualenvwrapper-win
        
        mkvirtualenv env_name      
        
        workon env_name
        
  
* <Open the terminal/shell and insert>

           git clone https://github.com/kamlesh1807/Django_CRUDAPIs-for-a-contact-book-app.git

           pip install -r requirements.txt

           python3 manage.py makemigrations

           python3 manage.py migrate

           python3 manage.py runserver


## Structure
In a RESTful API, endpoints (URLs) define the structure of the API and how end users access data from our application using the HTTP methods - GET, POST, PUT, DELETE.

 1. To Register a new user - POST 

         http://127.0.0.1:8080/api/ky/accounts/register/
         
       Note : Provide <b> Unique </b> UserName, Email , First  name , Last name . 
 2. To get the Token -  POST
 
         http://127.0.0.1:8080/api/ky/accounts/token/
         
 3. To Add Contact  - POST
              
         http://127.0.0.1:8080/api/ky/server/  Authorization Token : eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjExNDI0ODUxLCJqdGkiOiJkODcyNTM
         
      Note : Provide <b> Unique </b> Email , First  name , Last name , Phone no   and optional number.
 4. To List Contact  - GET
   
         http://127.0.0.1:8080/api/ky/server/   Authorization Token :eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjExNDI0ODUxLCJqdGkiOiJkODcyNTM 
         
     Note : it will display the contact details.    
 5.  To Update Contact  - PUT
  
         http://127.0.0.1:8080/api/ky/server/<ID>   Authorization Token : eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0bNjZXNzIiwiZXhwIjoxNjExNDI0ODUxLCJqdGkiOiJkODcyNTM
           
     Note : to update a contact -The  ID of the Contact which we want to update is passed while calling with the generated token.
           
 6.  To Delete Contact  - DELETE
  
         http://127.0.0.1:8080/api/ky/server/<ID>   Authorization Token :eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjNDI0ODUxLCJqdGkiOiJkODcyNTM
           
      Note : to Delete a contact -The  ID of the Contact which we want to update is passed while calling with the generated token.
     
     
## Test

  We can test the API using  POSTMAN  extension.
  
  ### Registration of a new user Add Contact Read Contact Update and Delete Contact  :
  
  ![Register A user](https://user-images.githubusercontent.com/61351274/105619902-230c4000-5e1d-11eb-9359-28a8e96a6ab0.JPG)

  ### Get Token of the Registered user
  
  ![Get token](https://user-images.githubusercontent.com/61351274/105619900-21db1300-5e1d-11eb-9af6-8204eaf2119b.JPG)
 
  ### Add Contact 
  
  ![Add contact](https://user-images.githubusercontent.com/61351274/105619898-1f78b900-5e1d-11eb-9f4c-6203adb4c706.JPG)
  
  ### List All Contact
  
  ![List All Contact](https://user-images.githubusercontent.com/61351274/105619901-2273a980-5e1d-11eb-9132-804c0496cd37.JPG)
  
  ### Update a Contact
  
  ![update](https://user-images.githubusercontent.com/61351274/105619903-23a4d680-5e1d-11eb-859c-c39aed039150.JPG)
  
  ### Delete a Contact'
  
  ![Delete contact](https://user-images.githubusercontent.com/61351274/105619899-20a9e600-5e1d-11eb-953c-2bc097e65744.JPG)

### Thanks For Visit.  
  
 
 
 
  
  


      
      
