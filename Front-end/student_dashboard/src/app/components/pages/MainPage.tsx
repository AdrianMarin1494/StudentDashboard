"use client"; // this is a clienct component

import React, { useState } from "react";

import styles from "./MainPage.module.css";

import WeekDays from "../main-page-content/week/WeekDays";
import TodayClasses from "../main-page-content/daily-classes/TodayClasses";
import MainContext from "../main-page-content/main-content/MainContent";

const MainPage = () => {
  const [selectedDay, setSelectedDay] = useState("");
  const [selectedClass, setSelectedClass] = useState("");

  const selectDayHandler = (theDay: string): void => {
    setSelectedDay(theDay);
    console.log(theDay);
  };

  const handleSelectClass = (theClass: string): void => {
    setSelectedClass(theClass);
    console.log(theClass);
  };

  return (
    <main className={styles["main-content"]}>
      <div className={styles["week"]}>
        <WeekDays onSelectDay={selectDayHandler} />
      </div>
      <div className={styles["classes"]}>
        <TodayClasses
          currentDay={selectedDay}
          onSelectClass={handleSelectClass}
        />
      </div>
      <div className={styles["content"]}>
        <MainContext currentClass={selectedClass} />
      </div>
    </main>
  );
};

export default MainPage;
