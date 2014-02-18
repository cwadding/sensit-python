# Returns api instance to get auxilary information about Buffer useful when creating your app.
#
# topic_id - The key for the parent topic
# id - The id of the feed
class Feed():

	def __init__(self, topic_id, id, client):
		self.topic_id = topic_id
		self.id = id
		self.client = client

	# Returns a list of feeds for a given topic. Requires authorization of **read_any_data**, or **read_application_data**.
	# '/topics/:topic_id/feeds' GET
	#
	def list(self, options = {}):
		body = options['query'] if 'query' in options else {}

		response = self.client.get('/topics/' + self.topic_id + '/feeds', body, options)

		return response

	# Returns a specific feed for a topic. Requires authorization of **read_any_data**, or **read_application_data**.
	# '/topics/:topic_id/feeds/:id' GET
	#
	def find(self, options = {}):
		body = options['query'] if 'query' in options else {}

		response = self.client.get('/topics/' + self.topic_id + '/feeds/' + self.id + '', body, options)

		return response

	# Create a feed on a given topic. Requires authorization of **read_any_data**, or **read_application_data**.
	# '/topics/:topic_id/feeds' POST
	#
	# data - A hash of data to be stored
	def create(self, data, options = {}):
		body = options['body'] if 'body' in options else {}
		body['data'] = data

		response = self.client.post('/topics/' + self.topic_id + '/feeds', body, options)

		return response

	# Update an associated Feed to the Topic. Requires authorization of **read_any_data**, or **read_application_data**.
	# '/topics/:topic_id/feeds/:id' PUT
	#
	# data - A hash of data to be stored
	def update(self, data, options = {}):
		body = options['body'] if 'body' in options else {}
		body['data'] = data

		response = self.client.put('/topics/' + self.topic_id + '/feeds/' + self.id + '', body, options)

		return response

	# Deletes the desired feed. Requires authorization of **read_any_data**, or **read_application_data**.
	# '/topics/:topic_id/feeds/:id' DELETE
	#
	def delete(self, options = {}):
		body = options['body'] if 'body' in options else {}

		response = self.client.delete('/topics/' + self.topic_id + '/feeds/' + self.id + '', body, options)

		return response

