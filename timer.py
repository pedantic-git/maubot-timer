from maubot import Plugin, MessageEvent
from maubot.handlers import command
import asyncio

class Timer(Plugin):
  NAMES = [
    "alfa", "bravo", "charlie", "delta", "echo", "foxtrot", "golf", "hotel",
    "india", "juliett", "kilo", "lima", "mike", "november", "oscar", "papa",
    "quebec", "romeo", "sierra", "tango", "uniform", "victor", "whiskey",
    "xray", "yankee", "zulu"
  ]

  async def start(self) -> None:
    self.namei = 0

  @command.new()
  @command.argument("time", required=True)
  @command.argument("name", required=False)
  async def timer(self, evt: MessageEvent, time: str, name: str | None) -> None:
    time = int(time)
    name = name or self.new_name()
    await evt.respond(f"⏳ Timer {name} started for {time} seconds")
    await asyncio.sleep(time)
    await evt.respond(f"⏰ Timer {name}: time's up!")

  def new_name(self) -> str:
    name = self.NAMES[self.namei % 26]
    self.namei += 1
    return name
