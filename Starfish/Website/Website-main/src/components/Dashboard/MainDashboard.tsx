"use client";
import React from "react";
import ChartThree from "../Charts/HouseholdEnergy";
import ChartFour from "../Charts/CommunityEnergy";
import WeatherForecast from "../WeatherForecast";
import InviteNeighbours from "../Invite Neighbours";
import Cash from "../Cash";

const option1 = 30;
const MainDashboard: React.FC = () => {
  return (
    <>
      <div className=" grid grid-cols-12 gap-4">
        <WeatherForecast />
        <InviteNeighbours />
        <ChartThree />
        <ChartFour option1={option1} />
        <Cash />
      </div>
    </>
  );
};

export default MainDashboard;
