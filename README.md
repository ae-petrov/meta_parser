# Open Graph processing

This web-service helps you to collect open graph tags from required URL. It includes Open Graph, Facebook, Twitter, Mobile, VK tags. Tags list may be expanded via settings.py

## Deployed project available on
[https://open-graph.gq](https://open-graph.gq)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

You need python 3.8 installed.

### Installation

A step by step series of examples that tell you how to get a service running.

#### Setup

Change or make dir where you want project will be cloned to.
```
cd <your_project_dir>
```

Clone repository
```
git clone https://github.com/ae-petrov/meta_parser.git
```

Now you should have following structure. Project is in meta_parser directory.
```
...<your_project_dir>/meta_parser
```

Project uses virtual environment. To install it change dir to project dir.
```
cd meta_parser
```

Make sure you are inside meta_parser directory by this comand.
```
pwd
```

#### Create and activate virtual environment

Now we are ready to create virtual environment. Following comand will create *venv* folder.
```
python -m venv venv
```

Activate your venv. After activation you should have (venv) sign before comand line. Check it out.
In case Windows user
```
source venv/scripts/activate
```

In case Linux user
```
source venv/bin/activate
```

#### Install

Install all necessary requirements using this comand. 
*Note that venv should be activated before. Else all references will be installed globaly*
```
pip install -r requirements.txt
```

### Launching web service

Now we are ready to launch our server.
```
python webservice.py
```

Server is launched on 127.0.0.1:8080. Type it in your browser and use service. 
Or you can use API via Postman or any other client.
API usage is described below.

## Deployment

When you launching webservice.py server is already running on your localhost. To make it public it is recommended to use Nginx for example.

## API Usage
Service is already deployed. You can use API in your app.
GET requests only are allowed.
Just make GET requests from your app following this pattern:
*https://open-graph.gq/api/?url=<URL_YOU_WANT_TO_PROCESS>*
Service will return JSON response in following format:
```
{
    "URL_YOU_WANT_TO_PROCESS": {
        "Open Graph": {<tags>},
        "Facebook": {<tags>},
        "Twitter": {<tags>},
        "Mobile": {<tags>},
        "Vkontakt": {<tags>}
    }
}
```

## Built With

* [CherryPy](https://cherrypy.org/) - Server side and API
* [Bootstrap4](https://getbootstrap.com/) - Frontend endpoints

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/ae-petrov/) for details on our code of conduct, and the process for submitting pull requests to us.

## Authors

* **Alexey Petrov** - *Initial work* - [ae-petrov](https://github.com/ae-petrov)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
