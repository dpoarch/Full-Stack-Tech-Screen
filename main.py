from flask import *
from flask_cors import CORS
from json import dumps
import json, time, glob, os, os.path, wget, csv


app = Flask(__name__)

CORS(app)
cors = CORS(app, resources = {
		r"/*": {
			"origins": "*"
		}
	})

@app.route('/', methods=['GET'])
def home():
	data_set = {'response': 'Success', 'Message': 'GET Success HTTP/1.1 200 OK', 'time': time.time()}
	json_dump = json.dumps(data_set)

	return json_dump


@app.route('/images', methods=['GET'])
def images():
	result = []
	dir_path = os.path.dirname(os.path.realpath(__file__)).replace("\\", "/")
	image = glob.glob(dir_path+'/s3_storage/*.png')
	image_json = json.dumps(image)

	for images in image:
		remove_dir = images.replace(dir_path+'/s3_storage', '')
		filter_slash = remove_dir.replace('\\', '')

		result.append({'image_name': filter_slash})
		# data_set = {'data': result, 'msg': 'GET Success HTTP/1.1 200 OK', 'time': time.time()}
		# json_dump = json.dumps(result)

	return Response(dumps({
			'content': result
		}), mimetype='text/json')


@app.route('/metadata/', methods=['GET'])
def storage():
	result = []
	user_query = str(request.args.get('image_name'))

	dir_path = os.path.dirname(os.path.realpath(__file__)).replace("\\", "/")
	image = glob.glob(dir_path+'/s3_storage/*.png')
	data_set = {'response': 'Error', 'Message': 'GET Success HTTP/1.1 200 OK', 'time': time.time()}
	for images in image:

		if images.find(user_query) != -1:
			
			filename_path = images.replace('\\', '/')
			
			with open(dir_path+'/s3_storage/metadata.csv') as  csv_file:
				csv_reader = csv.reader(csv_file, delimiter='\t')

				next(csv_reader)

				for line in csv_reader:
					if line[0] == user_query:	
						result = {'image_name': line[0], 'Longitude': line[1], 'Latitude' : line[2], 'Altitude_asl': line[3], 'bearing': line[4], 'Pitch': line[5], 'Roll': line[6], 'image': line[7], 'exposure': line[8], 'hdop': line[9]}
						end_data = {'data': result}
					
		else:
			data_set = {'response': dir_path+'/s3_storage/metadata.csv', 'Message': 'GET Success HTTP/1.1 200 OK', 'time': time.time()}
			json_dump = json.dumps(data_set)


	json_dump = json.dumps(end_data)
	return Response(dumps({
			'content': result
		}), mimetype='text/json')



# Web Runs on port 'http://127.0.0.1:4847'
if __name__ == '__main__':
	app.run(port=4847)