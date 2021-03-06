# A topic is root that data is attached to. It is the equivalent of a source in searchlight/solink and acts as a table which has columns(Fields) and rows(Feeds).
#
class Topic():

	def __init__(self, client):
		self.client = client

	# Requires authorization of **read_any_data**, or **read_application_data**.
	# '/api/topics' GET
	#
	def list(self, options = {}):
		body = options['query'] if 'query' in options else {}

		response = self.client.get('/api/topics', body, options)

		return response

	# Requires authorization of **read_any_data**, or **read_application_data**.
	# '/api/topics/:id' GET
	#
	def find(self, options = {}):
		body = options['query'] if 'query' in options else {}

		response = self.client.get('/api/topics/:id', body, options)

		return response

	# Requires authorization of **manage_any_data**, or **manage_application_data**.
	# '/api/topics' POST
	#
	# topic - A hash containing the name/id of the topic (required) and a description of the topic.
	def create(self, topic, options = {}):
		body = options['body'] if 'body' in options else {}
		body['topic'] = topic

		response = self.client.post('/api/topics', body, options)

		return response

	# Requires authorization of **manage_any_data**, or **manage_application_data**.
	# '/api/topics/:id' PUT
	#
	# topic - A hash containing the name/id of the topic (required) and a description of the topic.
	def update(self, topic, options = {}):
		body = options['body'] if 'body' in options else {}
		body['topic'] = topic

		response = self.client.put('/api/topics/:id', body, options)

		return response

	# Requires authorization of **manage_any_data**, or **manage_application_data**.
	# '/api/topics/:id' DELETE
	#
	def delete(self, options = {}):
		body = options['body'] if 'body' in options else {}

		response = self.client.delete('/api/topics/:id', body, options)

		return response

