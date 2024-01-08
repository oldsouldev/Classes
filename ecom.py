from nicegui import ui
cart = {}
with ui.header():
  with ui.row().classes('w-full items-center'):
    with ui.button(icon='menu'):
        with ui.menu() as menu:
            ui.separator()
            ui.menu_item('Close', on_click=menu.close)
    ui.space()
    ui.icon('shopping_cart')
orders = {}

with ui.card().style('width : 100%; align-items: center'):
        ui.image('https://uno.ma/pub/media/catalog/product/cache/af8d7fd2c4634f9c922fba76a4a30c04/l/d/ld0005935809_1_1.jpeg')
        a = ui.label('iPhone')
        a.tailwind('text-orange-600', 'text-xl', 'border-solid', 'border-2', 'border-rose-600')
        image1 = 'https://uno.ma/pub/media/catalog/product/cache/af8d7fd2c4634f9c922fba76a4a30c04/l/d/ld0005935809_1_1.jpeg'
        with ui.row() as roww:
           b = ui.label('15000')
           b.tailwind('text-orange-600', 'text-xl')
           ui.label('dh').tailwind('text-orange-600', 'text-xl')
        mini1 = {a.text:b.text, 'image1':image1}
        ui.button('buy', on_click = lambda: add(mini1))

with ui.card().style('width : 100%; align-items: center'):
        ui.image('https://961souq.com/cdn/shop/files/Samsung-a24.jpg')
        c = ui.label('Samsung')
        c.tailwind('text-orange-600', 'text-xl', 'border-solid', 'border-2', 'border-rose-600')
        image2 = 'https://961souq.com/cdn/shop/files/Samsung-a24.jpg'
        with ui.row():
            d = ui.label('5000')
            d.tailwind('text-orange-600', 'text-xl')
            ui.label('dh').tailwind('text-orange-600', 'text-xl')
        mini2 = {c.text:d.text, 'image2':image2}
        ui.button('buy', on_click = lambda: add(mini2))

with ui.card().style('width : 100%; align-items: center'):
        ui.image('https://files.refurbed.com/ii/oppo-a54-5g-1637760176.jpg')
        e = ui.label('OPPO')
        e.tailwind('text-orange-600', 'text-xl', 'border-solid', 'border-2', 'border-rose-600')
        image3 = 'https://files.refurbed.com/ii/oppo-a54-5g-1637760176.jpg'
        with ui.row():
            f = ui.label('4000')
            f.tailwind('text-orange-600', 'text-xl')
            ui.label('dh').tailwind('text-orange-600', 'text-xl')
        mini3 = {e.text:f.text, 'image3': image3}
        ui.button('buy', on_click = lambda: add(mini3))
def add(a):
        orders.update(a)
        ui.notify('Product added to cart')
        print(orders)
        badge.set_text(int(badge.text) + 1)
with ui.button(on_click = lambda: expand()).style('position : fixed; bottom : 0; right : 0') as b:
        ui.icon('shopping_cart')
        badge = ui.badge('0', color='red').props('floating')
def expand():
              with ui.dialog() as dialog, ui.card().style('width: 100%'):
                  with ui.column():
                     total = 0
                     for x, y in orders.items():
                       with ui.row().style('width: 100%'):
                         if (x != 'image1') and (x != 'image2') and (x != 'image3'):
                              ui.label(f'{x} : {y} dh')
                              total += int(y)
                         if (x == 'image1') or (x == 'image2') or (x == 'image3'):
                              with ui.avatar():
                                   ui.image(f'{orders[x]}')

                  to = ui.label(f'total = {total} dh')
                  to.on('click', lambda: ui.notify('I was clicked'))
                  to.tailwind('text-blue-600', 'absolute', 'bottom-4', 'right-2', 'text-xl')
                  ui.button('Close', on_click=dialog.close)
              dialog.open()

ui.run()
