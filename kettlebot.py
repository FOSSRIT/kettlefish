#    kettlefish is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    kettlefish is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with kettlefish.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import print_function
import re

from twisted.words.protocols.irc import IRCClient
from twisted.internet.protocol import ReconnectingClientFactory
from twisted.internet import reactor

from kettlefish import translate_remyspeak

class KettleBot(IRCClient):
    bot_name = "kettlefish"
    channel = "#rit-foss"
    versionNum = 1
    sourceURL = "http://github.com/oddshocks/kettlefish"
    lineRate = 1

    def signedOn(self):
        """Called when bot has succesfully signed on to server."""
        self.join(self.factory.channel)
        self.factory.add_bot(self)

    def joined(self, channel):
        """This will get called when the bot joins the channel."""
        print("Joined %s" % channel)

    def left(self, channel):
        """This will get called when the bot leaves the channel."""
        print("Left %s" % channel)

    def privmsg(self, user, channel, msg):
        """This will get called when the bot receives a message."""
        user = user.split('!', 1)[0]

        if user == 'decause':
            translated = translate_remyspeak(msg)
            display = re.sub(r'(\+\+)|(--)', '', translated)
            if not msg.lower() == translated.lower():
                self.msg(channel, 'What {} meant to say was: {}'.format(
                                    user, display))


class KettleBotFactory(ReconnectingClientFactory):
    active_bot = None

    def __init__(self, protocol=KettleBot):
        self.protocol = protocol
        self.channel = protocol.channel
        IRCClient.nickname = protocol.bot_name
        IRCClient.realname = protocol.bot_name

    def add_bot(self, bot):
        self.active_bot = bot


if __name__ == '__main__':
    # create factory protocol and application
    f = KettleBotFactory()

    # connect factory to this host and port
    reactor.connectTCP("irc.freenode.net", 6667, f)

    # run bot
    reactor.run()
