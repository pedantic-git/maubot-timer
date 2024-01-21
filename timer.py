from maubot import Plugin, MessageEvent
from maubot.handlers import command


class Timer(Plugin):
  @command.new()
  async def timer(self, evt: MessageEvent) -> None:
    await evt.reply("You rang?")
