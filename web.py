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

for index, todo_list in enumerate(todos):
    checkbox = st.checkbox(todo_list, key=todo_list)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo_list]
        st.rerun()

st.text_input(label="Add Item", label_visibility='hidden', placeholder="Add a todo",
              on_change=add_todo, key='new_todo')

st.session_state

