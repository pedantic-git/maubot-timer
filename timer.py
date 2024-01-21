from maubot import Plugin, MessageEvent
from maubot.handlers import command
import asyncio

class Timer(Plugin):
  @command.new()
  @command.argument("time")
  async def timer(self, evt: MessageEvent, time: str) -> None:
    time = int(time)
    await evt.respond(f"Timer started for {time} seconds")
    await asyncio.sleep(time)
    await evt.respond("Times up!")
