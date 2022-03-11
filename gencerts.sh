# Update the apt package index and install packages to allow apt to use a repository over HTTPS
sudo apt-get update
sudo apt-get install ca-certificates curl gnupg lsb-release

# Add Docker’s official GPG key
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

# set up the stable repository
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Update the apt package index, and install the latest version of Docker Engine and containerd
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io

#open ssl configuration scripts
openssl req -newkey rsa:2048 -sha256 -nodes -keyout priv.key -x509 -days 365 -out pub.pem -subj "/C=US/ST=New York/L=Brooklyn/O=Example Brooklyn Company/CN=20.223.203.100"

curl -F "url=" https://api.telegram.org/bot382694174:AAHZeoMmAJQ6C5oLQfoNax11deTbSC2gKvA/setWebhook

curl -F "url=https://20.223.203.100/bot/" -F "certificate=@cert.pem" https://api.telegram.org/bot382694174:AAHZeoMmAJQ6C5oLQfoNax11deTbSC2gKvA/setWebhook