# Yakei
Python service monitor.
* Right now i'm being lazy and putting notes here. Will use Sphinx for final documentation.

## Configuration 
Configuration files are pretty simple. They really don't have any requirements. You can space as much as you want or as little and put as many new lines as you feel would make you happy. The only requirements are this general format. 

### Comments
Any line starting with a * is a comment.
Example: ```* This is a comment. I'll be ignored by the parser.```

### The Domain Block
There should be one ```<Domain>``` block. Inside this block should be some resolvable address in the form ```address:port``` as an attribute.
Examples:
* ```<Domain localhost>```
* ```<Domain localhost:80>```
* ```<Domain http://www.abc.com>```

### The Service Block
Inside the ```<Domain>``` block there should be several ```<Service>``` blocks. Service blocks tell the monitoring which websites, processes and APIs are related to the specified domain. For instance, you could give the domain of www.abc.com and then have an API service, website and 2 services. When reporting on the status of the domain, it will include references to all 4 services.
Service blocks can be of three types. Website, API or Process. Each has slightly different options.
#### Websites
Websites only have 3 options that need to be defined.
* Type
* Load
* Poll
* Notification

Type defines what type of definition this service is. In the case of a website type would be Website.

Load defines what path should be requested. This is a relative path. This could be your home page, it could be a / to indicate the root index or it could be a specific page. In any case, it's whatever page you want Yakei to attemp to load as a connection test. Maybe you built a small html file for testing purposes and want to use that to minimize load.

Poll defines the interval between checks in seconds. Every Poll seconds the program will check if the service is online. For a website, online means that the page responds with Status Code 200. If we receive a Status Code 301 or 302 we will attempt to load that page instead. If the page specified by the redirect returns 200 then we define it as online. Anything else is considered offline.
 
Notification defines an email address to send offline warnings to. If you don't want any omit this attribute.

### API
APIs have a couple more options to be defined than Websites.
* Type
* Endpoint
* AltLocation
* Poll
* Notification
* DataType
* Expected

Type is the same as it is for a website, but this time we list API.

Endpoint defines the path that the program should request data from. This is a relative path, it is added to the domain as specified. This is followed unless you have defined...
  
AltLocation allows you to specific a second domain used for the API. Sometimes an API lives away from the domain specified in the domain block. If that's so, then you should list the path here. So if your domain were at https://api.abc.com/ then you would put https://api.abc.com

Poll defines the interval between checks in seconds.

Notification defines an email address to send warnings to. APIs are defined as offline if they don't return the expected data, don't return status code 200 or don't return valid data for the type specified.

DataType defines what kind of response we should expect from your API. This could be Json, JsonP or XML.

Expected defines what should be returned on the call we made. If you wrote a specific API endpoint for status that returns a specific value for online put it here. You can also put any here, but in that case Yakei will only check for status code 200 and valid Json, JsonP or XML.

### Process
Processes have a list like websites with one difference.
* Type
* Name
* Poll
* Notification

Type in this case would become Process.

Name is the name of the process. Hopefully this is unique. If you know there is more than one process running and want to provide a PID then put it here. Yakei assumes that any Name child made entirely of numbers is actually a PID.

Poll and Notification do the same thing they've done in the last two definitions.