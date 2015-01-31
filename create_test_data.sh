#!/bin/bash
http -a djf@linux.com:password POST http://localhost:8000/api/users/  email=tester@http.com password=password
http -a tester@http.com:password POST http://localhost:8000/api/tribes/  name="httpie test tribe"
