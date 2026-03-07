from pyscript import document
from project_info import projects_data

projectsListEl = document.querySelector("#projects-list")


def populate_project_els(nr):
    for _ in range(1, nr + 1):
        if _ in projects_data:
            project_title = projects_data[_]["title"]
            project_link = projects_data[_]["link"]
        else:
            project_title = "Work in progress"
            # project_link = "#"

        li_element = document.createElement("li")
        li_element.className = "day"
        li_element.innerHTML = f"""
            <a href="{project_link}" target="_blank" rel="noopener noreferrer">
                <p>Project</p>
                <h3>{_}</h3>
                <p>{project_title}</p>
            </a>
"""
        projectsListEl.appendChild(li_element)


populate_project_els(100)
