#Run
    python server.py

#DB
    OK

#dotenv
    ok

#jwt
    ok

#upload file
    ok

#cores
    ok
# salt key
    openssl rand -hex 32
    8663edef3ca737c9370ce741a96a506129995f4a0408bacdebe59bbf0875e7cf

# private key
    ssh-keygen -t rsa -b 4096 -m PEM -f private.key
# public key
    openssl rsa -in private.key -pubout -outform PEM -out public.key