import { useMapContext } from "@/contexts/mapdata/useMapContext";
import PropertySideCard from "./PropertySideCard";

const PropertyList = () => {
    const {data} = useMapContext();
    return (
        <ul role="list" className="flex flex-1 flex-col gap-y-7">
            <li>
                <ul role="list" className="-mx-2 space-y-1">
                    {data?.map((property) => <PropertySideCard property={property}></PropertySideCard>)}
                </ul>
            </li>
        </ul>
    );

}

export default PropertyList;