"use client";
import MainDashboard from "@/components/Dashboard/MainDashboard";
import DefaultLayout from "@/components/Layouts/DefaultLayout";

export default function Home() {
  return (
    <>
      <DefaultLayout>
        <MainDashboard />
      </DefaultLayout>
    </>
  );
}
