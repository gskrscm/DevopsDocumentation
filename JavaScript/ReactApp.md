Installation of nodejs and Npm (Npm inbuilt with node)
---------------------------------------------------------
curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash -

sudo apt-get install -y nodejs

Check Version [nodejs (8 LTS and above) and npm]
------------------------------------------------
node --version

npm --version

Install create-react-app module 
--------------------------------
npm install -g create-react-app 

Create react app using the module
---------------------------------
create-react-app <folder_name>

Start React app
------------------
From <folder_name> <b>npm start</b> - to start react app (runs on localhost:3000)
