import React, { useEffect, useState } from 'react';
import { MapContext, MapContextData } from './map-context';
import { Property } from '@/app/models/property.model';

type MapContextProviderProps = {
    children: JSX.Element | string;
};

export const MapContextProvider = ({ children }: MapContextProviderProps) => {
    const [map, setMap] = useState<Map>()
    const [data, setData] = useState<Property[] | undefined>();
    const [selectedProperty, setSelectedProperty] = useState<Property | null>(null)

    useEffect(() => {
        async function fetchData() {
            console.log('fetching data')
            const response = await fetch('/api/property');
            const result = await response.json();
            console.log('Data', result)

            // order data by energy saving
            
            if (result) {
                result.sort((a: Property,b: Property) => b.optimal_savings - a.optimal_savings);
            }

            setData(result);
        }
        console.log('use effect')

        fetchData();
    }, []);

    useEffect(() => {
        console.log('selected Property change', selectedProperty)
    }, [selectedProperty])

    const value: MapContextData = {
        data,
        selectedProperty,
        setSelectedProperty,
        map,
        setMap
    };

    return <MapContext.Provider value={value}>{children}</MapContext.Provider>;
};