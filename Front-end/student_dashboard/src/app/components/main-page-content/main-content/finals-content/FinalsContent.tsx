import React, { useState } from "react";

import styles from "./FinalsContent.module.css";
import FinalsDetails from "./FinalsDetails";

const DUMMY_FINALS = {
  Math: ["First Math exam", "Second Math exam", "Third Math exam"],
  English: ["First English exam", "Second English exam", "Third English exam"],
  Franch: ["First French exam", "Second French exam", "Third French exam"],
  Geography: [
    "First Geography exam",
    "Second Geography exam",
    "Third Geography exam",
  ],
  History: ["First History exam", "Second History exam", "Third History exam"],
  Economics: [
    "First Economics exam",
    "Second Economics exam",
    "Third Economics exam",
  ],
};

const FinalsContent = ({ selectedClassFinals }) => {
  const [selectedFinal, setSelectedFinal] = useState("");
  const finalsClassList = DUMMY_FINALS[selectedClassFinals];

  const handlesSelectFinal = (event) => {
    setSelectedFinal(event.target.textContent);
    console.log(event.target.textContent);
  };

  const finalsClass = finalsClassList.map((theClass) => (
    <li key={theClass} onClick={handlesSelectFinal}>
      {theClass}
    </li>
  ));

  const handleCloseModal = () => {
    setSelectedFinal("");
  };

  return (
    <>
      <div className={styles["finals-content"]}>
        {/* <h2>{props.currentDay}'s classes</h2> */}
        <h2>{selectedClassFinals} finals</h2>
        <ul className={styles["finals-list"]}>{finalsClass}</ul>
      </div>
      <div>
        <FinalsDetails
          selectedClassName={selectedClassFinals}
          selectedFinalName={selectedFinal}
          onCloseModal={handleCloseModal}
        />
      </div>
    </>
  );
};

export default FinalsContent;
