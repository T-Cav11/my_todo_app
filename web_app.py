import streamlit as st
import Functions

tasks = Functions.get_tasks()

def add_task():
    task = st.session_state["new_task"] + "\n"
    tasks.append(task)
    Functions.write_tasks(tasks)


st.title("Daily tasks")
st.subheader("Daily tasks to be completed")
st.write("This app is designed to increase your productivity")

for index, task in enumerate(tasks):
    checkbox = st.checkbox(task, key=task)
    if checkbox:
        tasks.pop(index)
        Functions.write_tasks(tasks)
        del st.session_state[task]
        st.rerun()




st.text_input(label="",placeholder="Add new task..",
              on_change=add_task, key="new_task")


