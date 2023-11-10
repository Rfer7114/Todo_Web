import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todo = st.session_state['new_todo'] + '\n'
    todos.append(todo)
    functions.write_todos(todos)


st.title("My Todo App")
st.subheader("Add, delete, edit your list")
st.write("My Current List:")

for todo_list in todos:
    st.checkbox(todo_list, key=todo_list)

st.text_input(label="Add Item", label_visibility='hidden', placeholder="Add a todo",
              on_change=add_todo, key='new_todo')

print('Hello')
st.session_state

