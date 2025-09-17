import MainDashboard from "@/components/Dashboard/MainDashboard";
import { Metadata } from "next";
import DefaultLayout from "@/components/Layouts/DefaultLayout";

export const metadata: Metadata = {
  title: "Starfish Energy",
  description: "Starfish Energy wants you to jo",
};

export default function Home() {
  // original iframe pointed at free-snails-production . up . railway . app   but that site is no longer valid.
  return (
    <>
      <DefaultLayout>
        <div className="relative h-0 w-full pb-[100vh]">
          <iframe
            src="http://example.com"
            className="absolute left-0 top-0 h-full w-full"
            frameBorder="0"
          />
        </div>
      </DefaultLayout>
    </>
  );
}
