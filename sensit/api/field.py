# .
#
# topic_id - The key for the parent topic
# id - Username of the user
class Field():

	def __init__(self, topic_id, id, client):
		self.topic_id = topic_id
		self.id = id
		self.client = client

	# Get all the fields associated with a topic. Requires authorization of **read_any_data**, or **read_application_data**
	# '/topics/:topic_id/fields' GET
	#
	def list(self, options = {}):
		body = options['query'] if 'query' in options else {}

		response = self.client.get('/topics/' + self.topic_id + '/fields', body, options)

		return response

	# Get a Field of the associated a topic and Id. Requires authorization of **read_any_data**, or **read_application_data**
	# '/topics/:topic_id/fields/:id' GET
	#
	def find(self, options = {}):
		body = options['query'] if 'query' in options else {}

		response = self.client.get('/topics/' + self.topic_id + '/fields/' + self.id + '', body, options)

		return response

	# Adds a new field that feed data can be added too. Requires authorization of **manage_any_data**, or **manage_application_data**
	# '/topics/:topic_id/fields' POST
	#
	# name - The descriptive name of the field.
	# key - The name that the is used to identify the field in a feed
	def create(self, name, key, options = {}):
		body = options['body'] if 'body' in options else {}
		body['name'] = name
		body['key'] = key

		response = self.client.post('/topics/' + self.topic_id + '/fields', body, options)

		return response

	# Updates the Field data and makes the corresponding changes in the index. Requires authorization of **manage_any_data**, or **manage_application_data**
	# '/api/topics/:topic_id/fields/:id' PUT
	#
	# name - The descriptive name of the field.
	def update(self, name, options = {}):
		body = options['body'] if 'body' in options else {}
		body['name'] = name

		response = self.client.put('/api/topics/' + self.topic_id + '/fields/' + self.id + '', body, options)

		return response

	# Deletes a field and the feed data in that field. Requires authorization of **manage_any_data**, or **manage_application_data**
	# '/api/topics/:topic_id/fields/:id' DELETE
	#
	def delete(self, options = {}):
		body = options['body'] if 'body' in options else {}

		response = self.client.delete('/api/topics/' + self.topic_id + '/fields/' + self.id + '', body, options)

		return response

