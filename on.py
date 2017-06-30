from pubnub import Pubnub

pubnub = Pubnub(publish_key="pub-c-e7f7f579-146d-48f8-adec-3f38ce14b0e9", subscribe_key="sub-c-e240c026-5c1a-11e7-8944-0619f8945a4f")

print (pubnub.publish(channel='my_channel', message="on"))