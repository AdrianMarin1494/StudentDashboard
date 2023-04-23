import React from "react";

import styles from "./HomeworkContent.module.css";

const DUMMY_HOMEWORKS = {
  Math: ["First Math homework", "Second Math homework", "Third Math homework"],
  English: [
    "First English homework",
    "Second English homework",
    "Third English homework",
  ],
  Franch: [
    "First French homework",
    "Second French homework",
    "Third French homework",
  ],
  Geography: [
    "First Geography homework",
    "Second Geography homework",
    "Third Geography homework",
  ],
  History: [
    "First History homework",
    "Second History homework",
    "Third History homework",
  ],
  Economics: [
    "First Economics homework",
    "Second Economics homework",
    "Third Economics homework",
  ],
};

const HomeworkContent = ({ selectedClassHomework }) => {
  //   const homeworkClassList = DUMMY_HOMEWORKS[props.selectedClass];
  const homeworkClassList = DUMMY_HOMEWORKS[selectedClassHomework];
  const homeworkClass = homeworkClassList.map((theClass) => (
    <li key={theClass}>{theClass}</li>
  ));
  return (
    <div className={styles["homework-content"]}>
      {/* <h2>{props.currentDay}'s classes</h2> */}
      <h2>{selectedClassHomework} homeworks</h2>
      <ul className={styles["homework-list"]}>{homeworkClass}</ul>
    </div>
  );
};

export default HomeworkContent;
