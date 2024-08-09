from bot import Elysian
from .Errors import Errors
from .BaseEvents import DevEvents
from .Wordism import Wordism


class Events(Errors, DevEvents, Wordism, name="Events"):
    def __init__(self, bot: Elysian):
        self.bot = bot


async def setup(bot: Elysian):
    await bot.add_cog(Events(bot))
