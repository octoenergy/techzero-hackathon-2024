import React from "react";
import Link from "next/link";

const Cash = () => {
  return (
    <div className="col-span-12 rounded-sm border border-stroke bg-white bg-white px-5 pb-5 pt-7.5 shadow-default dark:border-strokedark dark:bg-boxdark sm:px-7.5 xl:col-span-10">
      <h5 className="text-xl font-semibold text-black dark:text-white">
        Community Cashback
      </h5>
      <p>
        The more energy your community makes, the more cash you get for
        community projects and groceries.
      </p>
      <ul className="flex flex-col pt-1 text-lg text-black">
        <li>£10,000 for community garden</li>
        <li>£10 for each community member in Pret vouchers</li>
      </ul>
    </div>
  );
};

export default Cash;
