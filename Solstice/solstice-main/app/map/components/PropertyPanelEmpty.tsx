import { HomeIcon } from "@heroicons/react/24/outline"


const PropertyPanelEmpty = () => {
    return (
        <div
            className="relative block w-full rounded-lg border-2 border-dashed border-gray-300 text-gray-400 p-12 text-center hover:border-gray-400 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2"
        >
            <HomeIcon className="mx-auto h-12 w-12 "></HomeIcon>
            <span className="mt-2 block text-sm font-semibold ">Select a property to view details</span>
        </div>
    )
}

export default PropertyPanelEmpty