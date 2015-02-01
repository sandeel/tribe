#!/bin/bash
http POST http://localhost:8000/api/users/  email=tester@http.com password=password

http -a tester@http.com:password POST http://localhost:8000/api/tribes/  name="httpie test tribe"
http -a tester@http.com:password POST http://localhost:8000/api/invited_users/  email="tester2@http.com"

http POST http://localhost:8000/api/users/  email=tester2@http.com password=password


http -a tester2@http.com:password POST http://localhost:8000/api/tasks/ name="new Task"

