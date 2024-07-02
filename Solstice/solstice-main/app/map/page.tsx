"use client";

import { MapContextProvider } from '@/contexts/mapdata/MapContextProvider';
import { useMapContext } from '@/contexts/mapdata/useMapContext';
import LeafletMap from './components/LeafletMap';
import { Property } from '../models/property.model';
import PropertyPanel from './components/PropertyPanel';
import { HomeIcon } from '@heroicons/react/24/outline';
import PropertyPanelEmpty from './components/PropertyPanelEmpty';

const MapPage = () => {
    const { selectedProperty } = useMapContext();

    return (
        <>
            <LeafletMap></LeafletMap>

            <div className='my-2'>
                {selectedProperty ? <PropertyPanel property={selectedProperty} /> : <PropertyPanelEmpty />}
            </div>
        </>
    );
}




export default MapPage;