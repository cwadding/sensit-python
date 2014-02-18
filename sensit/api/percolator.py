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
	# '/topics/:topic_id/percolators' GET
	#
	def list(self, options = {}):
		body = options['query'] if 'query' in options else {}

		response = self.client.get('/topics/' + self.topic_id + '/percolators', body, options)

		return response

	# Return a specific percolator of the associated Topic by Id. Requires authorization of **read_any_percolators**, or **read_application_percolators**.
	# '/topics/:topic_id/percolators/:id' GET
	#
	def find(self, options = {}):
		body = options['query'] if 'query' in options else {}

		response = self.client.get('/topics/' + self.topic_id + '/percolators/' + self.id + '', body, options)

		return response

	# Create a percolator on the associated Topic with the specified name and query. Requires authorization of **manage_any_percolators**, or **manage_application_percolators**.
	# '/topics/:topic_id/percolators' POST
	#
	# name - The time zone of the time. Defaults to UTC
	# query - A hash of data to be stored
	def create(self, name, query, options = {}):
		body = options['body'] if 'body' in options else {}
		body['name'] = name
		body['query'] = query

		response = self.client.post('/topics/' + self.topic_id + '/percolators', body, options)

		return response

	# Update the query for a specific percolator. Requires authorization of **manage_any_percolators**, or **manage_application_percolators**.
	# '/topics/:topic_id/percolators/:id' PUT
	#
	# query - A hash of data to be stored
	def update(self, query, options = {}):
		body = options['body'] if 'body' in options else {}
		body['query'] = query

		response = self.client.put('/topics/' + self.topic_id + '/percolators/' + self.id + '', body, options)

		return response

	# Delete a percolator on the associated topic. Requires authorization of **manage_any_percolators**, or **manage_application_percolators**.
	# '/topics/:topic_id/percolators/:id' DELETE
	#
	def delete(self, options = {}):
		body = options['body'] if 'body' in options else {}

		response = self.client.delete('/topics/' + self.topic_id + '/percolators/' + self.id + '', body, options)

		return response

