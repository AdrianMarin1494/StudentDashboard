import React from "react";

import styles from "./HomeworkDetails.module.css";

const HOMEWORK_DETAILS = {
  Math: {
    "First Math homework": "Complete the exercise 4 from page 12",
    "Second Math homework": "Complete the exercise 2 from page 15",
    "Third Math homework": "Complete the exercise 7 from page 22",
  },
};

const HomeworkDetails = ({
  selectedClassName,
  selectedHomeworkName,
  onCloseModal,
}) => {
  if (!selectedClassName || !selectedHomeworkName) {
    return;
  }

  const homeworkDetails =
    HOMEWORK_DETAILS[selectedClassName][selectedHomeworkName];

  const closeModal = () => {
    onCloseModal();
  };

  return (
    <div className={styles["homeworkdetails-content"]}>
      <div>
        <h3>{selectedClassName}</h3>
        <h3>{selectedHomeworkName}</h3>
        <p>{homeworkDetails}</p>
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

export default HomeworkDetails;
