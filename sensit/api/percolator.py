# A **Percolator** is a reverse query much like a match rule which is run whenever a new feed is added. These can be used to create alerts by causing the sensit to publish the feed that was just added. A percolator query is defined by a `name` and and valid `query` according to the according the the [elasticsearch Query DSL](http://www.elasticsearch.org/guide/en/elasticsearch/reference/current/query-dsl.html).  For more information about Percolator queries please refer to the [elasticsearch percolator documentation](http://www.elasticsearch.org/guide/en/elasticsearch/reference/current/search-percolate.html).
#
# topic_id - The key for the parent topic
# id - The name of the percolator query
class Percolator():

	def __init__(self, topic_id, id, client):
		self.topic_id = topic_id
		self.id = id
		self.client = client

	# Returns a list or percolators for a given topic. Requires authorization of **read_any_percolators**, or **read_application_percolators**.
	# '/api/topics/:topic_id/percolators' GET
	#
	def list(self, options = {}):
		body = options['query'] if 'query' in options else {}

		response = self.client.get('/api/topics/' + self.topic_id + '/percolators', body, options)

		return response

	# Return a specific percolator of the associated Topic by Id. Requires authorization of **read_any_percolators**, or **read_application_percolators**.
	# '/api/topics/:topic_id/percolators/:id' GET
	#
	def find(self, options = {}):
		body = options['query'] if 'query' in options else {}

		response = self.client.get('/api/topics/' + self.topic_id + '/percolators/' + self.id + '', body, options)

		return response

	# Create a percolator on the associated Topic with the specified name and query. Requires authorization of **manage_any_percolators**, or **manage_application_percolators**.
	# '/api/topics/:topic_id/percolators' POST
	#
	# percolator - A Hash containing `name`: The name of the percolator(required).`query`: The query hash according to the according the the [elasticsearch Query DSL](http://www.elasticsearch.org/guide/en/elasticsearch/reference/current/query-dsl.html)
	def create(self, percolator, options = {}):
		body = options['body'] if 'body' in options else {}
		body['percolator'] = percolator

		response = self.client.post('/api/topics/' + self.topic_id + '/percolators', body, options)

		return response

	# Update the query for a specific percolator. Requires authorization of **manage_any_percolators**, or **manage_application_percolators**.
	# '/api/topics/:topic_id/percolators/:id' PUT
	#
	# percolator - A Hash containing the `query` hash according to the according the the [elasticsearch Query DSL](http://www.elasticsearch.org/guide/en/elasticsearch/reference/current/query-dsl.html)
	def update(self, percolator, options = {}):
		body = options['body'] if 'body' in options else {}
		body['percolator'] = percolator

		response = self.client.put('/api/topics/' + self.topic_id + '/percolators/' + self.id + '', body, options)

		return response

	# Delete a percolator on the associated topic. Requires authorization of **manage_any_percolators**, or **manage_application_percolators**.
	# '/api/topics/:topic_id/percolators/:id' DELETE
	#
	def delete(self, options = {}):
		body = options['body'] if 'body' in options else {}

		response = self.client.delete('/api/topics/' + self.topic_id + '/percolators/' + self.id + '', body, options)

		return response

