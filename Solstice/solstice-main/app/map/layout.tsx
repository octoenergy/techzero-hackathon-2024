"use client";

import { MapContextProvider } from "@/contexts/mapdata/MapContextProvider";
import PropertySideCard from "./components/PropertySideCard";
import { MapIcon } from "@heroicons/react/24/outline";
import PropertyList from "./components/PropertyList";

const navigation = [
    { name: 'Map', href: '#', icon: MapIcon, current: true },
  ]
export default function RootLayout({
    children,
}: Readonly<{
    children: React.ReactNode;
}>) {
    return (
        <MapContextProvider>

        <div>
            <div className="hidden lg:fixed lg:inset-y-0 lg:z-50 lg:flex lg:w-72 lg:flex-col">

              <div className="flex grow flex-col gap-y-2 overflow-y-auto bg-gray-900 px-6 pb-4">
                <div className="flex h-16 shrink-0 items-center text-xl font-bold">
                  Solstice
                </div>
                <nav className="flex flex-1 flex-col">
                  {/* <ul role="list" className="flex flex-1 flex-col gap-y-7">
                    <li>
                      <ul role="list" className="-mx-2 space-y-1">
                        {navigation.map((item) => (
                          <li key={item.name}>
                            <a
                              href={item.href}
                              className={'bg-gray-800 text-white group flex gap-x-3 rounded-md p-2 text-sm font-semibold leading-6'}
                            >
                              <item.icon className="h-6 w-6 shrink-0" aria-hidden="true" />
                              {item.name}
                            </a>
                          </li>
                        ))}
                      </ul>
                    </li>

                  </ul> */}

                
                  <PropertyList/>
                </nav>
              </div>
            </div>

            <div className="lg:pl-72">


              <main className="py-10">
                <div className="px-4 sm:px-6 lg:px-8">
                  {children}
                </div>
              </main>
            </div>
          </div>
        </MapContextProvider>
    )
}