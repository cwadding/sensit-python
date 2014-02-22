# Get the value of a specific field within a feed
#
# topic_id - The key for the parent topic
# feed_id - The id of the parent feed
# id - The key of the specific field
class Data():

	def __init__(self, topic_id, feed_id, id, client):
		self.topic_id = topic_id
		self.feed_id = feed_id
		self.id = id
		self.client = client

	# Requires authorization of **read_any_data**, or **read_application_data**.
	# '/api/topics/:topic_id/feeds/:feed_id/data/:id' GET
	#
	def find(self, options = {}):
		body = options['query'] if 'query' in options else {}

		response = self.client.get('/api/topics/' + self.topic_id + '/feeds/' + self.feed_id + '/data/' + self.id + '', body, options)

		return response

	# Update a specific value of a field within a feed with the data passed in. Requires authorization of **read_any_data**, or **read_application_data**.
	# '/api/topics/:topic_id/feeds/:feed_id/data/:id' PUT
	#
	def update(self, options = {}):
		body = options['body'] if 'body' in options else {}

		response = self.client.put('/api/topics/' + self.topic_id + '/feeds/' + self.feed_id + '/data/' + self.id + '', body, options)

		return response

