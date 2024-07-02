"use client";
import { MapContainer, TileLayer } from 'react-leaflet'
import 'leaflet/dist/leaflet.css';
import "leaflet-defaulticon-compatibility"
import "leaflet-defaulticon-compatibility/dist/leaflet-defaulticon-compatibility.css"


import MarkerClusterGroup from 'next-leaflet-cluster';
import 'next-leaflet-cluster/lib/assets/MarkerCluster.css'
import 'next-leaflet-cluster/lib/assets/MarkerCluster.Default.css'
import 'next-leaflet-cluster/lib/assets/marker-icon-2x.png'
import 'next-leaflet-cluster/lib/assets/marker-icon.png'
import 'next-leaflet-cluster/lib/assets/marker-shadow.png'

import { Property } from '../../models/property.model';
import { useMapContext } from '@/contexts/mapdata/useMapContext';
import PropertyMarker from './PropertyMarker';


const LeafletMap = () => {
    const { data, setMap } = useMapContext();

    return (
        <>
            <MapContainer ref={setMap} center={[51.505, -0.09]} zoom={13} scrollWheelZoom={true} className='rounded-lg'>
                <TileLayer
                    attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
                    url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
                />

                <MarkerClusterGroup>

                    {data ? data?.map((property: Property) => {
                        // return null
                        return (
                            <PropertyMarker property={property} />
                        );
                    }) : null}
                </MarkerClusterGroup>
            </MapContainer>
        </>
    );
}

export default LeafletMap