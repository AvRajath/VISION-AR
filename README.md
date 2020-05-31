This project contains 2 components one which is a full end to end working APP built using unity. And the 2nd Part is the Smart Glasses which is just a futuristic picture of what this application is capable of. 

Azure App service was deployed to Azure cloud using VSCODE editor. The NodeJS code in avaliable in Azure APP service folder.

The unity app which is the main focus of this Hack, The code and the packages along with the C# can be found in Unity Packages Zip file.
Check out the Readme inside the folder to know more.

The IoT setup is a simple connection to relay(a swithching device). And code for executing it on the RPI can be found in IoT setup folder.

Smart glasses is an experimental folder where in the hardware is complete but more of software integration would show the futuristic implementation of this product. An addition to the app to show some possible hacks.

Unity Package:
================

Unity Version used : 2018.4.15.f1(please use the same version of unity as you may face a lot of confilicts in other versions)

The package consists of a complete Unity scene which has the object details on the image targets. We have used Marker based image recognition. 

Steps to build:
=================

Disclaimer: This project has multiple dependencies such as it requires an IoT setup and physical access to those real world IoT objects. You can refer to this video to see what is happening in actual(https://youtu.be/IuT9wtThUno). 

Refer to IoT setup folder for instructions on how to set up code on RPI. Physical setup of RPI to devices can be found online.

An Very high level intro to how a setup can be recreated: 

* Unity with Vuforia library is necessary.

* Upload an image to https://developer.vuforia.com/vui/develop/databases of your choice. After uploading the image. Import the package to the unity assets. 

* Build a new object with a canvas attached to it. And add buttons to canvas which are named according to the operations that can be performed on the object.

* To make these buttons intractible we need to attach scripts which do some task based on the Device identified. This can be done using the test,test1,test2.cs scripts which are present in the assests folder. These scripts basically make an API call to the cloud(Azure App service) to update particular data on to cloud. 

* Adding these scripts to the canvas would bring some functionality to these buttons. These buttons would then when interacted would trigger data onto our server.

* This data received by our server will be processed for further use by the IoT infrastructure.

* Generate an App from this setup and publish it to your device.

