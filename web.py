import streamlit as st
import functions

todos_local = functions.get_todos()


def add_todo():
    todo_loca = st.session_state["new_todo"] + '\n'
    todos_local.append(todo_loca)
    functions.write_todos(todos_local)


st.title("My TodoList App")
st.subheader("This is my todo app")
st.write("This app is to increase your productivity.")

for index, todo in enumerate(todos_local):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos_local.pop(index)
        functions.write_todos(todos_local)
        del st.session_state[todo]
        st.experimental_rerun()


st.text_input(label="", placeholder="Enter a todo...",
              on_change=add_todo, key='new_todo')


