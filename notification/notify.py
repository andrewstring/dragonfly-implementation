import gi
# specify notify version before import
gi.require_version('Notify', '0.7')
from gi.repository import Notify

class Notification():

    def __init__(self, name, summaries):
        self.is_initialized = Notify.init(name)
        self.notifications = self.create_notifications(summaries)

    def create_notifications(self, summaries):
        assert type(summaries) is dict, 'Summaries must be a dictionary of summaries'
        notification_dict = {}
        for key, value in summaries.items():
            notification_dict[key] = Notify.Notification.new(value, icon='./img/logo.png')
        return notification_dict


if __name__ == '__main__':
    notifier = Notification()
    notifier.emit('Test')