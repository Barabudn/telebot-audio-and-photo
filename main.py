
import telebot
import cv2
token = 'Ваш токен'
bot = telebot.TeleBot(token)

@bot.message_handler(content_types=['voice'])
def voice_processing(message):
    file_info = bot.get_file(message.voice.file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    with open(f"{message.from_user.id + message.id}.wav", 'wb') as new_file:
        new_file.write(downloaded_file)

@bot.message_handler(content_types=['photo'])
def handle_docs_document(message):
    file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    src = 'D://Игорь/PyCharm/pythonProject4/photo' + message.photo[1].file_id + '.jpg'
    with open(src, 'wb') as new_file:
        image = new_file.write(downloaded_file)
        image = cv2.imread('photo' + message.photo[1].file_id + '.jpg')
        image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        faces = face_cascade.detectMultiScale(image_gray)
        print(f"{len(faces)} лиц обнаружено на изображении.") # просто для себя оставляю визуал
        if len(faces) >= 1:
            new_file.write(downloaded_file)
            bot.reply_to(message, "Фото добавлено")
        else:
            bot.reply_to(message, "Лиц не обнаружено, фото не добавлено")



if __name__ == '__main__':
    bot.polling(none_stop=True)
