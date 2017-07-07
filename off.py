from pubnub import Pubnub

pubnub = Pubnub(publish_key="publish_key", subscribe_key="subcribe_key")

print (pubnub.publish(channel='my_channel', message="off"))
