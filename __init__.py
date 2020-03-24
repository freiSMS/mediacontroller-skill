from mycroft import MycroftSkill, intent_file_handler


class Mediacontroller(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('mediacontroller.intent')
    def handle_mediacontroller(self, message):
        self.speak_dialog('mediacontroller')


def create_skill():
    return Mediacontroller()

