import React from "react";
import Link from "next/link";

const InviteNeighbours = () => {
  return (
    <div className="col-span-12 rounded-sm border border-stroke bg-white bg-white px-5 pb-5 pt-7.5 shadow-default dark:border-strokedark dark:bg-boxdark sm:px-7.5 xl:col-span-5">
      <h5 className="text-xl font-semibold text-black dark:text-white">
        Add Solar Neighbours
      </h5>
      <p>
        {" "}
        Increase your community's solar impact by adding neighbours to the solar
        map
      </p>
      <div className="flex">
        <Link href="/invites">
          <button className="text-bold my-2 rounded-md bg-[#7cc45f] px-4 py-1 text-lg text-black transition duration-150 ease-in-out hover:bg-opacity-70 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2">
            See Community Impact
          </button>
        </Link>
      </div>
    </div>
  );
};

export default InviteNeighbours;
