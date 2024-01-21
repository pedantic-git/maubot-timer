from maubot import Plugin, MessageEvent
from maubot.handlers import command
import asyncio

class Timer(Plugin):
  @command.new()
  @command.argument("time", required=True)
  @command.argument("name", required=False)
  async def timer(self, evt: MessageEvent, time: str, name: str | None) -> None:
    time = int(time)
    name = name or "anon"
    await evt.respond(f"⏳ Timer {name} started for {time} seconds")
    await asyncio.sleep(time)
    await evt.respond(f"⏰ Timer {name}: time's up!")
