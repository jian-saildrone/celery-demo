# Django + Celery demo 

## Set up environment 


## Task 1: 

## Task 2: Develop an example app - sending emails with Django and Celery 
- create a form / view 
- build new Celery task (seond emails)
- configure email server - Gmail configuration 

### Workflow
> Client --> Django --> RabbitMQ(message broker) --> Celery 
1. on client side, the user will fill in the form and send a POST request to Django server
2. on Django, Django is going to enqueue a new task to RabbitMQ
3. Celery will pick up the task and monitor the progress and actually send the email

## Task 3: Heroku Redis deployment 
- deployment of Heroku Redis (message broker) to serve Celery (local development)

### Steps 
1. create a new Redis instance in Heroku 
2. configure the Django app for Redis

### Worker 
> Client --> Django --> Heroku Redis --> Celery 

