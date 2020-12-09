#!/usr/bin/env python3

from _token import token
import vk_api
import vk_api.bot_longpoll
import random


# group_id = 'mozgoyoga'
group_id = 124866462

class Bot:
    def __init__(self, group_id, token):
        self.group_id = group_id
        self.token = token

        self.vk = vk_api.VkApi(token=token)
        self.long_poller = vk_api.bot_longpoll.VkBotLongPoll(self.vk, self.group_id)

        self.api = self.vk.get_api()

    def run(self):
        for event in self.long_poller.listen():
            print('event', event)
            print('Get event')
            try:
                self.on_event(event)
            except Exception as err:
                print(err)

    def on_event(self, event):
        if event.type == vk_api.bot_longpoll.VkBotEventType.MESSAGE_NEW:
            self.api.messages.send(
                # message='Thx for your treatment - "' + event.object.message['text'] +'"',
                message='Thx for your treatment. What do you want? "' + event.object.message['text'] +'"',
                random_id = random.randint(0,2**20),
                peer_id=event.object.message['peer_id'],
            )
        else:
            print('can not do this', event.type)

if __name__ == '__main__':
    bot = Bot(group_id, token)
    bot.run()