# A topic is root that data is attached to. It is the equivalent of a source in searchlight/solink and acts as a table which has columns(Fields) and rows(Feeds).
#
class Topic():

	def __init__(self, client):
		self.client = client

	# Requires authorization of **read_any_data**, or **read_application_data**.
	# '/topics' GET
	#
	def list(self, options = {}):
		body = options['query'] if 'query' in options else {}

		response = self.client.get('/topics', body, options)

		return response

	# Requires authorization of **read_any_data**, or **read_application_data**.
	# '/topics/:id' GET
	#
	def find(self, options = {}):
		body = options['query'] if 'query' in options else {}

		response = self.client.get('/topics/:id', body, options)

		return response

	# Requires authorization of **manage_any_data**, or **manage_application_data**.
	# '/topics' POST
	#
	# name - The name and id of the topic.
	def create(self, name, options = {}):
		body = options['body'] if 'body' in options else {}
		body['name'] = name

		response = self.client.post('/topics', body, options)

		return response

	# Requires authorization of **manage_any_data**, or **manage_application_data**.
	# '/topics/:id' PUT
	#
	# name - The name and id of the topic.
	def update(self, name, options = {}):
		body = options['body'] if 'body' in options else {}
		body['name'] = name

		response = self.client.put('/topics/:id', body, options)

		return response

	# Requires authorization of **manage_any_data**, or **manage_application_data**.
	# '/topics/:id' DELETE
	#
	def delete(self, options = {}):
		body = options['body'] if 'body' in options else {}

		response = self.client.delete('/topics/:id', body, options)

		return response

