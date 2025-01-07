# Comp2001CW2

About the project
This project is a micro service to manage the data within tables relating to the trails part of the larger app. The micro service is capible of CRUD operations for each table where appliable and user authentication.


Installation instructions (Must be on the university network either physically or via VPN)

Using Python
1. Download the project from the Github
2. Run app.py
3. Open a web browser
4. Enter the URL http://localhost:8000/
5. Press on the link or enter http://localhost:8000/api/ui/
6. Use the UI to run the CRUD procedures.



Using Docker 
1. Install Docker desktop
2. Start Docker
3. Run: docker pull harveymoth/comp2001cw2image
4. Run: docker run -p 8000:8000 harveymoth/comp2001cw2image
5. Open bowser and navigate to http://localhost:8000/
5. Press on the link or enter http://localhost:8000/api/ui/
6. Use the UI to run the CRUD procedures.
