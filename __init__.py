from mycroft import MycroftSkill, intent_file_handler


class CommonStorytelling(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('storytelling.common.intent')
    def handle_storytelling_common(self, message):
        story = message.data.get('story')

        self.speak_dialog('storytelling.common', data={
            'story': story
        })


def create_skill():
    return CommonStorytelling()

