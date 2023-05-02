"use client"; // this is a clienct component
import React from "react";

import styles from "./FinalsDetails.module.css";

const FINALS_DETAILS = {
  Math: {
    "First Math final": "Complete the first final",
    "Second Math final": "Complete the second final",
    "Third Math final": "Complete the third final",
  },
};

const FinalDetails = ({
  selectedClassName,
  selectedFinalName,
  onCloseModal,
}) => {
  if (!selectedClassName || !selectedFinalName) {
    return;
  }

  const projectDetails = FINALS_DETAILS[selectedClassName][selectedFinalName];

  const closeModal = () => {
    onCloseModal();
  };

  return (
    <div className={styles["finalsdetails-content"]}>
      <div>
        <h3>{selectedClassName}</h3>
        <h3>{selectedFinalName}</h3>
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

export default FinalDetails;
