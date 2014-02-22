# Publications are stored actions which are taken when a feed is created, updated, deleted, or there is a matching percolator query.
#
# topic_id - The key for the parent topic
# id - The identifier of the publication
class Publication():

	def __init__(self, topic_id, id, client):
		self.topic_id = topic_id
		self.id = id
		self.client = client

	# Get all publications for the associated Topic. Requires authorization of **read_any_publications**, or **read_application_publications**.
	# '/api/topics/:topic_id/publications' GET
	#
	def list(self, options = {}):
		body = options['query'] if 'query' in options else {}

		response = self.client.get('/api/topics/' + self.topic_id + '/publications', body, options)

		return response

	# Retrieve a specific publication on the associated topic by Id. Requires authorization of **read_any_publications**, or **read_application_publications**.
	# '/api/topics/:topic_id/publications/:id' GET
	#
	def find(self, options = {}):
		body = options['query'] if 'query' in options else {}

		response = self.client.get('/api/topics/' + self.topic_id + '/publications/' + self.id + '', body, options)

		return response

	# Create a new publication on the associated Topic which can be easily retrieved later using an id. Requires authorization of **manage_any_publications**, or **manage_application_publications**.
	# '/api/topics/:topic_id/publications' POST
	#
	# publication - A Hash containing `host`:The ip address or host of the connection(required).`protocol`:the protocol to communicate over (http, tcp, udp, mqtt) (required)`port`:The port of the connection.
	def create(self, publication, options = {}):
		body = options['body'] if 'body' in options else {}
		body['publication'] = publication

		response = self.client.post('/api/topics/' + self.topic_id + '/publications', body, options)

		return response

	# Update a publication. Requires authorization of **manage_any_publications**, or **manage_application_publications**.
	# '/api/topics/:topic_id/publications/:id' PUT
	#
	# publication - A Hash containing `host`:The ip address or host of the connection(required).`protocol`:the protocol to communicate over (http, tcp, udp, mqtt) (required)`port`:The port of the connection.
	def update(self, publication, options = {}):
		body = options['body'] if 'body' in options else {}
		body['publication'] = publication

		response = self.client.put('/api/topics/' + self.topic_id + '/publications/' + self.id + '', body, options)

		return response

	# Remove a saved publication on the associated Topic by Id. Requires authorization of **manage_any_publications**, or **manage_application_publications**.
	# '/api/topics/:topic_id/publications/:id' DELETE
	#
	def delete(self, options = {}):
		body = options['body'] if 'body' in options else {}

		response = self.client.delete('/api/topics/' + self.topic_id + '/publications/' + self.id + '', body, options)

		return response

