"use client"; // this is a clienct component
import React, { useState } from "react";

import styles from "./ProjectsContent.module.css";
import ProjectDetails from "./ProjectDetails";

const DUMMY_PROJECTS = {
  Math: ["First Math project", "Second Math project", "Third Math project"],
  English: [
    "First English project",
    "Second English project",
    "Third English project",
  ],
  Franch: [
    "First French project",
    "Second French project",
    "Third French project",
  ],
  Geography: [
    "First Geography project",
    "Second Geography project",
    "Third Geography project",
  ],
  History: [
    "First History project",
    "Second History project",
    "Third History project",
  ],
  Economics: [
    "First Economics project",
    "Second Economics project",
    "Third Economics project",
  ],
};

const ProjectsContent = ({ selectedClassProjects }) => {
  const [selectedProject, setSelectedProject] = useState("");
  const projectsClassList = DUMMY_PROJECTS[selectedClassProjects];

  const handlesSelectProject = (event) => {
    setSelectedProject(event.target.textContent);
    console.log(event.target.textContent);
  };

  const projectsClass = projectsClassList.map((theClass) => (
    <li key={theClass} onClick={handlesSelectProject}>
      {theClass}
    </li>
  ));

  const handleCloseModal = () => {
    setSelectedProject("");
  };

  return (
    <>
      <div className={styles["projects-content"]}>
        {/* <h2>{props.currentDay}'s classes</h2> */}
        <h2>{selectedClassProjects} projects</h2>
        <ul className={styles["projects-list"]}>{projectsClass}</ul>
      </div>
      <div>
        <ProjectDetails
          selectedClassName={selectedClassProjects}
          selectedProjectName={selectedProject}
          onCloseModal={handleCloseModal}
        />
      </div>
    </>
  );
};

export default ProjectsContent;
