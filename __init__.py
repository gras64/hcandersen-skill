from mycroft import MycroftSkill, intent_file_handler
from mycroft.messagebus.message import Message
from mycroft.util.parse import match_one
import time

class CommonStorytelling(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    def initialize(self):
        self.add_event('storytelling.response', self.handle_response)

    @intent_file_handler('storytelling.common.intent')
    def handle_storytelling_common(self, message):
        self.log.info('commonstorytelling is calles')
        if message.data.get("story") is None:
            response = self.get_response('which_story', num_retries=0)
            if response is None:
                return
        else:
            response = message.data.get("story")
            self.stories = []
            self.register = 0
            self.bus.emit(Message("storytelling", {'story': response}))
            time.sleep(3)
            stories = sorted(self.stories, reverse=True)
            self.log.info('choose ' + str(stories[0]))

    def handle_response(self, message):
        self.log.info('response gotten from ' + message.data.get('skill'))
        self.stories.append((str(message.data.get('confidence')),
                             message.data.get('skill'),
                             message.data.get('title')))


def create_skill():
    return CommonStorytelling()

