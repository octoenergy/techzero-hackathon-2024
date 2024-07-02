import { Property } from '@/app/models/property.model';
import { Dispatch, SetStateAction, createContext } from 'react';


export type MapContextData = {
    data: Property[] | undefined;
    selectedProperty: Property | null;
    setSelectedProperty: Dispatch<SetStateAction<Property | null>>;
};

export const MapContext = createContext<MapContextData>({
    data: undefined,
    selectedProperty: null,
    setSelectedProperty: () => {},
});