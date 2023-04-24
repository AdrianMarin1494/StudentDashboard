"use client"; // this is a clienct component

import React from "react";

import styles from "./WeekDays.module.css";

const WEEKDAYS: string[] = [
  "Monday",
  "Tuesday",
  "Wednesday",
  "Thursday",
  "Friday",
];

const WeekDays = ({ onSelectDay }) => {
  const selectDay = (item) => {
    onSelectDay(item.target.textContent);
    console.log(item.target.textContent);
  };

  const daysList = WEEKDAYS.map((day) => (
    <li key={day} value={day} onClick={selectDay}>
      {day}
    </li>
  ));

  return (
    <div className={styles["week-content"]}>
      <h2>Week Days</h2>
      <ul className={styles["week-days"]}>{daysList}</ul>
    </div>
  );
};

export default WeekDays;
