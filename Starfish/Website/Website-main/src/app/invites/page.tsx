"use client";

import DefaultLayout from "@/components/Layouts/DefaultLayout";
import Map from "@/components/Map";
import ChartFour from "@/components/Charts/CommunityEnergy";
import { useState } from "react";
export default function Home() {
  const [option1, setOption1] = useState(30);
  const updateOption1 = (newValue: number) => {
    setOption1(newValue);
  };

  return (
    <>
      <DefaultLayout>
        <p className="py-5 text-xl text-black">
          Click to add a neighbour's building to your community solar map.
        </p>
        <div className="flex flex-row justify-between">
          <Map updateOption1={updateOption1} />
          <div className="px-4">
            <ChartFour option1={option1} />
          </div>
        </div>
        <p className="pt-10">Solar Data: Solar API</p>
      </DefaultLayout>
    </>
  );
}
