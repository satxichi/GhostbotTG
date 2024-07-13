import requests
from bs4 import BeautifulSoup
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = '7285934387:AAEP0lpeNpIBQ0Rego2lsFZEo7DikLuqccY'

def search_ghost_info():
    url = 'https://ru.wikipedia.org/wiki/%D0%93%D0%BE%D1%83%D1%81%D1%82'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    paragraphs = soup.find_all('p')
    ghost_info = ''

    for paragraph in paragraphs:
        ghost_info += paragraph.text
        if len(ghost_info) > 1000:
            break

    return ghost_info.strip()
def search_ghost_photo():
    url = 'https://ru.wikipedia.org/wiki/%D0%93%D0%BE%D1%83%D1%81%D1%82#/media/%D0%A4%D0%B0%D0%B9%D0%BB:Ghost_CoD.jpg'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    infobox = soup.find('table', class_='infobox')
    if infobox:
        img_tag = infobox.find('img')
        if img_tag:
            img_url = 'https:' + img_tag['src']
            return img_url

    return None

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Привет! Я бот, который расскажет тебе о персонаже Гоуст из Call of Duty. Введи команду /ghost , чтобы узнать о персонаже. Введи команду /photo для картинки Call of Duty MW2')

async def ghost(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    ghost_info = search_ghost_info()
    await update.message.reply_text(ghost_info)

async def photo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    photo_url = search_ghost_photo()
    if photo_url:
        await update.message.reply_photo(photo=photo_url)
    else:
        await update.message.reply_text('Изображение не найдено.')

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("ghost", ghost))
    app.add_handler(CommandHandler("photo", photo))

    app.run_polling()

if __name__ == '__main__':
    main()
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Привет! Я бот, который расскажет тебе о персонаже Гоуст из Call of Duty. Введи команду /ghost, чтобы узнать больше.')

async def ghost(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    ghost_info = search_ghost_info()
    await update.message.reply_text(ghost_info)

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("ghost", ghost))

    app.run_polling()

if __name__ == '__main__':
    main()

