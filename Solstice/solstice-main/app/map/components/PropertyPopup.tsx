
import { Dispatch, SetStateAction, useState } from 'react'
import { Dialog, DialogBackdrop, DialogPanel, DialogTitle } from '@headlessui/react'
import { HomeIcon } from '@heroicons/react/24/outline'
import { Property } from '@/app/models/property.model'

function PropertyPopup({property, open, setOpen} : { property: Property, open: boolean, setOpen: Dispatch<SetStateAction<boolean>>} ) {

  return (
    <Dialog className="relative z-[999]" open={open} onClose={setOpen}>
      <DialogBackdrop
        transition
        className="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity data-[closed]:opacity-0 data-[enter]:duration-300 data-[leave]:duration-200 data-[enter]:ease-out data-[leave]:ease-in"
      />
      <div className="fixed inset-0 z-10 w-screen overflow-y-auto">
        <div className="flex min-h-full items-end justify-center p-4 text-center sm:items-center sm:p-0">
          <DialogPanel
            transition
            className="relative transform overflow-hidden rounded-lg bg-gray-800 text-gray-200 px-4 pb-4 pt-5 text-left shadow-xl transition-all data-[closed]:translate-y-4 data-[closed]:opacity-0 data-[enter]:duration-300 data-[leave]:duration-200 data-[enter]:ease-out data-[leave]:ease-in sm:my-8 sm:w-full sm:max-w-lg sm:p-6 data-[closed]:sm:translate-y-0 data-[closed]:sm:scale-95"
          >
            <div>
              <div className="mx-auto flex h-12 w-12 items-center justify-center rounded-full bg-blue-100">
                <HomeIcon className="h-6 w-6 text-blue-600" aria-hidden="true" />
              </div>
              <div className="mt-3 text-center sm:mt-5">
                <DialogTitle as="h3" className="text-base font-semibold leading-6 text-gray-200">
                  Property Details
                </DialogTitle>
                <div className="mt-2 text-left">
                  <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                    <div>
                      <h3 className="font-semibold">Property Info</h3>
                      <p className="text-sm"><span className="font-bold">UPRN:</span> {property.uprn}</p>
                      <p className="text-sm"><span className="font-bold">Address 1:</span> {property.address_1}</p>
                      <p className="text-sm"><span className="font-bold">Address 2:</span> {property.address_2}</p>
                      <p className="text-sm"><span className="font-bold">Address 3:</span> {property.address_3}</p>
                      <p className="text-sm"><span className="font-bold">Postcode:</span> {property.postcode}</p>
                    </div>
                    <div>
                      <h3 className="font-semibold">Property Info</h3>
                      <p className="text-sm"><span className="font-bold">Asset Rating:</span> {property.asset_rating} ({property.asset_rating_band})</p>
                      <p className="text-sm"><span className="font-bold">Floor Area:</span> {property.floor_area} sqm</p>
                      <p className="text-sm"><span className="font-bold">Building Level:</span> {property.building_level}</p>
                      <p className="text-sm"><span className="font-bold">Main Heating Fuel:</span> {property.main_heating_fuel}</p>
                      <p className="text-sm"><span className="font-bold">Title Number:</span> {property.title_number}</p>
                      <p className="text-sm"><span className="font-bold">Tenure:</span> {property.tenure}</p>
                    </div>
                    <div>
                      <h3 className="font-semibold">Energy & Emissions</h3>
                      <p className="text-sm"><span className="font-bold">Annual Energy Usage:</span> {property.annual_energy_usage} kWh</p>
                      <p className="text-sm"><span className="font-bold">Building Emissions:</span> {property.building_emissions} kg CO2</p>
                      <p className="text-sm"><span className="font-bold">Potential Energy Savings:</span> {property.potential_energy_savings} kWh</p>
                      <p className="text-sm"><span className="font-bold">Yield Potential:</span> {property.yield_potential}</p>
                    </div>
                    <div>
                      <h3 className="font-semibold">Location</h3>
                      <p className="text-sm"><span className="font-bold">Latitude:</span> {property.latitude}</p>
                      <p className="text-sm"><span className="font-bold">Longitude:</span> {property.longitude}</p>
                      <p className="text-sm"><span className="font-bold">DNO Substation Status:</span> {property.dno_substation_status}</p>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div className="mt-5 sm:mt-6 sm:grid sm:grid-flow-row-dense sm:grid-cols-2 sm:gap-3">
              <button
                type="button"
                className="mt-3 inline-flex w-full justify-center rounded-md bg-gray-700 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-gray-600 sm:col-start-1 sm:mt-0"
                onClick={() => setOpen(false)}
                data-autofocus
              >
                Cancel
              </button>
            </div>
          </DialogPanel>
        </div>
      </div>
    </Dialog>
  )
}

export default PropertyPopup