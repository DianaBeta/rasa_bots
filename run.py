from rasa_core.channels.slack import SlackInput
from rasa_core.agent import Agent
from rasa_core.interpreter import RegexInterpreter
from rasa_core.interpreter import RasaNLUInterpreter

nlu_interpreter = RasaNLUInterpreter('./models/current/nlu')
agent = Agent.load('./models/dialogue', interpreter = nlu_interpreter)

input_channel = SlackInput(
        slack_token="xoxb-615288492194-628946111974-NZQwORTSlw2e3LHRKGEruUtf"
        # this is the `bot_user_o_auth_access_token`
        #slack_channel="YOUR_SLACK_CHANNEL"
            # the name of your channel to which the bot posts (optional)
    )

# set serve_forever=True if you want to keep the server running
s = agent.handle_channels([input_channel], 5004, serve_forever=True)
