# connect to atp using docker and python
Datos 1 

# Change this in the ora file
WALLET_LOCATION = (SOURCE = (METHOD = file) (METHOD_DATA = (DIRECTORY="/wallet")))
SSL_SERVER_DN_MATCH=yes

# Build de image 
sudo docker build --no-cache --force-rm=true -t atpython .

# Run it 

docker run \
-e DB_USER=$user \
-e DB_PASSWORD=$pass \
-e DB_CONNECTIONSTRING=$CONNECTIONSTRING \
atpython

# With ATP 

sudo docker run -it -p 3000:3000 -v ~/Wallet_DB202001151800:/wallet -e DB_USER=hr -e DB_PASSWORD=Danielhernandez1108 -e DB_CONNECTIONSTRING=db202001151800_high -e TNS_ADMIN=/wallet atpython

# Docker 
sudo docker stop $(sudo docker ps -a -q)
sudo docker rm $(sudo docker ps -a -q)

sudo docker rmi atpython

# Para verlo
http://3.132.215.60:3000/

# With PostgreSQL AWS RDS