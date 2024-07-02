import { Property } from "@/app/models/property.model";
import { Marker, Popup } from "react-leaflet";

interface PropertyMarkerProps {
    property: Property
}
import { icon } from 'leaflet';
import { useMapContext } from "@/contexts/mapdata/useMapContext";

const lIcon = icon({ iconUrl: "/images/marker-icon.png" });


const PropertyMarker = ({ property }: PropertyMarkerProps) => {
    const {setSelectedProperty} = useMapContext();
    return (
        <Marker position={[property.latitude ?? 0, property.longitude ?? 0]} icon={lIcon}
            eventHandlers={{
                click: (e) => {
                    console.log('marker clicked', e)
                    setSelectedProperty(property)
                    // alert(`${property.address_1} clicked`)

                    // set selected = property.id
                },
            }}
        >
            {/* <Popup>
                {JSON.stringify(property)}
            </Popup> */}
        </Marker>
    );
}

export default PropertyMarker;