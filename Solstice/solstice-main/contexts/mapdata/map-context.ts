import { Property } from '@/app/models/property.model';
import { Map } from 'leaflet';
import { Dispatch, SetStateAction, createContext } from 'react';


export type MapContextData = {
    data: Property[] | undefined;
    selectedProperty: Property | null;
    setSelectedProperty: Dispatch<SetStateAction<Property | null>>;

    map: Map | undefined;
    setMap: Dispatch<SetStateAction<Map | null>>;
};

export const MapContext = createContext<MapContextData>({
    data: undefined,
    selectedProperty: null,
    setSelectedProperty: () => {},
    map: undefined,
    setMap: () => {},
});