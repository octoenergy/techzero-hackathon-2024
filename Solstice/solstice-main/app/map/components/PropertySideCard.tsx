import { Property } from "@/app/models/property.model";
import { useMapContext } from "@/contexts/mapdata/useMapContext";
import { BuildingOfficeIcon, MapIcon } from "@heroicons/react/24/outline";

const PropertySideCard = ({ property }: { property: Property }) => {
  const {setSelectedProperty, selectedProperty} = useMapContext();

    const selectedClass = property.address_1 === selectedProperty?.address_1 ? 'text-white group flex flex-col gap-y-2 rounded-md p-4 text-sm font-semibold leading-6 bg-gray-700 border-white border transition ' : 'bg-gray-800 text-white group flex flex-col gap-y-2 rounded-md p-4 text-sm font-semibold leading-6 hover:bg-gray-700 transition'

    if (!property.address_1) {
        return null;
    }


    return (
        <li className="py-1">
            <a
                href={'#'}
                onClick={() => setSelectedProperty(property)}
                className={selectedClass}
            >
                <div className="flex gap-x-3 items-center">
                    <BuildingOfficeIcon className="h-6 w-6 shrink-0" aria-hidden="true" />
                    <span>{property.address_1}</span>
                </div>
                <div className="flex justify-between flex-1 flex-col mt-2">
                    <span className="text-green-400">Energy Savings: {property.potential_energy_savings ?? "£?"}</span>
                    <span className="text-gray-400">Company {property.company_registration_number}</span>
                </div>
            </a>
        </li>
    );
}

export default PropertySideCard;