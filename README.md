# Piiphole
An Amazon Alexa skill that allows you peep who is at your door using Rekognition and a Raspberry Pi

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites

What things you need to install the software and how to install them

```
Give examples
```

### Installing

A step by step series of examples that tell you have to get a development env running

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

### Hardware:
* [Amazon Echo Dot](https://www.amazon.ca/Echo-Dot-2nd-Generation-Black/dp/B07456NHZ7/ref=sr_1_1?ie=UTF8&qid=1519593290&sr=8-1&keywords=alexa+dot&dpID=41iz5Tw82IL&preST=_SY300_QL70_&dpSrc=srch)
* [Raspberry Pi 3](https://www.amazon.ca/Raspberry-Pi-RASPBERRYPI3-MODB-1GB-Model-Motherboard/dp/B01CD5VC92/ref=sr_1_3?ie=UTF8&qid=1519593310&sr=8-3&keywords=raspberry+pi+3&dpID=51Vt9f26ryL&preST=_SX300_QL70_&dpSrc=srch)
* [Raspberry Pi Camera Module V2](https://www.amazon.ca/Raspberry-Pi-Camera-Module-Megapixel/dp/B01ER2SKFS/ref=sr_1_1?s=electronics&ie=UTF8&qid=1519593328&sr=1-1&keywords=raspberry+pi+camera+module+v2&dpID=41oaX6czzQL&preST=_SY300_QL70_&dpSrc=srch)

### Software:
* [Amazon Rekognition](https://aws.amazon.com/rekognition/) - Used to detect and recognize faces capture with the raspberry pi camera
* [Amazon S3](https://aws.amazon.com/s3/) - Used to store the captured image uploaded from the raspberry pi
* [Amazon Alexa Skills Kit](https://developer.amazon.com/alexa-skills-kit) - Used to trigger the Echo dot for the Piiphole skill
* [Amazon Lambda](https://aws.amazon.com/lambda/) - Implementation of the skill
* [Flask](http://flask.pocoo.org/) - Used to setup a web server that the raspberry pi hosts to connect with Lambda
* [Boto3](https://github.com/boto/boto3) - Library to connect with Amazon Web Services
* [Localtunnel](https://localtunnel.github.io/www/) - Allows to interact with the raspberry pi web server on the home network
 
## Authors

* **Josh Vocal** - [joshvocal](https://github.com/joshvocal)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
