import nextcord
from nextcord.ext import commands
from nextcord import Interaction
bot = commands.Bot()
token = ""
class func(nextcord.ui.Modal):
    def __init__(self):
        super().__init__(
            "文字",
            timeout=None,
        )

        self.func = nextcord.ui.TextInput(
            label="ラベル",
            style=nextcord.TextInputStyle.short,
            placeholder="背景文字",
            required=True,
        )
        self.add_item(self.func)

    async def callback(self, interaction: Interaction) -> None:
        await interaction.response.send_message(f"{self.func.value}が入力されました")
        return

@bot.slash_command(name="command", description="説明")
async def food_slash(interaction: Interaction):
    modal = func()
    await interaction.response.send_modal(modal=modal)

bot.run(token)
