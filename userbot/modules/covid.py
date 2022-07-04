from datetime import datetime
from covid import Covid
from userbot.events import register

@register(outgoing=True, pattern="^\.covid (.*)")
async def corona(event):
    await event.edit("**Ricerca...**")
    country = event.pattern_match.group(1)
    covid = Covid()
    country_data = covid.get_status_by_country_name(country)
    if country_data:
        output_text =  f"**😷Casi confermati: {country_data['confirmed']}**\n"
        output_text += f"**🦠Casi attualmente positivi: {country_data['active']}**\n"
        output_text += f"**☠️Morti: {country_data['deaths']}**\n"
        output_text += f"**🛌Ricoverati: {country_data['recovered']}**\n"
        output_text += (
            "__🔄Ultimo aggiornamento:"
            f"{datetime.utcfromtimestamp(country_data['last_update'] // 1000).strftime('%Y-%m-%d %H:%M:%S')}__\n"
        )
    else:
        output_text = "Nessuna informazione trovata per questo stato!"
    await event.edit(f"**Info sul corona virus in {country}:**\n\n{output_text}")