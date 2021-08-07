Based on [SummerProject2.5](https://github.com/DylanB5402/SummerProject2.5)

How to run:

- Create password.py

- install dependencies

    - pip install -r requirements.txt
    
Design Decisions:

- Run app on Heroku

- Receive url via http request

    - Save url to Firebase Database

    - Display new url on client side 

- Download url

    - Get which story to download via http request

    - Flag url with download tag in firebase (Cloud Firestore)
    
    - Respond with 202 success status code

    - Send url to be downloaded + emailed by worker process 



