import React, { useState } from "react";

import styles from "./HomeworkContent.module.css";

import HomeworkDetails from "./HomeworkDetails";

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
  const [selectedHomework, setSelectedHomework] = useState("");

  const handlesSelectHomework = (event) => {
    setSelectedHomework(event.target.textContent);
    console.log(event.target.textContent);
  };

  const homeworkClassList = DUMMY_HOMEWORKS[selectedClassHomework];
  const homeworkClass = homeworkClassList.map((theClass) => (
    <li key={theClass} onClick={handlesSelectHomework}>
      {theClass}
    </li>
  ));

  const handleCloseModal = () => {
    setSelectedHomework("");
  };

  return (
    <>
      <div className={styles["homework-content"]}>
        <h2>{selectedClassHomework} homeworks</h2>
        <ul className={styles["homework-list"]}>{homeworkClass}</ul>
      </div>
      <HomeworkDetails
        selectedClassName={selectedClassHomework}
        selectedHomeworkName={selectedHomework}
        onCloseModal={handleCloseModal}
      />
    </>
  );
};

export default HomeworkContent;
