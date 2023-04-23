"use client"; // this is a clienct component

import React from "react";

import styles from "./MainContext.module.css";
import LaptopImage from "../../../styles/images/laptop.avif";

import HomeworkContent from "./homework-content/HomeworkContent";
import ProjectsContent from "./projects-content/ProjectsContent";
import FinalsContent from "./finals-content/FinalsContent";

const MainContext = ({ currentClass }) => {
  if (!currentClass) {
    return (
      <div>
        <img
          // className={styles["nocontent-image"]}
          style={{ width: "100%", height: "97.5vh", "border-radius": "1vw" }}
          src={LaptopImage.src}
        />
      </div>
    );
  }
  return (
    <div className={styles["main-content"]}>
      <div className={styles["homework"]}>
        <HomeworkContent selectedClassHomework={currentClass} />
      </div>
      <div className={styles["projects"]}>
        <ProjectsContent selectedClassProjects={currentClass} />
      </div>
      <div className={styles["finals"]}>
        <FinalsContent selectedClassFinals={currentClass} />
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
