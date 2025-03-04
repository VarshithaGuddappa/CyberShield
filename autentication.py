from pymongo import MongoClient
import getpass
import os

def authenticate_user():
    try:
        # Prompt the user for email and password
        email = input("Enter your email (must be @bnmit.in): ")
        password = getpass.getpass("Enter your password: ")

        # Check if the email ends with @bnmit.in
        if not email.endswith("@bnmit.in"):
            print("Invalid email domain. Please use a valid bnmit.in email.")
            return False

        # Connect to the MongoDB database
        client = MongoClient("mongodb+srv://gudddenuf:welcome123@cluster0.ifxas.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
        db = client['tiger']
        collection = db['credentials']

        # Check if the email exists in the database and if the password matches
        user = collection.find_one({"email": email})
        if user and user['password'] == password:
            print("Authentication successful!")
            
            # Create the auth_done.txt file to mark the user as authenticated
            with open("auth_done.txt", "w") as f:
                f.write("Authenticated")
            return True
        else:
            print("Incorrect email or password. Access denied.")
            return False
    except Exception as e:
        print(f"Error during authentication: {e}")
        return False

# Run the authentication if not already done
def run_authentication():
    if not os.path.exists("auth_done.txt"):  # Only ask for authentication if not authenticated before
        if not authenticate_user():
            print("Authentication failed. Exiting program.")
            exit(1)
    else:
        print("Already authenticated. Skipping authentication.")

# Call the authentication function when setting up
run_authentication()
