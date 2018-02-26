# Piiphole - [DEMO VIDEO](https://youtu.be/NHSAuooeCOk)
An Amazon Alexa skill that allows you peep who is at your door using Rekognition and a Raspberry Pi

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites

* Setup your Amazon Alexa and install the app on your phone

* Set up your Raspberry Pi 3 with an operating system

```
https://www.raspberrypi.org/documentation/installation/noobs.md
```

* Once you have your Raspberry Pi 3 setup, install the following:

```
sudo pip install flask
sudo pip install boto3
sudo pip install awscli
sudo apt-get install nodejs npm node-semver
sudo npm install localtunnel
```

### Installing

TODO

## Deployment

SSH into your Raspberry Pi 3 and run the following command

```
python alexa_server.py
```

This will start the server on your Raspberry Pi and going on piiphole.localtunnel.me will allow you to execute commands on the Pi

## Built With

### Hardware:
* [Amazon Echo Dot](https://www.amazon.ca/Echo-Dot-2nd-Generation-Black/dp/B07456NHZ7/ref=sr_1_1?ie=UTF8&qid=1519593290&sr=8-1&keywords=alexa+dot&dpID=41iz5Tw82IL&preST=_SY300_QL70_&dpSrc=srch)
* [Raspberry Pi 3](https://www.amazon.ca/Raspberry-Pi-RASPBERRYPI3-MODB-1GB-Model-Motherboard/dp/B01CD5VC92/ref=sr_1_3?ie=UTF8&qid=1519593310&sr=8-3&keywords=raspberry+pi+3&dpID=51Vt9f26ryL&preST=_SX300_QL70_&dpSrc=srch)
* [Raspberry Pi Camera Module V2](https://www.amazon.ca/Raspberry-Pi-Camera-Module-Megapixel/dp/B01ER2SKFS/ref=sr_1_1?s=electronics&ie=UTF8&qid=1519593328&sr=1-1&keywords=raspberry+pi+camera+module+v2&dpID=41oaX6czzQL&preST=_SY300_QL70_&dpSrc=srch)

### Software:
* [Amazon Rekognition](https://aws.amazon.com/rekognition/) - Used to detect and recognize faces capture with the Raspberry Pi camera
* [Amazon S3](https://aws.amazon.com/s3/) - Used to store the captured image uploaded from the Raspberry Pi
* [Amazon Alexa Skills Kit](https://developer.amazon.com/alexa-skills-kit) - Used to trigger the Echo dot for the Piiphole skill
* [Amazon Lambda](https://aws.amazon.com/lambda/) - Implementation of the skill
* [Flask](http://flask.pocoo.org/) - Used to setup a web server that the Raspberry Pi hosts to connect with Lambda
* [Boto3](https://github.com/boto/boto3) - Library to connect with Amazon Web Services
* [Localtunnel](https://localtunnel.github.io/www/) - Allows to interact with the Raspberry Pi web server on the home network
 
## Authors

* **Josh Vocal** - [joshvocal](https://github.com/joshvocal)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
