from redbot.core import commands

class DotaCog(commands.Cog):
    """Dota's custom cog"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def mycom(self, ctx):
        """Dota does stuff!"""
        # Your dota will code here
        await ctx.send("I dota stuff can!")