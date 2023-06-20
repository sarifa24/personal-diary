extension = file.filename.split('.')[-1]
today = datetime.now()
mytime = today.strftime('%Y-%m-%d-%H-%M-%S')
filename = f'file-{mytime}.{extension}'
save_to = f'static/{filename}'
file.save(save_to)