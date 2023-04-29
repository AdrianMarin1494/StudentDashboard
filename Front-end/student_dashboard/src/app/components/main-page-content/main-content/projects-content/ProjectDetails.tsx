"use client"; // this is a clienct component
import React from "react";

import styles from "./ProjectDetails.module.css";

const PROJECTS_DETAILS = {
  Math: {
    "First Math project": "Complete the first project",
    "Second Math project": "Complete the second project",
    "Third Math project": "Complete the third project",
  },
};

const ProjectDetails = ({
  selectedClassName,
  selectedProjectName,
  onCloseModal,
}) => {
  if (!selectedClassName || !selectedProjectName) {
    return;
  }

  const projectDetails =
    PROJECTS_DETAILS[selectedClassName][selectedProjectName];

  const closeModal = () => {
    onCloseModal();
  };

  return (
    <div className={styles["projectdetails-content"]}>
      <div>
        <h3>{selectedClassName}</h3>
        <h3>{selectedProjectName}</h3>
        <p>{projectDetails}</p>
      </div>
      <div className={styles["comments-area"]}>
        <h3>Questions or details</h3>
        <textarea placeholder="Write your comment..." />
      </div>
      <div className={styles["actions"]}>
        <button onClick={closeModal}>Send</button>
        <button onClick={closeModal}>Close</button>
      </div>
    </div>
  );
};

export default ProjectDetails;
