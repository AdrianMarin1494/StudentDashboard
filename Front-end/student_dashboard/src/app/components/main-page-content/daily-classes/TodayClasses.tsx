"use client"; // this is a clienct component

import React from "react";
import styles from "./TodayClasses.module.css";

const DUMMY_CLASSES = {
  Monday: ["Math", "English", "Franch", "Geography", "History", "Economics"],
  Tuesday: ["English", "History", "Economics", "Math", "Spanish", "Franch"],
  Wednesday: ["Geography", "Spanish", "Economics", "Math", "English", "Franch"],
  Thursday: ["English", "History", "Economics", "Math", "Geography", "Franch"],
  Friday: ["Spanish", "History", "Economics", "Math", "English", "Franch"],
};

const TodayClasses = (props: any) => {
  if (!props.currentDay) {
    return (
      <div className={styles["classes-content"]}>
        <h2>No day selected</h2>
      </div>
    );
  }

  const selectClass = (event) => {
    props.onSelectClass(event.target.textContent);
  };

  const todayClassesList = DUMMY_CLASSES[props.currentDay];
  const todayClasses = todayClassesList.map((theClass) => (
    <li key={theClass} onClick={selectClass}>
      {theClass}
    </li>
  ));
  return (
    <div className={styles["classes-content"]}>
      <h2>{props.currentDay}'s classes</h2>
      <ul className={styles["classes-list"]}>{todayClasses}</ul>
    </div>
  );
};

export default TodayClasses;
