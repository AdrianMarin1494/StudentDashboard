"use client"; // this is a clienct component

import React from "react";

import styles from "./MainContext.module.css";

const MainContext = () => {
  return (
    <div className={styles["main-content"]}>
      <div className={styles["homework"]}>
        <h3>Test1</h3>
      </div>
      <div className={styles["projects"]}>
        <h3>Test2</h3>
      </div>
      <div className={styles["finals"]}>
        <h3>Test3</h3>
      </div>
      <div className={styles["teachernotes"]}>
        <h3>Test4</h3>
      </div>
      <div className={styles["downloaddocuments"]}>
        <h3>Test5</h3>
      </div>
      <div className={styles["classesdates"]}>
        <h3>Test6</h3>
      </div>
      <div className={styles["writetoteacher"]}>
        <h3>Test7</h3>
      </div>
      <div className={styles["uploaddocuments"]}>
        <h3>Test8</h3>
      </div>
      <div className={styles["attendence"]}>
        <h3>Test9</h3>
      </div>
      <div className={styles["grades"]}>
        <h3>Test10</h3>
      </div>
    </div>
  );
};

export default MainContext;
