# :computer: Web Server using Flask and boto3 for S3 object storage

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
