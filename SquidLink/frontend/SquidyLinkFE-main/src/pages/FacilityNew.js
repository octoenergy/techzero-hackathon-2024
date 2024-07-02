import { useState } from 'react';
import { PhotoIcon, UserCircleIcon } from '@heroicons/react/24/solid';
import { useNavigate } from 'react-router-dom';

export default function Example() {
  const [formData, setFormData] = useState({
    name: '',
    address_line_1: '',
    address_line_2: '',
    address_postcode: '',
    address_city: '',
    address_country: '',
    bms: 'Johnson Controls',
    sector: 'AGRICULTURE',
    floor_area_square_metres: 0,
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value,
    });
  };
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch('http://localhost:8000/facility', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
      });
      if (response.ok) {
        alert('Facility information saved successfully.');
        navigate("/project/new");
      } else {
        alert('Failed to save facility information.');
      }
    } catch (error) {
      console.error('Error:', error);
      alert('An error occurred while saving facility information.');
    }
  };

  return (
    <div className="space-y-10 divide-y divide-gray-900/10 p-20">
      <div className="grid grid-cols-1 gap-x-8 gap-y-8 pt-10 md:grid-cols-3">
        <div className="px-4 sm:px-0">
          <h2 className="text-base font-semibold leading-7 text-gray-900">Facility Information</h2>
          <p className="mt-1 text-sm leading-6 text-gray-600">Use a permanent address where you can receive mail.</p>
        </div>

        <form onSubmit={handleSubmit} className="bg-white shadow-sm ring-1 ring-gray-900/5 sm:rounded-xl md:col-span-2">
          <div className="px-4 py-6 sm:p-8">
            <div className="grid max-w-2xl grid-cols-1 gap-x-6 gap-y-8 sm:grid-cols-6">
              <div className="sm:col-span-full">
                <label htmlFor="name" className="block text-sm font-medium leading-6 text-gray-900">
                  Facility Name
                </label>
                <div className="mt-2">
                  <input
                    id="name"
                    name="name"
                    type="text"
                    value={formData.name}
                    onChange={handleChange}
                    className="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
                  />
                </div>
              </div>
              <div className="sm:col-span-3">
                <label htmlFor="address_line_1" className="block text-sm font-medium leading-6 text-gray-900">
                  Address Line 1
                </label>
                <div className="mt-2">
                  <input
                    type="text"
                    name="address_line_1"
                    id="address_line_1"
                    value={formData.address_line_1}
                    onChange={handleChange}
                    className="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
                  />
                </div>
              </div>

              <div className="sm:col-span-3">
                <label htmlFor="address_line_2" className="block text-sm font-medium leading-6 text-gray-900">
                  Address Line 2
                </label>
                <div className="mt-2">
                  <input
                    type="text"
                    name="address_line_2"
                    id="address_line_2"
                    value={formData.address_line_2}
                    onChange={handleChange}
                    className="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
                  />
                </div>
              </div>

              <div className="sm:col-span-2">
                <label htmlFor="address_postcode" className="block text-sm font-medium leading-6 text-gray-900">
                  ZIP / Postal code
                </label>
                <div className="mt-2">
                  <input
                    type="text"
                    name="address_postcode"
                    id="address_postcode"
                    value={formData.address_postcode}
                    onChange={handleChange}
                    className="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
                  />
                </div>
              </div>

              <div className="sm:col-span-2">
                <label htmlFor="address_city" className="block text-sm font-medium leading-6 text-gray-900">
                  City
                </label>
                <div className="mt-2">
                  <input
                    type="text"
                    name="address_city"
                    id="address_city"
                    value={formData.address_city}
                    onChange={handleChange}
                    className="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
                  />
                </div>
              </div>

              <div className="sm:col-span-2">
                <label htmlFor="address_country" className="block text-sm font-medium leading-6 text-gray-900">
                  Country
                </label>
                <div className="mt-2">
                  <input
                    type="text"
                    name="address_country"
                    id="address_country"
                    value={formData.address_country}
                    onChange={handleChange}
                    className="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
                  />
                </div>
              </div>

              <div className="sm:col-span-3">
                <label htmlFor="bms" className="block text-sm font-medium leading-6 text-gray-900">
                  Building Management System (BMS)
                </label>
                <div className="mt-2">
                  <select
                    id="bms"
                    name="bms"
                    value={formData.bms}
                    onChange={handleChange}
                    className="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
                  >
                    <option value="Johnson Controls">Johnson Controls</option>
                    <option value="Siemens">Siemens</option>
                    <option value="Honeywell">Honeywell</option>
                    <option value="Schneider Electric">Schneider Electric</option>
                    <option value="ABB">ABB</option>
                    <option value="Trane Technologies">Trane Technologies</option>
                    <option value="Delta Controls">Delta Controls</option>
                    <option value="Automated Logic">Automated Logic</option>
                    <option value="Legrand">Legrand</option>
                    <option value="BuildingIQ">BuildingIQ</option>
                  </select>
                </div>
              </div>

              <div className="sm:col-span-3">
                <label htmlFor="sector" className="block text-sm font-medium leading-6 text-gray-900">
                  Sector
                </label>
                <div className="mt-2">
                  <select
                    id="sector"
                    name="sector"
                    value={formData.sector}
                    onChange={handleChange}
                    className="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
                  >
                    <option value="AGRICULTURE">Agriculture</option>
                    <option value="COMMERCIAL">Commercial</option>
                    <option value="INDUSTRIAL">Industrial</option>
                    <option value="RESIDENTIAL">Residential</option>
                    <option value="OTHER">Other</option>
                  </select>
                </div>
              </div>

              <div className="col-span-full">
                <label htmlFor="floor_area_square_metres" className="block text-sm font-medium leading-6 text-gray-900">
                  Floor Area (Square Metres)
                </label>
                <div className="mt-2">
                  <input
                    type="number"
                    name="floor_area_square_metres"
                    id="floor_area_square_metres"
                    value={formData.floor_area_square_metres}
                    onChange={handleChange}
                    className="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
                  />
                </div>
              </div>
            </div>
          </div>
          <div className="flex items-center justify-end gap-x-6 border-t border-gray-900/10 px-4 py-4 sm:px-8">
            <button type="button" className="text-sm font-semibold leading-6 text-gray-900">
              Cancel
            </button>
            <button
              type="submit"
              className="rounded-md bg-indigo-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
            >
              Save
            </button>
          </div>
        </form>
      </div>
    </div>
  );
}
