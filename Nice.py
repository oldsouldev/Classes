from nicegui import ui
ui.header().style('background-color: orange')
ui.input().props('outlined dense').classes('bg-white').style('font-size:24px; font-weight: bold; width: 100%')
ui.button('hello',color="deep-orange").classes('glossy')
ui.label('Cross section').classes('text-h6 text-red')
ui.card().classes('text-white').style('align-items : center; width : 100%; background: radial-gradient(circle,#35a2ff 0%,#014a88 100%)')
ui.card().classes('bg-orange')
ui.run()
