"use client"; // this is a clienct component

import React, { useState } from "react";

import styles from "./MainPage.module.css";

import WeekDays from "../main-page-content/week/WeekDays";
import TodayClasses from "../main-page-content/daily-classes/TodayClasses";
import MainContext from "../main-page-content/main-content/MainContent";

const MainPage = () => {
  const [selectedDay, setSelectedDay] = useState("Monday");

  const selectDayHandler = (theDay: string): void => {
    setSelectedDay(theDay);
    console.log(theDay);
  };

  return (
    <main className={styles["main-content"]}>
      <div className={styles["week"]}>
        <WeekDays onSelectDayHandler={selectDayHandler} />
      </div>
      <div className={styles["classes"]}>
        <TodayClasses currentDay={selectedDay} />
      </div>
      <div className={styles["content"]}>
        <MainContext />
      </div>
    </main>
  );
};

export default MainPage;
