from nicegui import app, ui, events
from pathlib import Path
import datetime
import base64

media = Path('media')
app.add_media_files('/my_videos', media)

with ui.card().classes('width: 100%'):
  mind = ui.textarea(label = 'What is on your mind').classes('w-64')

#  ui.upload(on_upload=handle_upload)
  def handle_upload(e: events.UploadEventArguments) -> None:
    global filename
    b64_bytes = base64.b64encode(e.content.read())
    filename = e.name.strip("'\"")
    with open(f'stor/{filename}', 'wb') as file:
        file.write(base64.b64decode(b64_bytes))
#    ui.image(f'data:{e.type};base64,{b64_bytes.decode()}')
    ui.notify('Uplouded succes')
    post()
    mind.value = ''
    update.reset()
  update = ui.upload(on_upload=handle_upload)
def post():
#   ui.separator()
   with ui.card().classes('width: 100%'):
       with ui.row():
            ui.avatar('img:https://nicegui.io/logo_square.png', color='blue-2')
            with ui.column().classes('gap-1'):
                 ui.label(f'Mohammed Youss')
                 dt = datetime.datetime.now().date()
                 ui.label(f'{dt}')
       ui.separator()
       ui.label(f'{mind.value}')
       ui.image(f'stor/{filename}')

       u = ui.input(label='Ajoiter un Commentaire').classes('w-64')
       with ui.row():
            ui.button('Ajouter', on_click=lambda: add(u.value))
            with ui.button('Like!', on_click=lambda: badge.set_text(int(badge.text) + 1)):
                 badge = ui.badge('0', color='red').props('floating')
       def add(p):
           with ui.column():
              ui.label(p)
              u.value = ''
ui.run()
