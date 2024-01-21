from maubot import Plugin, MessageEvent
from maubot.handlers import command


class Timer(Plugin):
  @command.new()
  @command.argument("time")
  async def timer(self, evt: MessageEvent, time: str) -> None:
    await evt.respond(f"Timer started for {time} seconds")
