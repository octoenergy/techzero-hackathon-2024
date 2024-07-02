import { useState } from 'react';

export default function BidForm() {
  const [formData, setFormData] = useState({
    contractor_id: 0,
    project_id: 0,
    price: 0,
    duration: 0,
    site_inspection: true,
    estimated_savings: 0,
  });

  const handleChange = (e) => {
    const { name, value, type, checked } = e.target;
    setFormData({
      ...formData,
      [name]: type === 'checkbox' ? checked : Number(value),
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch('http://localhost:8000/bid', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
      });
      if (response.ok) {
        alert('Bid submitted successfully.');
      } else {
        alert('Failed to submit bid.');
      }
    } catch (error) {
      console.error('Error:', error);
      alert('An error occurred while submitting the bid.');
    }
  };

  return (
    <div className="space-y-10 divide-y divide-gray-900/10 p-20">
      <div className="grid grid-cols-1 gap-x-8 gap-y-8 pt-10 md:grid-cols-3">
        <div className="px-4 sm:px-0">
          <h2 className="text-base font-semibold leading-7 text-gray-900">Bid Information</h2>
          <p className="mt-1 text-sm leading-6 text-gray-600">Enter the bid details below.</p>
        </div>

        <form onSubmit={handleSubmit} className="bg-white shadow-sm ring-1 ring-gray-900/5 sm:rounded-xl md:col-span-2">
          <div className="px-4 py-6 sm:p-8">
            <div className="grid max-w-2xl grid-cols-1 gap-x-6 gap-y-8 sm:grid-cols-6">
              <div className="sm:col-span-3">
                <label htmlFor="contractor_id" className="block text-sm font-medium leading-6 text-gray-900">
                  Contractor ID
                </label>
                <div className="mt-2">
                  <input
                    id="contractor_id"
                    name="contractor_id"
                    type="number"
                    value={formData.contractor_id}
                    onChange={handleChange}
                    className="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
                  />
                </div>
              </div>

              <div className="sm:col-span-3">
                <label htmlFor="project_id" className="block text-sm font-medium leading-6 text-gray-900">
                  Project ID
                </label>
                <div className="mt-2">
                  <input
                    id="project_id"
                    name="project_id"
                    type="number"
                    value={formData.project_id}
                    onChange={handleChange}
                    className="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
                  />
                </div>
              </div>

              <div className="sm:col-span-3">
                <label htmlFor="price" className="block text-sm font-medium leading-6 text-gray-900">
                  Price
                </label>
                <div className="mt-2">
                  <input
                    id="price"
                    name="price"
                    type="number"
                    value={formData.price}
                    onChange={handleChange}
                    className="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
                  />
                </div>
              </div>

              <div className="sm:col-span-3">
                <label htmlFor="duration" className="block text-sm font-medium leading-6 text-gray-900">
                  Duration (days)
                </label>
                <div className="mt-2">
                  <input
                    id="duration"
                    name="duration"
                    type="number"
                    value={formData.duration}
                    onChange={handleChange}
                    className="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
                  />
                </div>
              </div>

              <div className="col-span-full">
                <label htmlFor="site_inspection" className="block text-sm font-medium leading-6 text-gray-900">
                  Site Inspection
                </label>
                <div className="mt-2 flex items-center">
                  <input
                    id="site_inspection"
                    name="site_inspection"
                    type="checkbox"
                    checked={formData.site_inspection}
                    onChange={handleChange}
                    className="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-600"
                  />
                  <span className="ml-3 text-sm leading-6 text-gray-600">Required</span>
                </div>
              </div>

              <div className="sm:col-span-3">
                <label htmlFor="estimated_savings" className="block text-sm font-medium leading-6 text-gray-900">
                  Estimated Savings
                </label>
                <div className="mt-2">
                  <input
                    id="estimated_savings"
                    name="estimated_savings"
                    type="number"
                    value={formData.estimated_savings}
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
              Submit Bid
            </button>
          </div>
        </form>
      </div>
    </div>
  );
}
