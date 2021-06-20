from flask import Flask, render_template, Response, flash
import boto3
from flask import request

app = Flask(__name__)

s3 = boto3.client('s3',
                  endpoint_url="YOUR-SERVER-ADDRESS-HERE",
                  aws_access_key_id="SERVER-ACCESS-KEY",
                  aws_secret_access_key="SERVER-SECRET-KEY",
                  verify=False
                  )

def getBuckets():
   response = s3.list_buckets()
   return response

@app.route("/newbucket/", methods=['POST'])
def create_new_bucket():   
   name = request.form['bkname']
   buckets = getBuckets()
   buckets = buckets['Buckets']
   print(buckets)
   s3.create_bucket(Bucket=name)
   buckets = getBuckets()
   return render_template(
        'main.html',
        buckets=buckets['Buckets'],
        bucketname=name)

@app.route("/delete/", methods=['POST'])
def delete_bucket():
   name = request.form['bucketname']
   response = s3.list_objects_v2(Bucket=name)
   if response['KeyCount'] == 0:
      s3.delete_bucket(Bucket=name)
      buckets = getBuckets()
      return render_template(
           'main.html',
           buckets=buckets['Buckets'])
   else:
      buckets = getBuckets()
      return render_template(
           'main.html',
           buckets=buckets['Buckets'], badDelete = True)


@app.route("/listobjects/", methods=['POST'])
def list_objects():
   name = request.form['bucketname']
   response = s3.list_objects_v2(Bucket=name)
   buckets = getBuckets()
   if response['KeyCount'] != 0:
      return render_template(
        'main.html',
        buckets=buckets['Buckets'], 
        objects=response['Contents'], 
        bucketname=name)
   else:
      return render_template(
      'main.html',
      buckets=buckets['Buckets'],
      bucketname=name)
        
@app.route("/deleteobject/", methods=['POST'])
def delete_object():
   name = request.form['bucketname']
   key = request.form['objectname']
   s3.delete_object(Bucket=name, Key=key)
   buckets = getBuckets()
   response = s3.list_objects_v2(Bucket=name)
   print(name)
   if response['KeyCount'] != 0:
      return render_template(
           'main.html',
           buckets=buckets['Buckets'],
           objects=response['Contents'],
           bucketname=name)
   else:
      return render_template(
         'main.html',
         buckets=buckets['Buckets'],
         bucketname=name)

@app.route("/uploadobject/", methods = ['GET', 'POST'])
def upload_object():
   name = request.form['bucketname']
   file = request.files["userfile"]
   if file.filename == "":
      return "Please select a file"
   if file :
      output = s3.upload_fileobj(file, name, file.filename, ExtraArgs={"ContentType": file.content_type})
      buckets = getBuckets()
      response = s3.list_objects_v2(Bucket=name)
      return render_template(
         'main.html',
         buckets=buckets['Buckets'],
         objects=response['Contents'],
         bucketname=name)

@app.route("/downloadobject/", methods=['POST'])
def download_object():
   name = request.form['bucketname']
   key = request.form['objectname']
   file = s3.get_object(Bucket=name, Key=key)
   buckets = getBuckets()
   response = s3.list_objects_v2(Bucket=name)
   return Response(
        file['Body'].read(),
        mimetype='text/plain',
        headers={"Content-Disposition": 'attachment;filename="%s"' %key}
    )

   
@app.route('/')
def home():
   buckets = getBuckets()
   return render_template(
        'main.html',
        buckets=buckets['Buckets'])

if __name__ == '__main__':
   # app.run() ## This is used to start an HTTP server
   
   # context = ('server.crt', 'server.key')
   # app.run(debug=True, ssl_context=context) ## This is used to start an HTTPS server