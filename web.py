import streamlit as st
import functions as fn

checklist = fn.get_todos()

def add_new_item():
    new_item = st.session_state['add'] + '\n'
    checklist.append(new_item)
    fn.write_todos(checklist)

st.header("My Checklist")
st.subheader("Add, delete items from your checklist below")
st.write("Use the Add option below to populate your <b>checklist</b>", unsafe_allow_html=True)

for index, item in enumerate(checklist):
    item_to_delete = st.checkbox(item, key=item)
    if item_to_delete:
        checklist.pop(index)
        fn.write_todos(checklist)
        del st.session_state[item]
        st.rerun()


st.text_input("Add Item", label_visibility='hidden',
              placeholder="Add a item to your list", key='add', on_change=add_new_item)
