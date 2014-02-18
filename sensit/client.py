from .http_client import HttpClient

# Assign all the api classes
from .api.user import User
from .api.topic import Topic
from .api.feed import Feed
from .api.data import Data
from .api.percolator import Percolator
from .api.report import Report
from .api.subscription import Subscription
from .api.field import Field

class Client():

	def __init__(self, auth = {}, options = {}):
		self.http_client = HttpClient(auth, options)

	# <no value>
	#
	def user(self):
		return User(self.http_client)

	# A topic is root that data is attached to. It is the equivalent of a source in searchlight/solink and acts as a table which has columns(Fields) and rows(Feeds).
	#
	def topic(self):
		return Topic(self.http_client)

	# Returns api instance to get auxilary information about Buffer useful when creating your app.
	#
	# topic_id - The key for the parent topic
	# id - The id of the feed
	def feed(self, topic_id, id):
		return Feed(topic_id, id, self.http_client)

	# Get the value of a specific field within a feed
	#
	# topic_id - The key for the parent topic
	# feed_id - The id of the parent feed
	# id - The key of the specific field
	def data(self, topic_id, feed_id, id):
		return Data(topic_id, feed_id, id, self.http_client)

	# A **Percolator** is a reverse query much like a match rule which is run whenever a new feed is added. These can be used to create alerts by causing the sensit to publish the feed that was just added. A percolator query is defined by a `name` and and valid `query` according to the according the the [elasticsearch Query DSL](http://www.elasticsearch.org/guide/en/elasticsearch/reference/current/query-dsl.html).  For more information about Percolator queries please refer to the [elasticsearch percolator documentation](http://www.elasticsearch.org/guide/en/elasticsearch/reference/current/search-percolate.html).
	#
	# topic_id - The key for the parent topic
	# id - The name of the percolator query
	def percolator(self, topic_id, id):
		return Percolator(topic_id, id, self.http_client)

	# Reports are stored filter and facet queries on the **Feed** data. A report is a assigned a `name` and the `query` is any elasticsearch query which filters only the desired data for the facets (See the [elasticsearch Query DSL](http://www.elasticsearch.org/guide/en/elasticsearch/reference/current/query-dsl-queries.html) for valid queries). A report can have many `facets` with each facet is referred to by a user defined `name`. Valid `type`'s of facet include **terms**, **range**, **histogram**, **filter**, **statistical**, **query**, **terms_stats**, or **geo_distance**. The `query` within a facet defines the field counts or statistics which the data is calculated over. See the [elasticsearch facet dsl](http://www.elasticsearch.org/guide/en/elasticsearch/reference/current/search-facets.html) for information about the various facet types and valid query fields.
	#
	# topic_id - The key for the parent topic
	# id - The identifier of the report
	def report(self, topic_id, id):
		return Report(topic_id, id, self.http_client)

	# Subscriptions allows feed data to imported using a socket rather than just using the Feed REST API. By creating a subscription sensit will start to listen for feed data being imported using the specified `host` and while using the topic name as the `channel` name.
	#
	# id - The identifier for the subscription
	def subscription(self, id):
		return Subscription(id, self.http_client)

	# .
	#
	# topic_id - The key for the parent topic
	# id - Username of the user
	def field(self, topic_id, id):
		return Field(topic_id, id, self.http_client)

