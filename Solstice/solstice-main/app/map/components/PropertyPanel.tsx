import { Property } from "@/app/models/property.model"

interface PropertyPanelProps {
    property: Property
}

const PropertyPanel = ({ property }: PropertyPanelProps) => {

    return (
        <div className="bg-gray-900 text-gray-200 rounded-lg shadow-lg p-6">
            <h2 className="text-2xl font-bold mb-4">Property Details</h2>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div>
                    <h3 className="font-semibold mb-2">Address</h3>
                    <p className="text-sm mb-1"><span className="font-bold">UPRN:</span> {property.uprn}</p>
                    <p className="text-sm mb-1"><span className="font-bold">Address 1:</span> {property.address_1}</p>
                    <p className="text-sm mb-1"><span className="font-bold">Address 2:</span> {property.address_2}</p>
                    <p className="text-sm mb-1"><span className="font-bold">Address 3:</span> {property.address_3}</p>
                    <p className="text-sm mb-1"><span className="font-bold">Postcode:</span> {property.postcode}</p>
                </div>
                <div>
                    <h3 className="font-semibold mb-2">Property Info</h3>
                    <p className="text-sm mb-1"><span className="font-bold">Asset Rating:</span> {property.asset_rating} ({property.asset_rating_band})</p>
                    {/* <p><EpcRatingBar epcRating={property.asset_rating_band}></EpcRatingBar></p> */}
                    <p className="text-sm mb-1"><span className="font-bold">Floor Area:</span> {property.floor_area} sqm</p>
                    <p className="text-sm mb-1"><span className="font-bold">Building Level:</span> {property.building_level}</p>
                    <p className="text-sm mb-1"><span className="font-bold">Main Heating Fuel:</span> {property.main_heating_fuel}</p>
                    <p className="text-sm mb-1"><span className="font-bold">Title Number:</span> {property.title_number}</p>
                </div>
                <div>
                    <h3 className="font-semibold mb-2">Energy & Emissions</h3>
                    <p className="text-sm mb-1"><span className="font-bold">Annual Energy Usage:</span> {property.annual_energy_usage} kWh</p>
                    <p className="text-sm mb-1"><span className="font-bold">Building Emissions:</span> {property.building_emissions} kg CO2</p>
                    <p className="text-sm mb-1"><span className="font-bold">Potential Energy Savings:</span> {property.potential_energy_savings} kWh</p>
                    <p className="text-sm mb-1"><span className="font-bold">Yield Potential:</span> {property.yield_potential}</p>
                </div>
                <div>
                    <h3 className="font-semibold mb-2">Location</h3>
                    <p className="text-sm mb-1"><span className="font-bold">Latitude:</span> {property.latitude}</p>
                    <p className="text-sm mb-1"><span className="font-bold">Longitude:</span> {property.longitude}</p>
                    <p className="text-sm mb-1"><span className="font-bold">DNO Substation Status:</span> {property.dno_substation_status}</p>
                </div>
            </div>
        </div>
    );
}

export default PropertyPanel;