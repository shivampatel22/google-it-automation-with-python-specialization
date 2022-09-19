Web Applications and Services
=============================
Web Applications and Services (sub)
-----------------------------------

A web application is an application that you interact with over HTTP. Most of the time when you’re using a website on the Internet, you’re interacting with a web application.

A web service is a web applications that have an API.

Instead of browsing to a web page to type and click around, you can use your program to send a message known as an API call to the web service's API endpoints.

Data Serialization
-------------------

Data serialization is the process of taking an in-memory data structure, like a Python object, and turning it into something that can be stored on disk or transmitted across a network. (ex: CSV file)

Turning the serialized object back into an in-memory object is called deserialization.

A web service's API endpoint can take messages in a specific format, containing specific data such as serialized data.

Data Serialization Formats
--------------------------
There are different data serialization formats:

- JavaScript Object Notation (JSON)
- Yet Another Markup Language (YAML)
- Python pickle
- Protocol Buffers
- eXtensible Markup Language (XML)
- JSON (JavaScript Object Notation) is the serialization format that is used widely today in IT.

More About JSON
---------------

Characateristics of JSON incliudes:

- JSON is human-readable
- JSON elements are always comma-delimited

JSON supports a few elements of different data types such as:

- Strings
- Numbers
- Objects
- Key-Value pair
- Arrays - arrays can contain strings, numbers, objects, or other arrays

Python Requests
---------------
The Python Requests Library
HTTP (HyperText Transfer Protocol) is the protocol of the world-wide web

Documentaton - https://pypi.org/project/requests/