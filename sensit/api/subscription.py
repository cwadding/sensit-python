# Subscriptions allows feed data to imported using a socket rather than just using the Feed REST API. By creating a subscription sensit will start to listen for feed data being imported using the specified `host` and while using the topic name as the `channel` name.
#
# id - The identifier for the subscription
class Subscription():

	def __init__(self, id, client):
		self.id = id
		self.client = client

	# Get the list of all subscriptions for importing feed data to the associated topics. Requires authorization of **read_any_subscriptions**, or **read_application_subscriptions**.
	# '/subscriptions' GET
	#
	def list(self, options = {}):
		body = options['query'] if 'query' in options else {}

		response = self.client.get('/subscriptions', body, options)

		return response

	# Get the information of a specific subscription. Requires authorization of **read_any_subscriptions**, or **read_application_subscriptions**.
	# '/subscriptions/:id' GET
	#
	def find(self, options = {}):
		body = options['query'] if 'query' in options else {}

		response = self.client.get('/subscriptions/' + self.id + '', body, options)

		return response

	# Create a subscription which will connect to the server and listen for feed data for any of the associated topics. Requires authorization of **manage_any_subscriptions**, or **manage_application_subscriptions**.
	# '/subscriptions' POST
	#
	# name - The channel or name to identify the subscription.
	# host - The ip address or host of the connection
	# protocol - the protocol to comminivate over
	def create(self, name, host, protocol, options = {}):
		body = options['body'] if 'body' in options else {}
		body['name'] = name
		body['host'] = host
		body['protocol'] = protocol

		response = self.client.post('/subscriptions', body, options)

		return response

	# Returns an object with the current configuration that Buffer is using, including supported services, their icons and the varying limits of character and schedules.  Requires authorization of **manage_any_subscriptions**, or **manage_application_subscriptions**.
	# '/subscriptions/:id' PUT
	#
	# name - The channel or name to identify the subscription.
	# host - The ip address or host of the connection
	# protocol - the protocol to comminivate over
	def update(self, name, host, protocol, options = {}):
		body = options['body'] if 'body' in options else {}
		body['name'] = name
		body['host'] = host
		body['protocol'] = protocol

		response = self.client.put('/subscriptions/' + self.id + '', body, options)

		return response

	# Delete the subscription and stop listening for feed data for the associated topics. Requires authorization of **manage_any_subscriptions**, or **manage_application_subscriptions**.
	# '/subscriptions/:id' DELETE
	#
	def delete(self, options = {}):
		body = options['body'] if 'body' in options else {}

		response = self.client.delete('/subscriptions/' + self.id + '', body, options)

		return response

