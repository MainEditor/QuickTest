import plotly.express as px
import pandas as pd
import flet as ft
from flet.plotly_chart import PlotlyChart


class StatWindow():
    def __init__(self, statistics, topic):
        self.topic = topic
        self.NEED_RETURN = False
        self.back_button = ft.TextButton(content=ft.Row([ft.Icon(name=ft.icons.ARROW_BACK), ft.Text('Вернуться к списку тем')], width=200, alignment=ft.MainAxisAlignment.CENTER), on_click=self.go_back)
        if len(statistics) > 1:
            self.data = list(map(float, statistics[1:]))
            ft.app(target=self.MainStatWindow)
        else:
            ft.app(target=self.NoStatWindow)

    def MainStatWindow(self, page: ft.Page):
        self.close = lambda: page.window_close()

        page.window_center()
        page.window_focused = True
        page.window_height = page.window_min_height = 705*1.2
        page.window_width = page.window_min_width = 948*1.2
        page.padding = 25
        page.title = "QuickTest"
        page.vertical_alignment = ft.MainAxisAlignment.CENTER
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        # d = {
        #     "Кол-во тестов": list(range(1, len(self.data)+1)) * 2,
        #     "Тип ответа": len(self.data) * ["Правильные ответы"] + len(self.data) * ["Неправильные ответы"],
        #     "Соотношение": self.data + [100 - x for x in self.data]
        # }
        # table = pd.DataFrame(d)
        # color='Тип ответа'
        # colors=['#4caf50', "#f44336"]
        fig = px.line(pd.DataFrame(), x=range(1, len(self.data)+1), y=self.data, title=f'Ваша статистика по теме "{self.topic}":', labels={'x': 'Тесты', 'y': 'Процент верных ответов, %'}, markers=True if len(self.data) < 20 else False)
        fig.update_layout(yaxis_range=[-2, 102])
        fig.update_layout(xaxis_range=[0.9, len(self.data) + 0.1])
        # fig.update_layout(xaxis=dict(dtick=1))
        page.add(PlotlyChart(fig, expand=True), self.back_button)
    
    def NoStatWindow(self, page):
        self.close = lambda: page.window_close()

        page.window_center()
        page.window_focused = True
        page.window_height = page.window_min_height = 400
        page.window_width = page.window_min_width = 600
        page.padding = 25
        page.vertical_alignment = ft.MainAxisAlignment.CENTER
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        page.title = "QuickTest"
        page.add(ft.Text(size=20, value='Нет доступных данных по данному набору тестов.'), self.back_button)
    
    def go_back(self, e):
        self.close()
        self.NEED_RETURN = True
