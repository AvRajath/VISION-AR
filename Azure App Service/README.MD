You can use VSCode editor to deploy it to Azure App services. Once the APP is up and running you can use the link for REST calls from Unity App and also edit the ../RPI to accept the query from the App service.

This code creates a NodeJS server which serves the request from our Augmented reality APP. 

When an user is in context of a device(refer to this video(https://youtu.be/IuT9wtThUno)) and based on the device the users command is sent to this Node. Which servers as a cloud point for this project. 

Further the RPI gets the data from this point and makes the changes accordingly in the IoT infrastructure to control the IoT devices.