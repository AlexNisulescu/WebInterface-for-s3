# :computer: Web Server using Flask and boto3 for S3 object storage

<a href="https://www.python.org/"><img src="https://img.shields.io/badge/language-Python-brightgreen"></a>
<a href="https://flask.palletsprojects.com/en/2.0.x/"><img src="https://img.shields.io/badge/Server-Flask-blue"></a>
<a href="https://boto3.amazonaws.com/v1/documentation/api/latest/index.html"><img src="https://img.shields.io/badge/AWS SDK-Boto3-yellow"></a>
<a href="#"><img src="https://img.shields.io/badge/Markup-HTML-orange"></a>
<a href="#"><img src="https://img.shields.io/badge/Style-CSS-blue"></a>

## Table of contents
 - [Introduction](#Introduction)
 - [Prerequisites](#Prerequisites)
 - [Application usage](#Application%20usage)

## Introduction
    This is an Web Server created in my spare time in order to offer an interface between the user
    and the S3 object storage.
    I hope that this will serve as an example for future developers trying to create any aplication
    that uses object storage for both private and hybrid cloud services

## Prerequisites
    In order to make this work, you need an S3 gateway object storage server running to connect to.
    I have tested it with MinIO, OpenIO and Ceph and it works just fine with all of them.
    You will alsi need to have Python3 installed (I have used 3.7.9) and both Flask and Boto3 
    installed (with pip).

 ## Application usage
    This app can be used to create your own cloud storage even if it's public, private or hybrid. 
    In order to start the server you need to remove the comment ("#") at line 124 if you plan to
    start the server as HTTP or lines 127 and 128 if you want to start it as HTTPS. For the last
    option you will also need a valid certificate and key.
