from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup


class Task(BoxLayout):
    def __init__(self, task_text, task_list, **kwargs):
        super().__init__(orientation='horizontal', size_hint_y=None, height=40, **kwargs)
        self.task_list = task_list

        self.label = Label(text=task_text)
        self.add_widget(self.label)

        edit_btn = Button(text='Edit', size_hint_x=0.2)
        edit_btn.bind(on_press=self.edit_task)
        self.add_widget(edit_btn)

        delete_btn = Button(text='Delete', size_hint_x=0.2)
        delete_btn.bind(on_press=self.delete_task)
        self.add_widget(delete_btn)

    def edit_task(self, instance):
        def save_edit(instance):
            new_text = edit_input.text
            self.label.text = new_text
            popup.dismiss()

        edit_input = TextInput(text=self.label.text, multiline=False)
        save_button = Button(text='Save')
        save_button.bind(on_press=save_edit)

        box = BoxLayout(orientation='vertical')
        box.add_widget(edit_input)
        box.add_widget(save_button)

        popup = Popup(title='Edit Task', content=box, size_hint=(0.8, 0.4))
        popup.open()

    def delete_task(self, instance):
        self.task_list.remove_widget(self)


class TodoApp(App):
    def build(self):
        self.root = BoxLayout(orientation='vertical', padding=10, spacing=10)

        input_layout = BoxLayout(size_hint_y=None, height=40, spacing=10)
        self.task_input = TextInput(hint_text='Enter task...', multiline=False)
        add_button = Button(text='Add')
        add_button.bind(on_press=self.add_task)

        input_layout.add_widget(self.task_input)
        input_layout.add_widget(add_button)

        self.task_list = BoxLayout(orientation='vertical', spacing=5, size_hint_y=1)

        self.root.add_widget(input_layout)
        self.root.add_widget(self.task_list)

        return self.root

    def add_task(self, instance):
        task_text = self.task_input.text.strip()
        if task_text:
            task = Task(task_text, self.task_list)
            self.task_list.add_widget(task)
            self.task_input.text = ''


if __name__ == '__main__':
    TodoApp().run()
