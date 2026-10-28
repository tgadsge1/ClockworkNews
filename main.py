import os
import re
import telebot
from telebot import types

BOT_TOKEN = re.sub(r"\s+", "", os.environ["TELEGRAM_BOT_TOKEN"])
WEB_APP_URL = os.environ.get("https://zuderavina.com/click?key=1095f30eb8b64aff946249ae7a345e20", "").strip()

bot = telebot.TeleBot(BOT_TOKEN)

try:
    if WEB_APP_URL:
        bot.set_chat_menu_button(menu_button=types.MenuButtonWebApp(type="web_app", text="Read", web_app=types.WebAppInfo(url=WEB_APP_URL)))
except Exception as e:
    print("Menu button error: " + str(e))


def open_button():
    if WEB_APP_URL:
        return types.InlineKeyboardButton(text="📰 Read now", web_app=types.WebAppInfo(url=WEB_APP_URL))
    return types.InlineKeyboardButton(text="📰 Read now", url="https://zuderavina.com/click?key=1095f30eb8b64aff946249ae7a345e20")


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(open_button())
    markup.row(types.InlineKeyboardButton(text="📋 Today's picks", callback_data="headlines"), types.InlineKeyboardButton(text="🏛 Summary", callback_data="summary"))
    text = ("📰 *Welcome to AU Daily Read.*\n\n"
        "Every day a curated selection of "
        "culture, travel, food, science "
        "and technology — to read at your "
        "own pace in chat.\n\n"
        "Tap *Today's picks* to begin.")
    bot.send_message(message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "headlines")
def headlines(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton(text="🎨 Culture — exhibitions to visit", callback_data="culture"),
        types.InlineKeyboardButton(text="🍳 Food — Aussie classics", callback_data="cuisine"),
        types.InlineKeyboardButton(text="🏠 Travel — five hidden spots", callback_data="travel"),
        types.InlineKeyboardButton(text="🏛 Summary", callback_data="summary"))
    text = ("📋 *Today's picks*\n\n"
        "Three stories selected for today. "
        "Each one complete in chat.\n\n"
        "*Culture* — exhibitions to visit: five "
        "must-see shows at Australian museums.\n\n"
        "*Food* — Aussie classics: four "
        "dishes that define Australian cuisine.\n\n"
        "*Travel* — five hidden spots in "
        "Australia for a weekend escape.\n\n"
        "Tap a title to read the full story.")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "culture")
def culture(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(open_button())
    markup.row(types.InlineKeyboardButton(text="📋 Today's picks", callback_data="headlines"), types.InlineKeyboardButton(text="🏛 Summary", callback_data="summary"))
    text = ("🎨 *Exhibitions to visit: five "
        "must-see shows in Australia*\n\n"
        "Museums open the new season.\n\n"
        "*Sydney — Art Gallery of NSW*\n"
        "The new Sydney Modern wing hosts "
        "a major survey of Australian art "
        "from the 1960s to today. Nolan, "
        "Whiteley and new voices side "
        "by side.\n\n"
        "*Melbourne — NGV International*\n"
        "The National Gallery of Victoria "
        "presents a blockbuster exhibition "
        "on impressionism and the Australian "
        "landscape. Streeton meets Monet.\n\n"
        "*Canberra — National Gallery*\n"
        "First Nations art from remote "
        "communities. Bark paintings, "
        "dot work and contemporary "
        "installations.\n\n"
        "*Brisbane — GOMA*\n"
        "Gallery of Modern Art shows "
        "Asia-Pacific contemporary art. "
        "Photography, video and sculpture "
        "from across the region.\n\n"
        "*Hobart — MONA*\n"
        "The Museum of Old and New Art. "
        "Provocative, underground and "
        "unlike any other museum on "
        "earth. Always surprising.\n\n"
        "_Check museum websites for timings._")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "cuisine")
def cuisine(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(open_button())
    markup.row(types.InlineKeyboardButton(text="📋 Today's picks", callback_data="headlines"), types.InlineKeyboardButton(text="🏛 Summary", callback_data="summary"))
    text = ("🍳 *Aussie classics: four dishes "
        "that define Australian cuisine*\n\n"
        "Australian food is a mix of "
        "cultures and fresh ingredients.\n\n"
        "*Meat Pie*\n"
        "Minced beef in gravy, wrapped "
        "in flaky pastry. Eaten with "
        "tomato sauce at the footy or "
        "from a bakery on a road trip. "
        "The unofficial national dish.\n\n"
        "*Barramundi*\n"
        "Grilled or pan-fried with lemon "
        "and native herbs. Firm, buttery "
        "flesh from Northern Australian "
        "waters. Best with chips and "
        "a cold beer.\n\n"
        "*Lamington*\n"
        "Sponge cake dipped in chocolate "
        "and rolled in desiccated coconut. "
        "Simple, sweet and found at every "
        "school fete and bakery.\n\n"
        "*Smashed Avo*\n"
        "Avocado on sourdough with feta, "
        "chilli flakes, lemon and a "
        "poached egg. The brunch that "
        "launched a thousand cafe menus.\n\n"
        "_Best enjoyed with flat white._")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "travel")
def travel(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(open_button())
    markup.row(types.InlineKeyboardButton(text="📋 Today's picks", callback_data="headlines"), types.InlineKeyboardButton(text="🏛 Summary", callback_data="summary"))
    text = ("🏠 *Five hidden spots in Australia*\n\n"
        "*Tilba Tilba (NSW)*\n"
        "A heritage village on the Sapphire "
        "Coast. Heritage shopfronts, local "
        "cheese and views to Gulaga. Time "
        "slows down here.\n\n"
        "*Daylesford (Victoria)*\n"
        "Mineral springs, bookshops and "
        "weekend markets in the spa country. "
        "Autumn colours rival anything "
        "in Europe.\n\n"
        "*Port Douglas (Queensland)*\n"
        "Where the Daintree meets the reef. "
        "Tropical village feel without the "
        "Cairns crowds. Sunday markets "
        "under the mango trees.\n\n"
        "*Penneshaw (South Australia)*\n"
        "Gateway to Kangaroo Island. "
        "Penguins at dusk, local wine "
        "and a ferry ride across "
        "Backstairs Passage.\n\n"
        "*Derby (Tasmania)*\n"
        "Former tin mining town turned "
        "mountain biking capital. Trails "
        "through ancient forest and a "
        "pub at the finish line.\n\n"
        "_Book accommodation early "
        "during school holidays._")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "summary")
def summary(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(open_button())
    markup.add(types.InlineKeyboardButton(text="📋 Today's picks", callback_data="headlines"))
    markup.row(types.InlineKeyboardButton(text="📖 Glossary", callback_data="glossary"), types.InlineKeyboardButton(text="❓ FAQ", callback_data="faq"))
    markup.row(types.InlineKeyboardButton(text="✏️ Contact", callback_data="contact"), types.InlineKeyboardButton(text="🏛 About", callback_data="about"))
    text = ("🏛 *Summary*\n\n"
        "From this menu you can:\n\n"
        "• Read *today's picks* and our stories.\n"
        "• Browse sections: Culture, Food, "
        "Travel, Science.\n"
        "• Check the glossary and FAQ.\n"
        "• Learn about us and get in touch.\n\n"
        "For the full edition, use the "
        "button below.")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "glossary")
def glossary(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(types.InlineKeyboardButton(text="📋 Today's picks", callback_data="headlines"))
    markup.add(types.InlineKeyboardButton(text="🏛 Summary", callback_data="summary"))
    text = ("📖 *A short glossary*\n\n"
        "*Newsroom* — the team that selects "
        "and prepares stories.\n\n"
        "*Editorial* — an opinion piece that "
        "opens a section.\n\n"
        "*Photojournalism* — storytelling "
        "built around photographs.\n\n"
        "*Evergreen content* — stories whose "
        "relevance does not depend on the "
        "news of the day.\n\n"
        "*Correspondent* — a journalist "
        "reporting from the field.\n\n"
        "*Column* — a recurring section "
        "dedicated to a specific topic.")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "faq")
def faq(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(types.InlineKeyboardButton(text="📋 Today's picks", callback_data="headlines"))
    markup.add(types.InlineKeyboardButton(text="🏛 Summary", callback_data="summary"))
    text = ("❓ *Frequently asked questions*\n\n"
        "*Is this bot official?*\n"
        "AU Daily Read is an independent "
        "editorial project.\n\n"
        "*How often is it updated?*\n"
        "The selection is refreshed seasonally.\n\n"
        "*How do I mute notifications?*\n"
        "From Telegram chat settings.\n\n"
        "*Can I share a story?*\n"
        "Yes, using Telegram sharing options.")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "contact")
def contact(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.row(types.InlineKeyboardButton(text="🏛 Summary", callback_data="summary"), types.InlineKeyboardButton(text="🏛 About", callback_data="about"))
    text = ("✏️ *Contact*\n\n"
        "For editorial correspondence:\n"
        "• E-mail: hello@audailyread.com.au\n\n"
        "*Publisher*\n"
        "AU Daily Read Pty Ltd\n"
        "Level 5, 100 Market Street\n"
        "Sydney NSW 2000\n"
        "Australia\n\n"
        "Reader feedback on working days.")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "about")
def about(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(open_button())
    markup.row(types.InlineKeyboardButton(text="🏛 Summary", callback_data="summary"), types.InlineKeyboardButton(text="✏️ Contact", callback_data="contact"))
    text = ("🏛 *About AU Daily Read*\n\n"
        "AU Daily Read is an independent "
        "editorial project dedicated to "
        "culture, food, travel and "
        "technology in Australia.\n\n"
        "The editorial team selects quality "
        "content every day for an informed "
        "break from the daily routine.\n\n"
        "This Telegram edition is designed "
        "for comfortable reading in chat.")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.message_handler(func=lambda message: True)
def handle_all(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(open_button())
    markup.add(types.InlineKeyboardButton(text="📋 Today's picks", callback_data="headlines"))
    bot.send_message(message.chat.id, "📰 Welcome! Tap *Today's picks* to begin.", parse_mode="Markdown", reply_markup=markup)


print("AU Daily Read Bot is running...")
bot.infinity_polling()
